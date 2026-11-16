-- ============================================================================
-- VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY (AUTONOMOUS), ERODE - 12
-- DEPARTMENT OF INFORMATION TECHNOLOGY
-- ACADEMIC YEAR: 2026-27 (ODD) | CLASS: 25IT3A&B
-- PROJECT-BASED ASSESSMENT
-- Scenario 6: Smart Campus Event Management & Student Participation Analysis System
-- File: seed_data.sql (Sample Data Ingestion - DML)
-- ============================================================================

-- 1. Insert Student Records
INSERT INTO students (student_id, name, department, year_of_study, email, phone) VALUES
('25IT001', 'Aarav Sharma', 'Information Technology', 3, 'aarav.sharma@vcet.ac.in', '9842100001'),
('25IT006', 'Dinesh Kumar', 'Information Technology', 3, 'dinesh.k@vcet.ac.in', '9842100006'),
('25IT036', 'Kavya S', 'Information Technology', 3, 'kavya.s@vcet.ac.in', '9842100036'),
('25IT066', 'Manojkumar P', 'Information Technology', 3, 'manoj.p@vcet.ac.in', '9842100066'),
('25IT096', 'Swetha R', 'Information Technology', 3, 'swetha.r@vcet.ac.in', '9842100096'),
('25CS012', 'Bala Murugan', 'Computer Science & Engg', 2, 'bala.m@vcet.ac.in', '9842100012'),
('25CS045', 'Harini V', 'Computer Science & Engg', 4, 'harini.v@vcet.ac.in', '9842100045'),
('25CS089', 'Siddharth M', 'Computer Science & Engg', 3, 'siddharth.m@vcet.ac.in', '9842100089'),
('25EC015', 'Ananya G', 'Electronics & Comm Engg', 2, 'ananya.g@vcet.ac.in', '9842100015'),
('25EC052', 'Pradeep K', 'Electronics & Comm Engg', 3, 'pradeep.k@vcet.ac.in', '9842100052'),
('25AD010', 'Deepak Raja', 'Artificial Intelligence & DS', 2, 'deepak.r@vcet.ac.in', '9842100010'),
('25AD032', 'Nivetha S', 'Artificial Intelligence & DS', 3, 'nivetha.s@vcet.ac.in', '9842100032'),
('25EE022', 'Ramesh Babu', 'Electrical & Electronics Engg', 4, 'ramesh.b@vcet.ac.in', '9842100022'),
('25ME018', 'Vigneshwaran T', 'Mechanical Engineering', 3, 'vignesh.t@vcet.ac.in', '9842100018'),
('25CE009', 'Pooja Devi', 'Civil Engineering', 2, 'pooja.d@vcet.ac.in', '9842100009'),
('25IT015', 'Gokulnath C', 'Information Technology', 2, 'gokul.c@vcet.ac.in', '9842100015'),
('25IT028', 'Janani M', 'Information Technology', 4, 'janani.m@vcet.ac.in', '9842100028'),
('25CS061', 'Karthik S', 'Computer Science & Engg', 3, 'karthik.s@vcet.ac.in', '9842100061'),
('25AD045', 'Sneha Lakshmi', 'Artificial Intelligence & DS', 4, 'sneha.l@vcet.ac.in', '9842100045'),
('25EC077', 'Vikramaditya S', 'Electronics & Comm Engg', 4, 'vikram.s@vcet.ac.in', '9842100077');

