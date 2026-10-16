# Week 2, Day 1 — Fetch a URL's Text (Monday, Oct 12)

## The idea

Week 1's tools were toys — a calculator and a dict of canned answers. Today the
agent touches the real world for the first time: the web. The real world is messy
in ways a calculator never is — pages time out, servers return 404s, half the
"pages" you fetch are PDFs. The lesson today is the one that carries through the
whole week: **unhappy paths come back as observations, not exceptions.** Your
Week 1 loop already does this for malformed replies; today your tools start
doing it for the network.

## What you'll build

`week-02-real-tools/web_fetch.py` with one tool:

- **`fetch_url(url, timeout=15) -> dict`** — returns the page's clean text, or a
  structured error: `{"ok": false, "error": "timeout|http_404|non_html|...", "detail": ...}`.
- Text extraction: strip scripts, styles, nav boilerplate — `html.parser` plus a
  little cleanup is enough. No BeautifulSoup dependency if you want to keep it
  dependency-free; if you already have `requests` or `httpx` installed, use it,
  otherwise `pip install httpx` in your Anaconda env today.
- Register it in the same registry pattern from Week 1: name, description, parameter
  schema, error contract. The registry doesn't know or care that this tool is real.

## Steps

1. **Install.** `pip install httpx` (or requests — your pick, one only).
2. **Write `fetch_url`.** Handle, in order: DNS/timeout, non-2xx status, non-HTML
   content type, and absurdly large pages (cap at ~50KB of text — the model's
   context is not infinite).
3. **Wire it through the registry.** Same `run_tool` dispatch as Week 1. The loop
   from Day 4 doesn't change at all — that's the point. New hands, same engine.
4. **Test with three URLs:** one normal article, one that 404s, one non-HTML file
   (a PDF link is a good one). Each must come back as a clean observation the
   loop can read — including the failures.

## Done criteria (binary)

- [ ] `fetch_url` returns clean text for a real article page.
- [ ] A 404 and a non-HTML response each return a structured error observation,
      not an exception — verified by running them through the registry.

## What this unlocks

- **Tue:** two more tools — the shell and the filesystem. Three real hands.
- **Week 6:** these error contracts are what your eval harness will grade.

## Likely snag

**A JS-heavy page returns almost no text.** Your tool reads raw HTML, not a
rendered page — that's a real limitation, not a bug. Park it. Chasing a headless
browser this week is scope creep; file it in the parking lot and move on.

## When you're done

Reply "Day 1 done". Tomorrow's sheet: the shell and the filesystem.
