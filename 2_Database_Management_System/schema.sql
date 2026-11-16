-- ============================================================================
-- VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY (AUTONOMOUS), ERODE - 12
-- DEPARTMENT OF INFORMATION TECHNOLOGY
-- ACADEMIC YEAR: 2026-27 (ODD) | CLASS: 25IT3A&B
-- PROJECT-BASED ASSESSMENT
-- Scenario 6: Smart Campus Event Management & Student Participation Analysis System
-- File: schema.sql (Database Definition Language - DDL)
-- ============================================================================

-- Enable Foreign Key constraints in SQLite
PRAGMA foreign_keys = ON;

-- Drop existing tables in reverse dependency order
DROP TABLE IF EXISTS event_feedback;
DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS registrations;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS students;

-- ----------------------------------------------------------------------------
-- Table 1: students
-- Maintains student profile details
-- ----------------------------------------------------------------------------
CREATE TABLE students (
    student_id VARCHAR(15) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    year_of_study INTEGER NOT NULL CHECK (year_of_study BETWEEN 1 AND 4),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ----------------------------------------------------------------------------
-- Table 2: events
-- Maintains technical and non-technical campus event information
-- ----------------------------------------------------------------------------
CREATE TABLE events (
    event_id VARCHAR(15) PRIMARY KEY,
    event_name VARCHAR(150) NOT NULL,
    category VARCHAR(50) NOT NULL CHECK (category IN ('Technical Symposium', 'Workshop', 'Hackathon', 'Seminar', 'Cultural Fest', 'Webinar')),
    event_date DATE NOT NULL,
    venue VARCHAR(100) NOT NULL,
    max_participants INTEGER NOT NULL CHECK (max_participants > 0),
    organizer_dept VARCHAR(50) NOT NULL,
    status VARCHAR(20) DEFAULT 'Upcoming' CHECK (status IN ('Upcoming', 'Ongoing', 'Completed', 'Cancelled'))
);

-- ----------------------------------------------------------------------------
-- Table 3: registrations
-- Enrolls students into events with strict uniqueness constraint (Prevents Duplicate Registrations)
-- ----------------------------------------------------------------------------
CREATE TABLE registrations (
    registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id VARCHAR(15) NOT NULL,
    event_id VARCHAR(15) NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'Registered' CHECK (status IN ('Registered', 'Cancelled')),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    CONSTRAINT unq_student_event UNIQUE (student_id, event_id)
);

-- ----------------------------------------------------------------------------
-- Table 4: attendance
-- Records student event attendance, timestamp, and certificate issuance
-- ----------------------------------------------------------------------------
CREATE TABLE attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    registration_id INTEGER NOT NULL UNIQUE,
    attendance_status VARCHAR(20) NOT NULL CHECK (attendance_status IN ('Present', 'Absent')),
    checkin_time TIMESTAMP,
    certificate_status VARCHAR(20) DEFAULT 'Pending' CHECK (certificate_status IN ('Pending', 'Issued', 'Not Eligible')),
    remarks VARCHAR(255),
    FOREIGN KEY (registration_id) REFERENCES registrations(registration_id) ON DELETE CASCADE
);

-- ----------------------------------------------------------------------------
-- Table 5: event_feedback
-- Captures post-event student ratings and feedback
-- ----------------------------------------------------------------------------
CREATE TABLE event_feedback (
    feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
    registration_id INTEGER NOT NULL UNIQUE,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    comments TEXT,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (registration_id) REFERENCES registrations(registration_id) ON DELETE CASCADE
);

-- ----------------------------------------------------------------------------
-- Performance Indexes & Views
-- ----------------------------------------------------------------------------
CREATE INDEX idx_student_dept ON students(department);
CREATE INDEX idx_event_date ON events(event_date);
CREATE INDEX idx_reg_student ON registrations(student_id);
CREATE INDEX idx_reg_event ON registrations(event_id);

-- View: Event Attendance Summary View
CREATE VIEW view_event_summary AS
SELECT 
    e.event_id,
    e.event_name,
    e.category,
    e.event_date,
    e.max_participants,
    COUNT(r.registration_id) AS total_registrations,
    SUM(CASE WHEN a.attendance_status = 'Present' THEN 1 ELSE 0 END) AS total_attended,
    ROUND(
        (CAST(SUM(CASE WHEN a.attendance_status = 'Present' THEN 1 ELSE 0 END) AS FLOAT) / 
         NULLIF(COUNT(r.registration_id), 0)) * 100, 2
    ) AS attendance_percentage
FROM events e
LEFT JOIN registrations r ON e.event_id = r.event_id
LEFT JOIN attendance a ON r.registration_id = a.registration_id
GROUP BY e.event_id, e.event_name, e.category, e.event_date, e.max_participants;
