# 2. Database Management System (DBMS)

This folder contains all the database assets for the **Smart Campus Event Management and Student Participation Analysis System** (Scenario 6) aligned with syllabus **25ITT31 - Database Management Systems**.

## Contents
* `DBMS_Design_and_Normalization.md`: Complete theoretical and practical report containing the ER diagram, relational model, step-by-step normalization analysis (1NF through BCNF), and SQL query execution analysis.
* `schema.sql`: DDL definitions creating tables (`students`, `events`, `registrations`, `attendance`, `event_feedback`), views (`view_event_summary`), indexes, and constraints.
* `seed_data.sql`: DML script ingesting 20 students, 8 events, 50 registrations, and attendance logs.
* `queries.sql`: Advanced SQL queries showcasing joins, aggregate metrics, subqueries, and window functions.
* `smart_campus.db`: The compiled SQLite relational database.
* `init_db.py`: Python automation script to rebuild the database from scratch.
* `run_queries.py`: Python execution and test script that verifies query outputs and duplicate prevention.
* `diagrams/er_diagram.png`: High-resolution Entity-Relationship (ER) diagram.
* `screenshots/dbms_execution_screenshot.png`: Execution screenshot showing terminal output of database operations.

## How to Run
```bash
# Re-initialize the database
python init_db.py

# Execute all queries and run the duplicate registration test
python run_queries.py
```
