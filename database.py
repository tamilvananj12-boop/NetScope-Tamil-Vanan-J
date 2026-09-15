import sqlite3
from pathlib import Path
DB_PATH = Path("netscope.db")
def get_connection():
    conn = sqlite3.connect(DB_PATH); conn.row_factory = sqlite3.Row; return conn
def init_db():
    with get_connection() as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS scans (id INTEGER PRIMARY KEY AUTOINCREMENT, target TEXT NOT NULL, scanned_at TEXT NOT NULL, duration REAL NOT NULL, open_services INTEGER NOT NULL, report_file TEXT NOT NULL)")
def save_scan(target, scanned_at, duration, open_services, report_file):
    with get_connection() as conn:
        conn.execute("INSERT INTO scans (target, scanned_at, duration, open_services, report_file) VALUES (?, ?, ?, ?, ?)", (target, scanned_at, duration, open_services, report_file))
def list_scans():
    with get_connection() as conn: return conn.execute("SELECT * FROM scans ORDER BY id DESC").fetchall()
