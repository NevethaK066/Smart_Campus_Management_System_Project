package com.vcet.events.exception;

/**
 * Custom Exception thrown when a student attempts to register for an event
 * for which they are already enrolled (Functional Requirement 3).
 */
public class DuplicateRegistrationException extends Exception {
    private static final long serialVersionUID = 1L;
    private final String studentId;
    private final String eventId;

    public DuplicateRegistrationException(String studentId, String eventId) {
        super(String.format("Duplicate Registration Rejected: Student '%s' is already registered for Event '%s'!", studentId, eventId));
        this.studentId = studentId;
        this.eventId = eventId;
    }

    public String getStudentId() {
        return studentId;
    }

    public String getEventId() {
        return eventId;
    }
}
