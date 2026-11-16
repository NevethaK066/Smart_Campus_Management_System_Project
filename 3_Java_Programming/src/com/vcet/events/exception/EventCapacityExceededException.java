package com.vcet.events.exception;

/**
 * Custom Exception thrown when an event has reached its maximum participant capacity.
 */
public class EventCapacityExceededException extends Exception {
    private static final long serialVersionUID = 1L;

    public EventCapacityExceededException(String eventId, int maxCapacity) {
        super(String.format("Event Full: Event '%s' has reached its maximum participant limit of %d seats!", eventId, maxCapacity));
    }
}
