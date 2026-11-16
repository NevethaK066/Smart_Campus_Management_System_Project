package com.vcet.events.model;

import java.sql.Timestamp;

/**
 * Model class representing a Student profile.
 * Incorporates Encapsulation, Validation, and String Formatting.
 */
public class Student {
    private String studentId;
    private String name;
    private String department;
    private int yearOfStudy;
    private String email;
    private String phone;
    private Timestamp createdAt;

    public Student(String studentId, String name, String department, int yearOfStudy, String email, String phone) {
        this.studentId = studentId;
        this.name = name;
        this.department = department;
        this.yearOfStudy = yearOfStudy;
        this.email = email;
        this.phone = phone;
    }

    public Student(String studentId, String name, String department, int yearOfStudy, String email, String phone, Timestamp createdAt) {
        this(studentId, name, department, yearOfStudy, email, phone);
        this.createdAt = createdAt;
    }

    public String getStudentId() {
        return studentId;
    }

    public void setStudentId(String studentId) {
        this.studentId = studentId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public int getYearOfStudy() {
        return yearOfStudy;
    }

    public void setYearOfStudy(int yearOfStudy) {
        this.yearOfStudy = yearOfStudy;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public Timestamp getCreatedAt() {
        return createdAt;
    }

    @Override
    public String toString() {
        return String.format("[%s] %-18s | Dept: %-26s | Year: %d | Email: %s",
                studentId, name, department, yearOfStudy, email);
    }
}
