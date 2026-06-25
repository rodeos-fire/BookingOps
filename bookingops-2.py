# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: BookingOps
from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List
from enum import Enum


class ResourceStatus(Enum):
    AVAILABLE = "available"
    BUSY = "busy"
    MAINTENANCE = "maintenance"


@dataclass(frozen=True)
class Customer:
    id: str
    name: str
    email: Optional[str] = None

    def __hash__(self):
        return hash(self.id)


@dataclass
class Reservation:
    id: str
    resource_id: str
    customer: Customer
    start_date: date
    end_date: date
    status: ResourceStatus = ResourceStatus.AVAILABLE
    notes: Optional[str] = None

    def overlaps_with(self, other: "Reservation") -> bool:
        return self.start_date <= other.end_date and other.start_date <= self.end_date


@dataclass
class ConflictReport:
    reservation_a: Reservation
    reservation_b: Reservation
    conflict_type: str = "date_overlap"

    def __str__(self) -> str:
        return f"[{self.reservation_a.id}] <-> [{self.reservation_b.id}]: {self.conflict_type}"


@dataclass
class ResourceUsageReport:
    resource_id: str
    total_reservations: int = 0
    busy_days: set[date] = field(default_factory=set)

    def add_reservation(self, reservation: Reservation):
        self.total_reservations += 1
        if reservation.status == ResourceStatus.BUSY:
            self.busy_days.add(reservation.start_date)
