package com.vcet.events.exception;

/**
 * Custom Exception thrown when an expected entity record cannot be located.
 */
public class RecordNotFoundException extends Exception {
    private static final long serialVersionUID = 1L;

    public RecordNotFoundException(String message) {
        super(message);
    }
}
