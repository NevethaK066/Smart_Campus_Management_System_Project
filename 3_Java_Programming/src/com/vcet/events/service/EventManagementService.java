package com.vcet.events.service;

import com.vcet.events.dao.EventDAO;
import com.vcet.events.dao.RegistrationDAO;
import com.vcet.events.dao.StudentDAO;
import com.vcet.events.exception.DuplicateRegistrationException;
import com.vcet.events.exception.EventCapacityExceededException;
import com.vcet.events.exception.RecordNotFoundException;
import com.vcet.events.model.Event;
import com.vcet.events.model.Registration;
import com.vcet.events.model.Student;

import java.sql.SQLException;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

/**
 * Core Service Layer orchestrating event workflows, business logic,
 * Stream API filtering/mapping, and duplicate registration enforcement.
 */
public class EventManagementService implements IEventService {
    private final StudentDAO studentDAO;
    private final EventDAO eventDAO;
    private final RegistrationDAO registrationDAO;

    public EventManagementService() {
        this.studentDAO = new StudentDAO();
        this.eventDAO = new EventDAO();
        this.registrationDAO = new RegistrationDAO();
    }

    public EventManagementService(StudentDAO studentDAO, EventDAO eventDAO, RegistrationDAO registrationDAO) {
        this.studentDAO = studentDAO;
        this.eventDAO = eventDAO;
        this.registrationDAO = registrationDAO;
    }

    @Override
    public void registerStudent(Student student) throws SQLException {
        studentDAO.addStudent(student);
    }

    @Override
    public void addEvent(Event event) throws SQLException {
        eventDAO.addEvent(event);
    }

    @Override
    public int registerForEvent(String studentId, String eventId)
            throws SQLException, DuplicateRegistrationException, EventCapacityExceededException, RecordNotFoundException {
        
        // 1. Verify Student exists
        Optional<Student> studentOpt = studentDAO.findById(studentId);
        if (studentOpt.isEmpty()) {
            throw new RecordNotFoundException("Student ID '" + studentId + "' not registered in campus database!");
        }

        // 2. Verify Event exists
        Optional<Event> eventOpt = eventDAO.findById(eventId);
        if (eventOpt.isEmpty()) {
            throw new RecordNotFoundException("Event ID '" + eventId + "' does not exist!");
        }
        Event event = eventOpt.get();

        // 3. Check for Duplicate Registration (Functional Requirement 3)
        if (registrationDAO.isAlreadyRegistered(studentId, eventId)) {
            throw new DuplicateRegistrationException(studentId, eventId);
        }

        // 4. Check Event Capacity (Functional Requirement 2)
        int currentCount = eventDAO.getRegistrationCount(eventId);
        if (currentCount >= event.getMaxParticipants()) {
            throw new EventCapacityExceededException(eventId, event.getMaxParticipants());
        }

        // 5. Proceed with Registration
        int regId = registrationDAO.registerStudent(studentId, eventId);
        
        // 6. Trigger Asynchronous Notification Thread (Multithreading)
        NotificationService.sendAsyncRegistrationNotification(studentId, studentOpt.get().getEmail(), event.getEventName(), regId);

        return regId;
    }

    @Override
    public void recordAttendance(int registrationId, String status, String remarks)
            throws SQLException, RecordNotFoundException {
        boolean updated = registrationDAO.recordAttendance(registrationId, status, remarks);
        if (!updated) {
            throw new RecordNotFoundException("Registration ID #" + registrationId + " not found!");
        }
    }

    @Override
    public List<Registration> getParticipantsByEvent(String eventId) throws SQLException {
        return registrationDAO.findByEvent(eventId);
    }

    @Override
    public void displayEventReport(String eventId) throws SQLException {
        Optional<Event> eventOpt = eventDAO.findById(eventId);
        if (eventOpt.isEmpty()) {
            System.out.println("[ERROR] Event not found: " + eventId);
            return;
        }

        Event e = eventOpt.get();
        List<Registration> participants = registrationDAO.findByEvent(eventId);

        // Using Java Streams API for aggregation and filtering (Unit 5)
        long totalRegistered = participants.size();
        long presentCount = participants.stream()
                .filter(p -> "Present".equalsIgnoreCase(p.getAttendanceStatus()))
                .count();
        long absentCount = participants.stream()
                .filter(p -> "Absent".equalsIgnoreCase(p.getAttendanceStatus()))
                .count();

        double attendanceRate = totalRegistered > 0 ? ((double) presentCount / totalRegistered) * 100.0 : 0.0;

        StringBuilder sb = new StringBuilder();
        sb.append("\n========================================================================================\n");
        sb.append(String.format(" EVENT REPORT: [%s] %s\n", e.getEventId(), e.getEventName().toUpperCase()));
        sb.append("========================================================================================\n");
        sb.append(String.format(" Category: %-20s | Date: %-12s | Venue: %s\n", e.getCategory(), e.getEventDate(), e.getVenue()));
        sb.append(String.format(" Max Capacity: %-16d | Total Registered: %-8d | Attendance Rate: %.1f%%\n",
                e.getMaxParticipants(), totalRegistered, attendanceRate));
        sb.append(String.format(" Status Summary: Present: %d | Absent: %d | Unrecorded: %d\n",
                presentCount, absentCount, (totalRegistered - presentCount - absentCount)));
        sb.append("----------------------------------------------------------------------------------------\n");
        sb.append(String.format(" %-6s | %-10s | %-20s | %-26s | %-10s\n", "Reg ID", "Student ID", "Student Name", "Department", "Attendance"));
        sb.append("----------------------------------------------------------------------------------------\n");

        participants.forEach(p -> {
            sb.append(String.format(" #%-5d | %-10s | %-20s | %-26s | %-10s\n",
                    p.getRegistrationId(),
                    p.getStudentId(),
                    p.getStudentName(),
                    p.getDepartment(),
                    (p.getAttendanceStatus() != null ? p.getAttendanceStatus() : "Pending")));
        });
        sb.append("========================================================================================\n");

        System.out.println(sb);
    }

    @Override
    public Map<String, Long> getDepartmentRegistrationSummary() throws SQLException {
        List<Student> students = studentDAO.findAll();
        // Stream Collectors groupingBy
        return students.stream()
                .collect(Collectors.groupingBy(Student::getDepartment, Collectors.counting()));
    }

    public List<Student> getAllStudents() throws SQLException {
        return studentDAO.findAll();
    }

    public List<Event> getAllEvents() throws SQLException {
        return eventDAO.findAll();
    }
}
