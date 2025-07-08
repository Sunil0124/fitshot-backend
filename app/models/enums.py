from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    TRAINER = "trainer"
    STUDENT = "student"

class AppointmentStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