-- 2. Insert Events
INSERT INTO events (event_id, event_name, category, event_date, venue, max_participants, organizer_dept, status) VALUES
('EVT101', 'National Level Hackathon 2026', 'Hackathon', '2026-08-14', 'Main Auditorium', 60, 'Information Technology', 'Completed'),
('EVT102', 'Hands-on AI & Deep Learning Workshop', 'Workshop', '2026-08-22', 'IT Lab 3 & 4', 40, 'Artificial Intelligence & DS', 'Completed'),
('EVT103', 'Cloud DevOps & Microservices Seminar', 'Seminar', '2026-09-05', 'Seminar Hall 2', 50, 'Computer Science & Engg', 'Completed'),
('EVT104', 'TECHFEST 2026 - State Level Symposium', 'Technical Symposium', '2026-09-20', 'Open Air Theatre', 100, 'Information Technology', 'Completed'),
('EVT105', 'IoT & Embedded Robotics Bootcamp', 'Workshop', '2026-10-10', 'ECE Microprocessor Lab', 35, 'Electronics & Comm Engg', 'Completed'),
('EVT106', 'VCET Cultural Fiesta - Tarang 2026', 'Cultural Fest', '2026-10-25', 'College Stadium Ground', 150, 'Student Affairs', 'Completed'),
('EVT107', 'Full-Stack Web Development Hackfest', 'Hackathon', '2026-11-28', 'Central Computing Facility', 50, 'Information Technology', 'Upcoming'),
('EVT108', 'Next-Gen Cybersecurity & Ethical Hacking', 'Workshop', '2026-12-05', 'IT Lab 1', 45, 'Information Technology', 'Upcoming');

-- 3. Insert Registrations
INSERT INTO registrations (registration_id, student_id, event_id, registration_date, status) VALUES
-- Event 101: Hackathon 2026
(1, '25IT001', 'EVT101', '2026-08-01 10:15:00', 'Registered'),
(2, '25IT006', 'EVT101', '2026-08-01 10:30:00', 'Registered'),
(3, '25IT036', 'EVT101', '2026-08-01 11:00:00', 'Registered'),
(4, '25IT066', 'EVT101', '2026-08-01 11:15:00', 'Registered'),
(5, '25IT096', 'EVT101', '2026-08-01 11:45:00', 'Registered'),
(6, '25CS012', 'EVT101', '2026-08-02 09:20:00', 'Registered'),
(7, '25CS045', 'EVT101', '2026-08-02 10:00:00', 'Registered'),
(8, '25AD010', 'EVT101', '2026-08-02 14:10:00', 'Registered'),
(9, '25AD032', 'EVT101', '2026-08-03 16:00:00', 'Registered'),
(10, '25EC015', 'EVT101', '2026-08-04 11:30:00', 'Registered'),

-- Event 102: AI Workshop
(11, '25IT001', 'EVT102', '2026-08-10 09:00:00', 'Registered'),
(12, '25IT006', 'EVT102', '2026-08-10 09:15:00', 'Registered'),
(13, '25IT036', 'EVT102', '2026-08-10 09:30:00', 'Registered'),
(14, '25AD010', 'EVT102', '2026-08-11 11:00:00', 'Registered'),
(15, '25AD032', 'EVT102', '2026-08-11 11:30:00', 'Registered'),
(16, '25AD045', 'EVT102', '2026-08-12 14:00:00', 'Registered'),
(17, '25CS045', 'EVT102', '2026-08-12 15:30:00', 'Registered'),
(18, '25CS089', 'EVT102', '2026-08-13 10:10:00', 'Registered'),

-- Event 103: Cloud Seminar
(19, '25IT066', 'EVT103', '2026-08-25 10:00:00', 'Registered'),
(20, '25IT096', 'EVT103', '2026-08-25 10:30:00', 'Registered'),
(21, '25CS012', 'EVT103', '2026-08-26 11:00:00', 'Registered'),
(22, '25CS089', 'EVT103', '2026-08-26 14:00:00', 'Registered'),
(23, '25IT028', 'EVT103', '2026-08-27 15:00:00', 'Registered'),
(24, '25EE022', 'EVT103', '2026-08-28 09:30:00', 'Registered'),

-- Event 104: TECHFEST Symposium
(25, '25IT001', 'EVT104', '2026-09-01 09:00:00', 'Registered'),
(26, '25IT006', 'EVT104', '2026-09-01 09:30:00', 'Registered'),
(27, '25IT036', 'EVT104', '2026-09-01 10:00:00', 'Registered'),
(28, '25IT066', 'EVT104', '2026-09-01 10:30:00', 'Registered'),
(29, '25IT096', 'EVT104', '2026-09-01 11:00:00', 'Registered'),
(30, '25CS012', 'EVT104', '2026-09-02 11:30:00', 'Registered'),
(31, '25CS045', 'EVT104', '2026-09-02 12:00:00', 'Registered'),
(32, '25EC015', 'EVT104', '2026-09-03 14:00:00', 'Registered'),
(33, '25EC052', 'EVT104', '2026-09-03 14:30:00', 'Registered'),
(34, '25AD010', 'EVT104', '2026-09-04 15:00:00', 'Registered'),
(35, '25ME018', 'EVT104', '2026-09-05 16:00:00', 'Registered'),
(36, '25CE009', 'EVT104', '2026-09-05 16:30:00', 'Registered'),

