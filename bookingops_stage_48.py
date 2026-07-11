# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: BookingOps
import pytest
from bookingops.models import Resource, Reservation, Conflict, Customer


class TestResourceCreation:
    def test_resource_creation(self):
        r = Resource(name="Room A", capacity=50)
        assert r.name == "Room A"
        assert r.capacity == 50

    def test_invalid_capacity_raises(self):
        with pytest.raises(ValueError):
            Resource(name="Bad Room", capacity=-1)


class TestReservationValidation:
    def test_valid_reservation(self):
        res = Reservation(resource_id=1, start_time="2024-01-01 09:00", end_time="2024-01-01 10:00")
        assert not res.conflicts

    def test_overlapping_reservations(self):
        r = Resource(name="Room X", capacity=30)
        r.add_reservation(Reservation(resource_id=r.id, start_time="2024-01-01 09:00", end_time="2024-01-01 10:00"))
        r.add_reservation(Reservation(resource_id=r.id, start_time="2024-01-01 09:30", end_time="2024-01-01 10:30"))
        assert len(r.reservations) == 2


class TestCustomerAndConflict:
    def test_customer_creation(self):
        c = Customer(name="Alice")
        assert c.name == "Alice"

    def test_conflict_generation(self):
        res1 = Reservation(resource_id=1, start_time="2024-06-01 09:00", end_time="2024-06-01 10:00")
        res2 = Reservation(resource_id=1, start_time="2024-06-01 09:30", end_time="2024-06-01 10:30")
        conflict = Conflict(reservations=[res1, res2])
        assert len(conflict.reservations) == 2
