-- ============================================================================
-- VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY (AUTONOMOUS), ERODE - 12
-- DEPARTMENT OF INFORMATION TECHNOLOGY
-- ACADEMIC YEAR: 2026-27 (ODD) | CLASS: 25IT3A&B
-- PROJECT-BASED ASSESSMENT
-- Scenario 6: Smart Campus Event Management & Student Participation Analysis System
-- File: queries.sql (SQL Queries Covering Syllabus: Joins, Subqueries, Aggregations, Views)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- Query 1: Basic Retrieval & Multi-Table INNER JOIN
-- Retrieve student name, department, event name, category, and attendance status
-- ----------------------------------------------------------------------------
SELECT 
    s.student_id,
    s.name AS student_name,
    s.department,
    e.event_id,
    e.event_name,
    e.category,
    r.registration_date,
    COALESCE(a.attendance_status, 'Not Recorded') AS attendance_status,
    COALESCE(a.certificate_status, 'N/A') AS certificate_status
FROM registrations r
JOIN students s ON r.student_id = s.student_id
JOIN events e ON r.event_id = e.event_id
LEFT JOIN attendance a ON r.registration_id = a.registration_id
ORDER BY e.event_id, s.student_id;

-- ----------------------------------------------------------------------------
-- Query 2: Aggregate Analysis with GROUP BY & HAVING
-- Calculate Event-wise Registrations, Attended Count, Absent Count, and Attendance %
-- ----------------------------------------------------------------------------
SELECT 
    e.event_id,
    e.event_name,
    e.category,
    e.max_participants,
    COUNT(r.registration_id) AS total_registered,
    SUM(CASE WHEN a.attendance_status = 'Present' THEN 1 ELSE 0 END) AS total_present,
    SUM(CASE WHEN a.attendance_status = 'Absent' THEN 1 ELSE 0 END) AS total_absent,
    ROUND(
        (CAST(SUM(CASE WHEN a.attendance_status = 'Present' THEN 1 ELSE 0 END) AS FLOAT) / 
         NULLIF(COUNT(r.registration_id), 0)) * 100, 2
    ) AS attendance_rate_pct
FROM events e
LEFT JOIN registrations r ON e.event_id = r.event_id
LEFT JOIN attendance a ON r.registration_id = a.registration_id
GROUP BY e.event_id, e.event_name, e.category, e.max_participants
HAVING COUNT(r.registration_id) > 0
ORDER BY total_registered DESC;

-- ----------------------------------------------------------------------------
-- Query 3: Department-wise Participation Distribution
-- Find total registrations across college departments
-- ----------------------------------------------------------------------------
SELECT 
    s.department,
    COUNT(DISTINCT s.student_id) AS active_students,
    COUNT(r.registration_id) AS total_event_registrations,
    SUM(CASE WHEN a.attendance_status = 'Present' THEN 1 ELSE 0 END) AS total_attended
FROM students s
LEFT JOIN registrations r ON s.student_id = r.student_id
LEFT JOIN attendance a ON r.registration_id = a.registration_id
GROUP BY s.department
ORDER BY total_event_registrations DESC;

-- ----------------------------------------------------------------------------
-- Query 4: Subquery (Correlated / Scalar)
-- Find students whose event participation count is strictly greater than average
-- ----------------------------------------------------------------------------
SELECT 
    s.student_id,
    s.name,
    s.department,
    s.year_of_study,
    COUNT(r.registration_id) AS participation_count
FROM students s
JOIN registrations r ON s.student_id = r.student_id
GROUP BY s.student_id, s.name, s.department, s.year_of_study
HAVING COUNT(r.registration_id) > (
    -- Average participation count per student
    SELECT AVG(reg_count) FROM (
        SELECT COUNT(registration_id) AS reg_count
        FROM registrations
        GROUP BY student_id
    )
)
ORDER BY participation_count DESC;

-- ----------------------------------------------------------------------------
-- Query 5: Window Function - Leaderboard Ranking
-- Rank top participating students across the entire institution
-- ----------------------------------------------------------------------------
SELECT 
    s.student_id,
    s.name,
    s.department,
    COUNT(r.registration_id) AS total_events,
    SUM(CASE WHEN a.attendance_status = 'Present' THEN 1 ELSE 0 END) AS events_attended,
    DENSE_RANK() OVER (ORDER BY COUNT(r.registration_id) DESC) AS campus_rank
FROM students s
JOIN registrations r ON s.student_id = r.student_id
LEFT JOIN attendance a ON r.registration_id = a.registration_id
GROUP BY s.student_id, s.name, s.department
ORDER BY campus_rank ASC, s.name ASC;

-- ----------------------------------------------------------------------------
-- Query 6: Event Feedback & Average Rating by Event
-- ----------------------------------------------------------------------------
SELECT 
    e.event_id,
    e.event_name,
    COUNT(f.feedback_id) AS total_feedbacks,
    ROUND(AVG(f.rating), 2) AS average_rating
FROM events e
JOIN registrations r ON e.event_id = r.event_id
JOIN event_feedback f ON r.registration_id = f.registration_id
GROUP BY e.event_id, e.event_name
ORDER BY average_rating DESC;

-- ----------------------------------------------------------------------------
-- Query 7: Duplicate Registration Prevention Demonstration
-- Attempting to insert a duplicate registration causes an Integrity Constraint Violation
-- (Demonstrated via simulated query)
-- ----------------------------------------------------------------------------
-- SELECT 'Testing Duplicate Prevention: Unique constraint (student_id, event_id)';
-- INSERT INTO registrations (student_id, event_id) VALUES ('25IT001', 'EVT101'); 
-- -> Output: Error: UNIQUE constraint failed: registrations.student_id, registrations.event_id