-- Event 105: IoT Bootcamp
(37, '25EC015', 'EVT105', '2026-09-25 10:00:00', 'Registered'),
(38, '25EC052', 'EVT105', '2026-09-25 10:30:00', 'Registered'),
(39, '25EC077', 'EVT105', '2026-09-26 11:00:00', 'Registered'),
(40, '25EE022', 'EVT105', '2026-09-26 11:30:00', 'Registered'),
(41, '25IT006', 'EVT105', '2026-09-27 14:00:00', 'Registered'),
(42, '25CS089', 'EVT105', '2026-09-27 15:00:00', 'Registered'),

-- Event 106: Cultural Fest
(43, '25IT001', 'EVT106', '2026-10-15 09:00:00', 'Registered'),
(44, '25IT036', 'EVT106', '2026-10-15 09:30:00', 'Registered'),
(45, '25CS045', 'EVT106', '2026-10-15 10:00:00', 'Registered'),
(46, '25EC015', 'EVT106', '2026-10-16 11:00:00', 'Registered'),
(47, '25ME018', 'EVT106', '2026-10-16 12:00:00', 'Registered'),
(48, '25CE009', 'EVT106', '2026-10-16 14:00:00', 'Registered'),
(49, '25AD032', 'EVT106', '2026-10-17 15:00:00', 'Registered'),
(50, '25IT015', 'EVT106', '2026-10-17 16:00:00', 'Registered');

-- 4. Insert Attendance Logs
INSERT INTO attendance (registration_id, attendance_status, checkin_time, certificate_status, remarks) VALUES
-- Event 101 Attendance
(1, 'Present', '2026-08-14 08:45:00', 'Issued', 'Active participant, 1st prize winner'),
(2, 'Present', '2026-08-14 08:50:00', 'Issued', 'Team leader, runner-up'),
(3, 'Present', '2026-08-14 08:55:00', 'Issued', 'Full-day attendance verified'),
(4, 'Present', '2026-08-14 09:00:00', 'Issued', 'Full-day attendance verified'),
(5, 'Present', '2026-08-14 09:05:00', 'Issued', 'Special jury mention'),
(6, 'Absent', NULL, 'Not Eligible', 'Did not report at check-in'),
(7, 'Present', '2026-08-14 09:12:00', 'Issued', 'Full-day attendance verified'),
(8, 'Present', '2026-08-14 09:15:00', 'Issued', 'Best AI UI demo'),
(9, 'Present', '2026-08-14 09:20:00', 'Issued', 'Full-day attendance verified'),
(10, 'Absent', NULL, 'Not Eligible', 'Medical leave informed'),

-- Event 102 Attendance
(11, 'Present', '2026-08-22 08:50:00', 'Issued', 'Completed all lab assignments'),
(12, 'Present', '2026-08-22 08:55:00', 'Issued', 'Completed model training task'),
(13, 'Present', '2026-08-22 09:00:00', 'Issued', 'Outstanding hands-on score'),
(14, 'Present', '2026-08-22 09:05:00', 'Issued', 'Lab task completed'),
(15, 'Present', '2026-08-22 09:10:00', 'Issued', 'Lab task completed'),
(16, 'Present', '2026-08-22 09:12:00', 'Issued', 'Lab task completed'),
(17, 'Absent', NULL, 'Not Eligible', 'No show on session day'),
(18, 'Present', '2026-08-22 09:20:00', 'Issued', 'Lab task completed'),

