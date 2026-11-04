"""
Day 2 - the fact store: durable, timestamped, queryable memory.

A fact is a row: what it says, when it was learned, where it came from.
SQLite, standard library, one file on disk next to the agent. Two
operations only: remember() writes a fact, recall() reads facts back by
keyword, newest first. Deliberately dumb retrieval: the discipline is
deliberate writes and honest timestamps, not search quality.
"""

import os
import sqlite3
from datetime import datetime, timezone

# This instructs where the database lives - inside the DB_PATH variable
# Places DB_PATH in same folder as fact_store.py
# --file-- hands the path of the currently running file as a string
# os.path.abspath(__file__) expands __file__ to full adress from drive root, in case the path is relative
# os.path.dirname(...) keeps only the folder, throws away the file name
# os.path.join(folder, "facts.db") places facts.db into the folder
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "facts.db")


def connect(path=DB_PATH):
    """
    Opens the store, creating a new facts table as if this is a new file,
    but only if it is missing (IF NOT EXISTS).
    """
    conn = sqlite3.connect(path)
    conn.execute("""CREATE TABLE IF NOT EXISTS facts (
        id INTEGER PRIMARY KEY,
        fact_text TEXT NOT NULL,
        learned_at TEXT NOT NULL,
        source TEXT)""")
    return conn


def remember(conn, fact, source, learned_at=None):
    """Write one fact. The timestamp defaults to now and is never optional
    in the table: a fact without a when cannot take part in Friday's
    stale-fact questions at all."""
    conn.execute(
        "INSERT INTO facts (fact_text, learned_at, source) VALUES (?, ?, ?)",
        (fact, learned_at or _now_iso(), source))
    conn.commit()


def _now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def recall (conn, query):
    """
    Facts containing the query text, newest first. when two facts
    contradict, the freshest is returned on top; whether it should win 
    is not decided here.  The caller will decide this.
    """
    return conn.execute(
        "SELECT fact_text, learned_at, source FROM facts "
        "WHERE fact_text LIKE ? ORDER BY learned_at DESC",
        (f"%{query}%",)).fetchall()


if __name__ == "__main__":
    # Self-test: write in this process, read back in the same breath.
    # The real test is tomorrow's: a different process, same file.
    db = connect()
    remember(db, "SAFE_DIR is the sandbox", "fact_store self-test")
    remember(db, "The restart is the test: memory that dies with the "
                 "process isn't memory", "fact_store self-test")
    for fact, learned_at, source in recall(db, "sandbox"):
        print(f"{fact}  [{learned_at}, {source}]")

