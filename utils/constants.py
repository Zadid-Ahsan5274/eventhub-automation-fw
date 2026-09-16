"""
Central place for routes, timeouts and other static constants used
across the framework. Keeping routes here means page objects never
hardcode raw query strings.
"""

class Routes:
    HOME = "/"
    LOGIN="/login"
    REGISTER="/register"
    EVENTS="/events"
    BOOKINGS="/bookings"
    MANAGE_EVENTS="/admin/events"

class Timeouts:
    SHORT=5_000
    MEDIUM=15_000
    LONG=30_000