-- Event 103 Attendance
(19, 'Present', '2026-09-05 09:10:00', 'Issued', 'Attended keynote and Q&A'),
(20, 'Present', '2026-09-05 09:15:00', 'Issued', 'Attended keynote and Q&A'),
(21, 'Absent', NULL, 'Not Eligible', 'Clash with department meeting'),
(22, 'Present', '2026-09-05 09:20:00', 'Issued', 'Attended keynote and Q&A'),
(23, 'Present', '2026-09-05 09:25:00', 'Issued', 'Attended keynote and Q&A'),
(24, 'Present', '2026-09-05 09:30:00', 'Issued', 'Attended keynote and Q&A'),

-- Event 104 Attendance
(25, 'Present', '2026-09-20 08:40:00', 'Issued', 'Symposium paper presentation'),
(26, 'Present', '2026-09-20 08:45:00', 'Issued', 'Coding challenge winner'),
(27, 'Present', '2026-09-20 08:50:00', 'Issued', 'Web design event'),
(28, 'Present', '2026-09-20 08:55:00', 'Issued', 'Technical quiz finalist'),
(29, 'Present', '2026-09-20 09:00:00', 'Issued', 'Paper presentation runner up'),
(30, 'Present', '2026-09-20 09:05:00', 'Issued', 'General participant'),
(31, 'Absent', NULL, 'Not Eligible', 'Absent'),
(32, 'Present', '2026-09-20 09:10:00', 'Issued', 'Robo race winner'),
(33, 'Present', '2026-09-20 09:15:00', 'Issued', 'Circuit debugging event'),
(34, 'Present', '2026-09-20 09:20:00', 'Issued', 'AI poster presentation'),
(35, 'Present', '2026-09-20 09:25:00', 'Issued', 'CAD modeling event'),
(36, 'Absent', NULL, 'Not Eligible', 'Absent'),

-- Event 105 Attendance
(37, 'Present', '2026-10-10 09:00:00', 'Issued', 'Hardware kit completed'),
(38, 'Present', '2026-10-10 09:05:00', 'Issued', 'Sensors interface demo'),
(39, 'Present', '2026-10-10 09:10:00', 'Issued', 'NodeMCU setup completed'),
(40, 'Absent', NULL, 'Not Eligible', 'Absent'),
(41, 'Present', '2026-10-10 09:20:00', 'Issued', 'Cross-dept IoT participant'),
(42, 'Present', '2026-10-10 09:25:00', 'Issued', 'MQTT cloud connection task'),

-- Event 106 Attendance
(43, 'Present', '2026-10-25 09:30:00', 'Issued', 'Music band participant'),
(44, 'Present', '2026-10-25 09:35:00', 'Issued', 'Classical dance performance'),
(45, 'Present', '2026-10-25 09:40:00', 'Issued', 'Dramatics club lead'),
(46, 'Present', '2026-10-25 09:45:00', 'Issued', 'Photography exhibition'),
(47, 'Absent', NULL, 'Not Eligible', 'Absent'),
(48, 'Present', '2026-10-25 09:55:00', 'Issued', 'Art and craft display'),
(49, 'Present', '2026-10-25 10:00:00', 'Issued', 'Mime show winner'),
(50, 'Present', '2026-10-25 10:05:00', 'Issued', 'Anchoring committee member');

-- 5. Insert Feedback
INSERT INTO event_feedback (registration_id, rating, comments) VALUES
(1, 5, 'Exceptional problem statements and smooth platform evaluation!'),
(2, 5, 'Great hackathon atmosphere, highly encouraging faculty coordinators.'),
(3, 4, 'Very well organized. Better internet bandwidth recommended for cloud APIs.'),
(11, 5, 'Practical training on deep learning models was extremely illuminating.'),
(12, 4, 'Trainer explained mathematical intuition of backprop very clearly.'),
(13, 5, 'Superb lab session with GPU notebook access.'),
(19, 4, 'Industry insights in Kubernetes and cloud infra were top notch.'),
(25, 5, 'TECHFEST symposium had strong competition and good jury panels.'),
(26, 5, 'Loved the coding round challenges.'),
(37, 5, 'Hands-on sensors kit helped understand IoT prototyping thoroughly.'),
(43, 5, 'Thrilling performances and energetic audience!'),
(44, 5, 'Wonderful stage arrangements and sound system.');
