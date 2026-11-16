package com.vcet.events.model;

import java.sql.Timestamp;

/**
 * Model class tracking attendance status, check-in timestamps, and certificate eligibility.
 */
public class AttendanceRecord {
    private int attendanceId;
    private int registrationId;
    private String attendanceStatus; // 'Present', 'Absent'
    private Timestamp checkinTime;
    private String certificateStatus; // 'Pending', 'Issued', 'Not Eligible'
    private String remarks;

    public AttendanceRecord(int attendanceId, int registrationId, String attendanceStatus, Timestamp checkinTime, String certificateStatus, String remarks) {
        this.attendanceId = attendanceId;
        this.registrationId = registrationId;
        this.attendanceStatus = attendanceStatus;
        this.checkinTime = checkinTime;
        this.certificateStatus = certificateStatus;
        this.remarks = remarks;
    }

    public int getAttendanceId() {
        return attendanceId;
    }

    public int getRegistrationId() {
        return registrationId;
    }

    public String getAttendanceStatus() {
        return attendanceStatus;
    }

    public void setAttendanceStatus(String attendanceStatus) {
        this.attendanceStatus = attendanceStatus;
    }

    public Timestamp getCheckinTime() {
        return checkinTime;
    }

    public void setCheckinTime(Timestamp checkinTime) {
        this.checkinTime = checkinTime;
    }

    public String getCertificateStatus() {
        return certificateStatus;
    }

    public void setCertificateStatus(String certificateStatus) {
        this.certificateStatus = certificateStatus;
    }

    public String getRemarks() {
        return remarks;
    }

    public void setRemarks(String remarks) {
        this.remarks = remarks;
    }

    @Override
    public String toString() {
        return String.format("Att #%-3d | Reg #%-3d | Status: %-7s | CheckIn: %-19s | Certificate: %-12s | %s",
                attendanceId, registrationId, attendanceStatus, (checkinTime != null ? checkinTime.toString() : "N/A"), certificateStatus, (remarks != null ? remarks : ""));
    }
}
