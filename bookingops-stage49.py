# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: BookingOps
import unittest
from datetime import date

class TestBookingOpsEdgeCases(unittest.TestCase):
    def setUp(self):
        self.bo = BookingOps()

    def test_update_nonexistent_resource_raises(self):
        with self.assertRaises(ValueError):
            self.bo.update_resource("nonexistent", 10)

    def test_delete_nonexistent_reservation_raises(self):
        with self.assertRaises(KeyError):
            self.bo.delete_reservation("nonexistent")

    def test_update_with_empty_details_ignores_invalid_keys(self):
        res = Resource(name="R1", capacity=5, start=date(2024, 6, 1), end=date(2024, 6, 3))
        self.bo.resources["R1"] = res
        res.details = {}
        updated = self.bo.update_resource("R1", details=res.details)
        self.assertEqual(updated.capacity, 5)

    def test_delete_with_no_reservations_returns_empty(self):
        result = self.bo.delete_reservation("any")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
