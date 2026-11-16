package com.vcet.events.model;

/**
 * Model class representing a Campus Event.
 */
public class Event {
    private String eventId;
    private String eventName;
    private String category;
    private String eventDate;
    private String venue;
    private int maxParticipants;
    private String organizerDept;
    private String status;

    public Event(String eventId, String eventName, String category, String eventDate, String venue, int maxParticipants, String organizerDept, String status) {
        this.eventId = eventId;
        this.eventName = eventName;
        this.category = category;
        this.eventDate = eventDate;
        this.venue = venue;
        this.maxParticipants = maxParticipants;
        this.organizerDept = organizerDept;
        this.status = status;
    }

    public String getEventId() {
        return eventId;
    }

    public void setEventId(String eventId) {
        this.eventId = eventId;
    }

    public String getEventName() {
        return eventName;
    }

    public void setEventName(String eventName) {
        this.eventName = eventName;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getEventDate() {
        return eventDate;
    }

    public void setEventDate(String eventDate) {
        this.eventDate = eventDate;
    }

    public String getVenue() {
        return venue;
    }

    public void setVenue(String venue) {
        this.venue = venue;
    }

    public int getMaxParticipants() {
        return maxParticipants;
    }

    public void setMaxParticipants(int maxParticipants) {
        this.maxParticipants = maxParticipants;
    }

    public String getOrganizerDept() {
        return organizerDept;
    }

    public void setOrganizerDept(String organizerDept) {
        this.organizerDept = organizerDept;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return String.format("[%s] %-32s | %-18s | Date: %s | Venue: %-20s | Cap: %3d | Status: %s",
                eventId, eventName, category, eventDate, venue, maxParticipants, status);
    }
}
