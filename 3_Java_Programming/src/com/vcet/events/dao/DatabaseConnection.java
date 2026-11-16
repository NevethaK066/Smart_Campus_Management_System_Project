package com.vcet.events.dao;

import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * Singleton database connection manager handling SQLite JDBC connectivity.
 */
public class DatabaseConnection {
    private static Connection connection = null;

    private DatabaseConnection() {
    }

    public static synchronized Connection getConnection() throws SQLException {
        if (connection == null || connection.isClosed()) {
            try {
                Class.forName("org.sqlite.JDBC");
            } catch (ClassNotFoundException e) {
                System.err.println("[WARN] org.sqlite.JDBC driver class not found in classpath.");
            }

            // Check potential database file paths
            String[] candidatePaths = new String[]{
                "smart_campus.db",
                "../smart_campus.db",
                "2_Database_Management_System/smart_campus.db",
                "../2_Database_Management_System/smart_campus.db"
            };
            
            String dbPath = "2_Database_Management_System/smart_campus.db";
            for (String p : candidatePaths) {
                File f = new File(p);
                if (f.exists()) {
                    dbPath = f.getAbsolutePath();
                    break;
                }
            }

            String url = "jdbc:sqlite:" + dbPath;
            connection = DriverManager.getConnection(url);
            
            // Enable foreign keys
            try (Statement stmt = connection.createStatement()) {
                stmt.execute("PRAGMA foreign_keys = ON;");
            }
        }
        return connection;
    }

    public static synchronized void closeConnection() {
        if (connection != null) {
            try {
                connection.close();
            } catch (SQLException ignored) {
            }
            connection = null;
        }
    }
}
