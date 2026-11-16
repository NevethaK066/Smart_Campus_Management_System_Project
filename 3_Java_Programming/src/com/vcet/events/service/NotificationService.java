package com.vcet.events.service;

/**
 * Multithreaded Notification Service.
 * Demonstrates Java Thread Model, Priorities, and Synchronization (Syllabus Unit 3).
 */
public class NotificationService {

    public static void sendAsyncRegistrationNotification(String studentId, String studentEmail, String eventName, int regId) {
        Thread notifyThread = new Thread(() -> {
            try {
                // Simulate asynchronous email dispatch and QR e-pass generation
                Thread.sleep(150);
                synchronized (System.out) {
                    System.out.println("  [NOTIFICATION DAEMON] E-Pass generated for Reg #" + regId + " -> Sent to " + studentEmail);
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }, "AsyncNotifier-" + regId);

        // Set thread priority
        notifyThread.setPriority(Thread.NORM_PRIORITY + 1);
        notifyThread.start();
    }
}
