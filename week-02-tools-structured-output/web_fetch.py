"""Fetch a URL's text. Unhappy paths return structured errors, never exceptions."""

import httpx
from html.parser import HTMLParser

MAX_CHARS = 50000  # cap: the model's context is not infinite


class _TextExtractor(HTMLParser):
    """Collects visible text, skipping script and style content."""

    def __init__(self):
        super().__init__()
        self.parts = []
        self._skip = 0  # depth inside a script/style tag

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip = max(0, self._skip - 1)

    def handle_data(self, data):
        if self._skip == 0:
            self.parts.append(data)

    def text(self):
        raw = " ".join(self.parts)
        return " ".join(raw.split())  # collapse all whitespace runs


def fetch_url(url, timeout=15):
    """Return {'ok': True, 'url': ..., 'text': ...} or {'ok': False, 'error': ..., 'detail': ...}."""
    try:
        response = httpx.get(url, timeout=timeout, follow_redirects=True)
    except httpx.TimeoutException as e:
        return {"ok": False, "error": "timeout", "detail": str(e)}
    except httpx.RequestError as e:
        return {"ok": False, "error": "request_error", "detail": str(e)}

    if response.status_code == 404:
        return {"ok": False, "error": "http_404", "detail": f"Server returned 404 for {url}"}
    if not 200 <= response.status_code < 300:
        return {"ok": False, "error": "http_error", "detail": f"Server returned {response.status_code} for {url}"}

    content_type = response.headers.get("content-type", "")
    if "text/html" not in content_type:
        return {"ok": False, "error": "non_html", "detail": f"Content-Type is {content_type!r}, not HTML"}

    extractor = _TextExtractor()
    extractor.feed(response.text)
    text = extractor.text()[:MAX_CHARS]
    return {"ok": True, "url": url, "text": text}
