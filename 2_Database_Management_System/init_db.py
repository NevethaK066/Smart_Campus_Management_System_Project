import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "smart_campus.db")

# Read schema and seed files
with open(os.path.join(os.path.dirname(__file__), "schema.sql"), "r") as f:
    schema_sql = f.read()

with open(os.path.join(os.path.dirname(__file__), "seed_data.sql"), "r") as f:
    seed_sql = f.read()

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Enable foreign keys
cursor.execute("PRAGMA foreign_keys = ON;")

# Execute schema script
cursor.executescript(schema_sql)
print("[OK] Schema executed successfully.")

# Execute seed data script
cursor.executescript(seed_sql)
print("[OK] Seed data ingested successfully.")

# Verify counts
cursor.execute("SELECT COUNT(*) FROM students;")
print(f"Students count: {cursor.fetchone()[0]}")

cursor.execute("SELECT COUNT(*) FROM events;")
print(f"Events count: {cursor.fetchone()[0]}")

cursor.execute("SELECT COUNT(*) FROM registrations;")
print(f"Registrations count: {cursor.fetchone()[0]}")

cursor.execute("SELECT COUNT(*) FROM attendance;")
print(f"Attendance records count: {cursor.fetchone()[0]}")

cursor.execute("SELECT COUNT(*) FROM event_feedback;")
print(f"Feedback records count: {cursor.fetchone()[0]}")

conn.commit()
conn.close()
print(f"[OK] Database created at: {db_path}")
