import sqlite3
import os
import sys

# Switch to script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

db_paths = [
    "smart_campus.db",
    "../smart_campus.db"
]
db_path = next((p for p in db_paths if os.path.exists(p)), None)

if not db_path:
    print("[ERROR] smart_campus.db not found!")
    sys.exit(1)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def print_banner():
    print("=" * 90)
    print(" VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY (AUTONOMOUS), ERODE - 12")
    print(" DEPARTMENT OF INFORMATION TECHNOLOGY | CLASS: 25IT3A&B | COURSE: 25ITT31 - DBMS")
    print(" SMART CAMPUS DATABASE INTERACTIVE SQL QUERY CONSOLE")
    print("=" * 90)
    print(" Connected Database: " + os.path.abspath(db_path))
    print(" Available Tables: students, events, registrations, attendance, event_feedback")
    print(" Available Views : view_event_summary")
    print("-" * 90)
    print(" Commands:")
    print("   - Type any SQL query (e.g. SELECT * FROM students LIMIT 5;) and press Enter")
    print("   - Type 'tables' to inspect all tables and column schemas")
    print("   - Type 'run-all' to execute all syllabus queries with formatted tables")
    print("   - Type 'exit' or 'quit' to close")
    print("=" * 90 + "\n")

def show_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type IN ('table', 'view') AND name NOT LIKE 'sqlite_%';")
    tables = cursor.fetchall()
    print("\n--- DATABASE SCHEMA OBJECTS ---")
    for t in tables:
        t_name = t[0]
        cursor.execute(f"PRAGMA table_info({t_name});")
        cols = [f"{col[1]} ({col[2]})" for col in cursor.fetchall()]
        print(f" • {t_name.upper()}:")
        print(f"     Columns: {', '.join(cols)}")
    print()

def execute_query(sql):
    try:
        cursor.execute(sql)
        if sql.strip().upper().startswith("SELECT") or sql.strip().upper().startswith("PRAGMA"):
            rows = cursor.fetchall()
            if not rows:
                print(" -> (0 rows returned)")
                return
            
            headers = [d[0] for d in cursor.description]
            col_widths = [len(h) for h in headers]
            for row in rows[:50]:
                for i, val in enumerate(row):
                    col_widths[i] = max(col_widths[i], len(str(val)))
            
            header_str = " | ".join(f"{h:<{col_widths[i]}}" for i, h in enumerate(headers))
            separator = "-+-".join("-" * col_widths[i] for i in range(len(headers)))
            print("\n" + header_str)
            print(separator)
            
            for row in rows[:50]:
                row_str = " | ".join(f"{str(val if val is not None else 'NULL'):<{col_widths[i]}}" for i, val in enumerate(row))
                print(row_str)
            
            print(f"\n -> Total Rows: {len(rows)}\n")
        else:
            conn.commit()
            print(f" -> Query OK. Rows affected: {cursor.rowcount}\n")
    except sqlite3.Error as e:
        print(f" -> [SQL Error]: {e}\n")

if __name__ == "__main__":
    print_banner()
    while True:
        try:
            query = input("SQL> ").strip()
            if not query:
                continue
            if query.lower() in ("exit", "quit"):
                print("Exiting SQL Console. Goodbye!")
                break
            elif query.lower() == "tables":
                show_tables()
            elif query.lower() == "run-all":
                import subprocess
                subprocess.run([sys.executable, "run_queries.py"])
            else:
                execute_query(query)
        except (KeyboardInterrupt, EOFError):
            print("\nSession ended.")
            break

conn.close()
