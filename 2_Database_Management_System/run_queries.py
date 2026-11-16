import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "smart_campus.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def print_separator(title):
    print("\n" + "=" * 90)
    print(f" {title}")
    print("=" * 90)

# Query 1
print_separator("QUERY 1: Student Registrations with Event & Attendance Details (Multi-Table JOIN)")
q1 = """
SELECT 
    s.student_id,
    SUBSTR(s.name, 1, 15) AS student_name,
    SUBSTR(s.department, 1, 18) AS dept,
    e.event_id,
    SUBSTR(e.event_name, 1, 24) AS event_title,
    COALESCE(a.attendance_status, 'Pending') AS status,
    COALESCE(a.certificate_status, 'Pending') AS cert
FROM registrations r
JOIN students s ON r.student_id = s.student_id
JOIN events e ON r.event_id = e.event_id
LEFT JOIN attendance a ON r.registration_id = a.registration_id
LIMIT 10;
"""
cursor.execute(q1)
print(f"{'Student ID':<12} {'Student Name':<17} {'Department':<20} {'Event ID':<10} {'Event Title':<26} {'Status':<10} {'Certificate':<12}")
print("-" * 107)
for row in cursor.fetchall():
    print(f"{row[0]:<12} {row[1]:<17} {row[2]:<20} {row[3]:<10} {row[4]:<26} {row[5]:<10} {row[6]:<12}")

# Query 2
print_separator("QUERY 2: Event Summary (Aggregations, GROUP BY, Attendance Rate %)")
q2 = """
SELECT 
    e.event_id,
    SUBSTR(e.event_name, 1, 28) AS event_name,
    e.category,
    e.max_participants,
    COUNT(r.registration_id) AS registered,
    SUM(CASE WHEN a.attendance_status = 'Present' THEN 1 ELSE 0 END) AS present,
    COALESCE(ROUND((CAST(SUM(CASE WHEN a.attendance_status = 'Present' THEN 1 ELSE 0 END) AS FLOAT) / 
          NULLIF(COUNT(r.registration_id), 0)) * 100, 1), 0.0) AS att_pct
FROM events e
LEFT JOIN registrations r ON e.event_id = r.event_id
LEFT JOIN attendance a ON r.registration_id = a.registration_id
GROUP BY e.event_id, e.event_name, e.category, e.max_participants
ORDER BY registered DESC;
"""
cursor.execute(q2)
print(f"{'Event ID':<10} {'Event Name':<30} {'Category':<22} {'Capacity':<10} {'Reg':<6} {'Att':<6} {'Att %':<8}")
print("-" * 92)
for row in cursor.fetchall():
    att_pct_str = f"{row[6]:.1f}%"
    print(f"{row[0]:<10} {row[1]:<30} {row[2]:<22} {row[3]:<10} {row[4]:<6} {row[5]:<6} {att_pct_str:<8}")

# Query 3
print_separator("QUERY 3: Department-wise Participation Statistics")
q3 = """
SELECT 
    s.department,
    COUNT(DISTINCT s.student_id) AS distinct_students,
    COUNT(r.registration_id) AS total_registrations,
    SUM(CASE WHEN a.attendance_status = 'Present' THEN 1 ELSE 0 END) AS attended_events
FROM students s
LEFT JOIN registrations r ON s.student_id = r.student_id
LEFT JOIN attendance a ON r.registration_id = a.registration_id
GROUP BY s.department
ORDER BY total_registrations DESC;
"""
cursor.execute(q3)
print(f"{'Department':<32} {'Active Students':<18} {'Registrations':<16} {'Attended':<10}")
print("-" * 76)
for row in cursor.fetchall():
    print(f"{row[0]:<32} {row[1]:<18} {row[2]:<16} {row[3]:<10}")

# Query 4: Subquery
print_separator("QUERY 4: Subquery - Students with Above-Average Event Registrations")
q4 = """
SELECT 
    s.student_id,
    s.name,
    s.department,
    COUNT(r.registration_id) AS participation_count
FROM students s
JOIN registrations r ON s.student_id = r.student_id
GROUP BY s.student_id, s.name, s.department
HAVING COUNT(r.registration_id) > (
    SELECT AVG(cnt) FROM (
        SELECT COUNT(registration_id) AS cnt FROM registrations GROUP BY student_id
    )
)
ORDER BY participation_count DESC;
"""
cursor.execute(q4)
print(f"{'Student ID':<12} {'Student Name':<20} {'Department':<30} {'Participations':<15}")
print("-" * 77)
for row in cursor.fetchall():
    print(f"{row[0]:<12} {row[1]:<20} {row[2]:<30} {row[3]:<15}")

# Query 5: Window Function Leaderboard
print_separator("QUERY 5: Window Function - Campus Event Leaderboard (DENSE_RANK)")
q5 = """
SELECT 
    s.student_id,
    s.name,
    s.department,
    COUNT(r.registration_id) AS total_events,
    SUM(CASE WHEN a.attendance_status = 'Present' THEN 1 ELSE 0 END) AS attended,
    DENSE_RANK() OVER (ORDER BY COUNT(r.registration_id) DESC) AS rank
FROM students s
JOIN registrations r ON s.student_id = r.student_id
LEFT JOIN attendance a ON r.registration_id = a.registration_id
GROUP BY s.student_id, s.name, s.department
LIMIT 6;
"""
cursor.execute(q5)
print(f"{'Rank':<6} {'Student ID':<12} {'Student Name':<20} {'Department':<28} {'Registered':<12} {'Attended':<10}")
print("-" * 88)
for row in cursor.fetchall():
    print(f"{row[5]:<6} {row[0]:<12} {row[1]:<20} {row[2]:<28} {row[3]:<12} {row[4]:<10}")

# Query 6: Integrity Constraint Verification
print_separator("TEST CASE: Duplicate Registration Prevention (Functional Requirement 3)")
print("Attempting duplicate registration: student_id='25IT001' into event_id='EVT101'...")
try:
    cursor.execute("INSERT INTO registrations (student_id, event_id) VALUES ('25IT001', 'EVT101');")
    conn.commit()
    print("[FAIL] Duplicate registration was permitted!")
except sqlite3.IntegrityError as e:
    print(f"[PASS] Integrity Constraint Blocked Duplicate Registration Successfully!")
    print(f"       Database Error Message: {e}")

conn.close()
print("\n" + "=" * 90)
print(" DBMS Execution Completed Successfully.")
print("=" * 90)
