import sqlite3
from datetime import datetime, timedelta
import os
import re

DB_PATH = os.path.join('data', 'schedule.db')

TIME_RE = re.compile(r'(\b\d{1,2}(:\d{2})?\s*(am|pm)?\b|\bnoon\b|\bmidnight\b)', re.IGNORECASE)

def init_db():
    os.makedirs('data', exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS schedules (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    time TEXT,
                    task TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()
    conn.close()

def clear_old_schedules():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM schedules WHERE DATE(created_at) < DATE('now','-3 day')")
    conn.commit()
    conn.close()

def save_schedule_to_db(schedule):
    clear_old_schedules()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    for time, task in schedule:
        c.execute("INSERT INTO schedules (time, task) VALUES (?, ?)", (time, task))
    conn.commit()
    conn.close()

def get_all_schedules():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT time, task FROM schedules ORDER BY time ASC")
    rows = c.fetchall()
    conn.close()
    return [{'time': r[0], 'task': r[1]} for r in rows]

def parse_time_hint(line):
    now = datetime.now()
    match = TIME_RE.search(line)
    if match:
        text = match.group(0).lower()
        if text == "noon":
            return now.replace(hour=12, minute=0)
        elif text == "midnight":
            return now.replace(hour=0, minute=0)
        try:
            dt = datetime.strptime(text, "%I%p") if "am" in text or "pm" in text else datetime.strptime(text, "%H:%M")
            return now.replace(hour=dt.hour, minute=dt.minute)
        except Exception:
            pass
    return None

def build_schedule_for_today(instructions):
    now = datetime.now()
    current_time = now.replace(hour=9, minute=0, second=0, microsecond=0)
    schedule = []

    for line in instructions:
        hint = parse_time_hint(line)
        if hint:
            t = hint.strftime("%Y-%m-%d %H:%M")
        else:
            t = current_time.strftime("%Y-%m-%d %H:%M")
            current_time += timedelta(minutes=30)
        schedule.append((t, line))

    return schedule
