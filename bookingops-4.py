# === Stage 4: Implement create operations for the primary records ===
# Project: BookingOps
from typing import Optional, List
import uuid
from datetime import datetime, timedelta

class Resource:
    def __init__(self, name: str, capacity: int = 1):
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.capacity = capacity
        self.bookings: List[Reservation] = []

    def add_booking(self, reservation: Reservation) -> bool:
        if not self._check_conflict(reservation):
            self.bookings.append(reservation)
            return True
        return False

    def _check_conflict(self, new_reservation: Reservation) -> bool:
        for existing in self.bookings:
            if (new_reservation.start_time < existing.end_time and 
                new_reservation.end_time > existing.start_time):
                return True
        return False

class Customer:
    def __init__(self, name: str, email: Optional[str] = None):
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.email = email

class Reservation:
    def __init__(self, resource_id: str, customer_id: str, start_time: datetime, 
                 end_time: datetime, notes: Optional[str] = None):
        self.id = str(uuid.uuid4())[:8]
        self.resource_id = resource_id
        self.customer_id = customer_id
        self.start_time = start_time
        self.end_time = end_time
        self.notes = notes

    def __repr__(self):
        return f"Reservation({self.id}, {self.resource_id}, {self.customer_id})"
