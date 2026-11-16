package com.vcet.events.dao;

import com.vcet.events.model.AttendanceRecord;
import com.vcet.events.model.Registration;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

/**
 * Data Access Object managing Registrations and Attendance logs.
 */
public class RegistrationDAO {

    public boolean isAlreadyRegistered(String studentId, String eventId) throws SQLException {
        String sql = "SELECT COUNT(*) FROM registrations WHERE student_id = ? AND event_id = ?";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, studentId);
            ps.setString(2, eventId);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    return rs.getInt(1) > 0;
                }
            }
        }
        return false;
    }

    public int registerStudent(String studentId, String eventId) throws SQLException {
        String sql = "INSERT INTO registrations (student_id, event_id, status) VALUES (?, ?, 'Registered')";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {
            ps.setString(1, studentId);
            ps.setString(2, eventId);
            ps.executeUpdate();
            try (ResultSet rs = ps.getGeneratedKeys()) {
                if (rs.next()) {
                    return rs.getInt(1);
                }
            }
        }
        return -1;
    }

    public List<Registration> findByEvent(String eventId) throws SQLException {
        List<Registration> list = new ArrayList<>();
        String sql = "SELECT r.registration_id, r.student_id, r.event_id, r.registration_date, r.status, " +
                     "s.name AS student_name, s.department, e.event_name, a.attendance_status " +
                     "FROM registrations r " +
                     "JOIN students s ON r.student_id = s.student_id " +
                     "JOIN events e ON r.event_id = e.event_id " +
                     "LEFT JOIN attendance a ON r.registration_id = a.registration_id " +
                     "WHERE r.event_id = ? " +
                     "ORDER BY r.registration_id ASC";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, eventId);
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    Registration reg = new Registration(
                            rs.getInt("registration_id"),
                            rs.getString("student_id"),
                            rs.getString("event_id"),
                            rs.getTimestamp("registration_date"),
                            rs.getString("status")
                    );
                    reg.setStudentName(rs.getString("student_name"));
                    reg.setDepartment(rs.getString("department"));
                    reg.setEventName(rs.getString("event_name"));
                    reg.setAttendanceStatus(rs.getString("attendance_status"));
                    list.add(reg);
                }
            }
        }
        return list;
    }

    public boolean recordAttendance(int registrationId, String attendanceStatus, String remarks) throws SQLException {
        String checkSql = "SELECT attendance_id FROM attendance WHERE registration_id = ?";
        String certStatus = attendanceStatus.equalsIgnoreCase("Present") ? "Issued" : "Not Eligible";
        Timestamp now = attendanceStatus.equalsIgnoreCase("Present") ? new Timestamp(System.currentTimeMillis()) : null;

        try (Connection conn = DatabaseConnection.getConnection()) {
            boolean exists = false;
            try (PreparedStatement checkPs = conn.prepareStatement(checkSql)) {
                checkPs.setInt(1, registrationId);
                try (ResultSet rs = checkPs.executeQuery()) {
                    exists = rs.next();
                }
            }

            if (exists) {
                String updateSql = "UPDATE attendance SET attendance_status = ?, checkin_time = ?, certificate_status = ?, remarks = ? WHERE registration_id = ?";
                try (PreparedStatement ps = conn.prepareStatement(updateSql)) {
                    ps.setString(1, attendanceStatus);
                    ps.setTimestamp(2, now);
                    ps.setString(3, certStatus);
                    ps.setString(4, remarks);
                    ps.setInt(5, registrationId);
                    return ps.executeUpdate() > 0;
                }
            } else {
                String insertSql = "INSERT INTO attendance (registration_id, attendance_status, checkin_time, certificate_status, remarks) VALUES (?, ?, ?, ?, ?)";
                try (PreparedStatement ps = conn.prepareStatement(insertSql)) {
                    ps.setInt(1, registrationId);
                    ps.setString(2, attendanceStatus);
                    ps.setTimestamp(3, now);
                    ps.setString(4, certStatus);
                    ps.setString(5, remarks);
                    return ps.executeUpdate() > 0;
                }
            }
        }
    }

    public List<AttendanceRecord> findAllAttendance() throws SQLException {
        List<AttendanceRecord> list = new ArrayList<>();
        String sql = "SELECT * FROM attendance ORDER BY attendance_id ASC";
        try (Connection conn = DatabaseConnection.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                list.add(new AttendanceRecord(
                        rs.getInt("attendance_id"),
                        rs.getInt("registration_id"),
                        rs.getString("attendance_status"),
                        rs.getTimestamp("checkin_time"),
                        rs.getString("certificate_status"),
                        rs.getString("remarks")
                ));
            }
        }
        return list;
    }
}
