package com.vcet.events.model;

import java.sql.Timestamp;

/**
 * Model class binding a Student to an Event registration.
 */
public class Registration {
    private int registrationId;
    private String studentId;
    private String eventId;
    private Timestamp registrationDate;
    private String status;

    // Optional navigation fields
    private String studentName;
    private String eventName;
    private String department;
    private String attendanceStatus;

    public Registration(int registrationId, String studentId, String eventId, Timestamp registrationDate, String status) {
        this.registrationId = registrationId;
        this.studentId = studentId;
        this.eventId = eventId;
        this.registrationDate = registrationDate;
        this.status = status;
    }

    public int getRegistrationId() {
        return registrationId;
    }

    public String getStudentId() {
        return studentId;
    }

    public String getEventId() {
        return eventId;
    }

    public Timestamp getRegistrationDate() {
        return registrationDate;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getStudentName() {
        return studentName;
    }

    public void setStudentName(String studentName) {
        this.studentName = studentName;
    }

    public String getEventName() {
        return eventName;
    }

    public void setEventName(String eventName) {
        this.eventName = eventName;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public String getAttendanceStatus() {
        return attendanceStatus;
    }

    public void setAttendanceStatus(String attendanceStatus) {
        this.attendanceStatus = attendanceStatus;
    }

    @Override
    public String toString() {
        return String.format("Reg #%-3d | Student: %-9s (%-15s) | Event: %-7s | Date: %s | Status: %s",
                registrationId, studentId, (studentName != null ? studentName : ""), eventId, registrationDate, status);
    }
}
