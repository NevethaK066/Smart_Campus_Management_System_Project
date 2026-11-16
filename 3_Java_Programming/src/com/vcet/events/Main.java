package com.vcet.events;

import com.vcet.events.exception.DuplicateRegistrationException;
import com.vcet.events.exception.EventCapacityExceededException;
import com.vcet.events.exception.RecordNotFoundException;
import com.vcet.events.model.Event;
import com.vcet.events.model.Student;
import com.vcet.events.service.EventManagementService;
import com.vcet.events.test.TestCaseRunner;

import java.sql.SQLException;
import java.util.List;
import java.util.Scanner;

/**
 * Main Interactive Application for Smart Campus Event Management System.
 * Supports complete interactive keyboard input for manual testing.
 */
public class Main {
    private static final EventManagementService service = new EventManagementService();
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        if (args.length > 0 && args[0].equalsIgnoreCase("--test")) {
            TestCaseRunner.main(args);
            return;
        }

        printBanner();
        boolean running = true;

        while (running) {
            printMenu();
            System.out.print("Select an option (1-9): ");
            String choice = scanner.nextLine().trim();

            switch (choice) {
                case "1" -> viewAllEvents();
                case "2" -> viewAllStudents();
                case "3" -> addNewStudent();
                case "4" -> addNewEvent();
                case "5" -> registerStudentForEvent();
                case "6" -> recordAttendance();
                case "7" -> viewEventReport();
                case "8" -> {
                    System.out.println("\n--- Invoking Automated Test Suite ---");
                    TestCaseRunner.main(new String[]{});
                }
                case "9" -> {
                    System.out.println("\nExiting Smart Campus Event Management System. Thank you!");
                    running = false;
                }
                default -> System.out.println("[WARN] Invalid option. Please enter a number between 1 and 9.");
            }
        }
    }

    private static void printBanner() {
        System.out.println("==========================================================================================");
        System.out.println(" VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY (AUTONOMOUS), ERODE - 12");
        System.out.println(" DEPARTMENT OF INFORMATION TECHNOLOGY | CLASS: 25IT3A&B | AY: 2026-27 (ODD)");
        System.out.println(" Scenario 6: Smart Campus Event Management & Student Participation Analysis System");
        System.out.println("==========================================================================================");
    }

    private static void printMenu() {
        System.out.println("\n----------------------------- INTERACTIVE CAMPUS PORTAL -----------------------------");
        System.out.println("  1. View All Campus Events (FR2)");
        System.out.println("  2. View All Student Profiles (FR1)");
        System.out.println("  3. [MANUAL INPUT] Add New Student Profile (FR1)");
        System.out.println("  4. [MANUAL INPUT] Add New Campus Event (FR2)");
        System.out.println("  5. [MANUAL INPUT] Register Student for Event [Duplicate Prevention] (FR3)");
        System.out.println("  6. [MANUAL INPUT] Record Student Attendance & Participation Status (FR4)");
        System.out.println("  7. [MANUAL INPUT] Display Registered Participants & Event-wise Report (FR5)");
        System.out.println("  8. Run Automated Test Suite (All 6 Test Cases)");
        System.out.println("  9. Exit Application");
        System.out.println("------------------------------------------------------------------------------------");
    }

    private static void viewAllEvents() {
        try {
            List<Event> events = service.getAllEvents();
            System.out.println("\n=== CAMPUS EVENTS SCHEDULE ===");
            for (Event e : events) {
                System.out.println(e);
            }
        } catch (SQLException e) {
            System.err.println("[ERROR] Failed to retrieve events: " + e.getMessage());
        }
    }

    private static void viewAllStudents() {
        try {
            List<Student> students = service.getAllStudents();
            System.out.println("\n=== REGISTERED STUDENT PROFILES ===");
            for (Student s : students) {
                System.out.println(s);
            }
        } catch (SQLException e) {
            System.err.println("[ERROR] Failed to retrieve students: " + e.getMessage());
        }
    }

    private static void addNewStudent() {
        String id = "";
        try {
            System.out.println("\n--- ADD NEW STUDENT PROFILE ---");
            System.out.print("Enter Student Roll No (e.g., 25IT150): ");
            id = scanner.nextLine().trim();
            System.out.print("Enter Student Full Name: ");
            String name = scanner.nextLine().trim();
            System.out.print("Enter Department (e.g., Information Technology): ");
            String dept = scanner.nextLine().trim();
            System.out.print("Enter Year of Study (1-4): ");
            int year = Integer.parseInt(scanner.nextLine().trim());
            System.out.print("Enter College Email (e.g., student@vcet.ac.in): ");
            String email = scanner.nextLine().trim();
            System.out.print("Enter Phone Number: ");
            String phone = scanner.nextLine().trim();

            Student s = new Student(id, name, dept, year, email, phone);
            service.registerStudent(s);
            System.out.println("[SUCCESS] Student profile for '" + name + "' added successfully!");
        } catch (NumberFormatException e) {
            System.err.println("[ERROR] Invalid year format. Please enter a valid number (1-4).");
        } catch (SQLException e) {
            if (e.getMessage().contains("PRIMARY KEY") || e.getMessage().contains("UNIQUE constraint failed: students.student_id")) {
                System.err.println("\n[ERROR - DUPLICATE STUDENT ID]");
                System.err.println("  Student Roll Number '" + id + "' is ALREADY registered in the system!");
                System.err.println("  Each student must have a unique Roll Number. Please try again with a new ID (e.g., 25IT150).");
            } else if (e.getMessage().contains("UNIQUE constraint failed: students.email")) {
                System.err.println("\n[ERROR - DUPLICATE EMAIL]");
                System.err.println("  The email address is already associated with another student account.");
            } else {
                System.err.println("[ERROR] Database Error: " + e.getMessage());
            }
        }
    }

    private static void addNewEvent() {
        try {
            System.out.println("\n--- ADD NEW CAMPUS EVENT ---");
            System.out.print("Enter Event ID (e.g., EVT201): ");
            String id = scanner.nextLine().trim();
            System.out.print("Enter Event Title: ");
            String name = scanner.nextLine().trim();
            System.out.print("Enter Category (Workshop, Hackathon, Seminar, Technical Symposium, Cultural Fest): ");
            String category = scanner.nextLine().trim();
            System.out.print("Enter Event Date (YYYY-MM-DD): ");
            String date = scanner.nextLine().trim();
            System.out.print("Enter Venue (e.g., IT Lab 2, Main Auditorium): ");
            String venue = scanner.nextLine().trim();
            System.out.print("Enter Max Participant Capacity (e.g., 50): ");
            int cap = Integer.parseInt(scanner.nextLine().trim());
            System.out.print("Enter Organizing Department (e.g., Information Technology): ");
            String orgDept = scanner.nextLine().trim();

            Event ev = new Event(id, name, category, date, venue, cap, orgDept, "Upcoming");
            service.addEvent(ev);
            System.out.println("[SUCCESS] Event '" + name + "' created and scheduled successfully!");
        } catch (NumberFormatException e) {
            System.err.println("[ERROR] Invalid capacity number.");
        } catch (SQLException e) {
            System.err.println("[ERROR] Database Error: " + e.getMessage());
        }
    }

    private static void registerStudentForEvent() {
        try {
            System.out.println("\n--- REGISTER STUDENT FOR EVENT ---");
            System.out.print("Enter Student ID (e.g., 25IT001): ");
            String studentId = scanner.nextLine().trim();
            System.out.print("Enter Event ID (e.g., EVT107): ");
            String eventId = scanner.nextLine().trim();

            int regId = service.registerForEvent(studentId, eventId);
            System.out.println("\n[SUCCESS] Registration Confirmed!");
            System.out.println("  -> Allocated Registration ID: #" + regId);
            System.out.println("  -> Enrolled Student: " + studentId + " in Event: " + eventId);
        } catch (DuplicateRegistrationException e) {
            System.err.println("\n[ERROR - DUPLICATE REGISTRATION BLOCKED]");
            System.err.println("  " + e.getMessage());
        } catch (EventCapacityExceededException e) {
            System.err.println("\n[ERROR - CAPACITY EXCEEDED]");
            System.err.println("  " + e.getMessage());
        } catch (RecordNotFoundException | SQLException e) {
            System.err.println("\n[ERROR] " + e.getMessage());
        }
    }

    private static void recordAttendance() {
        try {
            System.out.println("\n--- RECORD EVENT ATTENDANCE ---");
            System.out.print("Enter Registration ID (e.g., 1): ");
            int regId = Integer.parseInt(scanner.nextLine().trim());
            System.out.print("Attendance Status (Present / Absent): ");
            String status = scanner.nextLine().trim();
            System.out.print("Remarks (e.g., Attended Full Day, Winner, Absent): ");
            String remarks = scanner.nextLine().trim();

            service.recordAttendance(regId, status, remarks);
            System.out.println("[SUCCESS] Attendance successfully recorded in database!");
            System.out.println("  -> Status set to: " + status);
            System.out.println("  -> Certificate Status updated to: " + (status.equalsIgnoreCase("Present") ? "Issued" : "Not Eligible"));
        } catch (NumberFormatException e) {
            System.err.println("[ERROR] Invalid Registration ID number.");
        } catch (RecordNotFoundException | SQLException e) {
            System.err.println("[ERROR] " + e.getMessage());
        }
    }

    private static void viewEventReport() {
        try {
            System.out.println("\n--- VIEW EVENT REPORT ---");
            System.out.print("Enter Event ID (e.g., EVT101): ");
            String eventId = scanner.nextLine().trim();
            service.displayEventReport(eventId);
        } catch (SQLException e) {
            System.err.println("[ERROR] " + e.getMessage());
        }
    }
}
