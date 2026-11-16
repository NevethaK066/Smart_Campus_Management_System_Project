package com.vcet.events.service;

import com.vcet.events.exception.DuplicateRegistrationException;
import com.vcet.events.exception.EventCapacityExceededException;
import com.vcet.events.exception.RecordNotFoundException;
import com.vcet.events.model.Event;
import com.vcet.events.model.Registration;
import com.vcet.events.model.Student;

import java.sql.SQLException;
import java.util.List;
import java.util.Map;

/**
 * Service Layer Interface defining campus event operations (Demonstrating OOP Interface).
 */
public interface IEventService {
    void registerStudent(Student student) throws SQLException;
    void addEvent(Event event) throws SQLException;
    int registerForEvent(String studentId, String eventId) throws SQLException, DuplicateRegistrationException, EventCapacityExceededException, RecordNotFoundException;
    void recordAttendance(int registrationId, String status, String remarks) throws SQLException, RecordNotFoundException;
    List<Registration> getParticipantsByEvent(String eventId) throws SQLException;
    void displayEventReport(String eventId) throws SQLException;
    Map<String, Long> getDepartmentRegistrationSummary() throws SQLException;
}
