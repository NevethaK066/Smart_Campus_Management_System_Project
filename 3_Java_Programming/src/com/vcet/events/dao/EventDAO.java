package com.vcet.events.dao;

import com.vcet.events.model.Event;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/**
 * Data Access Object for Event entity.
 */
public class EventDAO {

    public boolean addEvent(Event event) throws SQLException {
        String sql = "INSERT INTO events (event_id, event_name, category, event_date, venue, max_participants, organizer_dept, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, event.getEventId());
            ps.setString(2, event.getEventName());
            ps.setString(3, event.getCategory());
            ps.setString(4, event.getEventDate());
            ps.setString(5, event.getVenue());
            ps.setInt(6, event.getMaxParticipants());
            ps.setString(7, event.getOrganizerDept());
            ps.setString(8, event.getStatus());
            return ps.executeUpdate() > 0;
        }
    }

    public Optional<Event> findById(String eventId) throws SQLException {
        String sql = "SELECT * FROM events WHERE event_id = ?";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, eventId);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    return Optional.of(mapResultSetToEvent(rs));
                }
            }
        }
        return Optional.empty();
    }

    public List<Event> findAll() throws SQLException {
        List<Event> events = new ArrayList<>();
        String sql = "SELECT * FROM events ORDER BY event_date ASC";
        try (Connection conn = DatabaseConnection.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                events.add(mapResultSetToEvent(rs));
            }
        }
        return events;
    }

    public int getRegistrationCount(String eventId) throws SQLException {
        String sql = "SELECT COUNT(*) FROM registrations WHERE event_id = ? AND status = 'Registered'";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, eventId);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    return rs.getInt(1);
                }
            }
        }
        return 0;
    }

    private Event mapResultSetToEvent(ResultSet rs) throws SQLException {
        return new Event(
                rs.getString("event_id"),
                rs.getString("event_name"),
                rs.getString("category"),
                rs.getString("event_date"),
                rs.getString("venue"),
                rs.getInt("max_participants"),
                rs.getString("organizer_dept"),
                rs.getString("status")
        );
    }
}
