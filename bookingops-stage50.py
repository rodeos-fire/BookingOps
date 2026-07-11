# === Stage 50: Add unit tests for import and export behavior ===
# Project: BookingOps
import unittest
from booking_ops import BookingOps, Resource, Reservation, Customer


class TestExportImport(unittest.TestCase):
    def setUp(self):
        self.ops = BookingOps()
        res1 = Resource("RoomA", "Conference")
        res2 = Resource("RoomB", "Office")
        cust1 = Customer("Alice", "alice@example.com")
        cust2 = Customer("Bob", "bob@example.com")

        r1 = Reservation(res1, cust1, "2025-06-10 09:00", "2025-06-10 10:00", "Team Standup")
        r2 = Reservation(res2, cust2, "2025-06-11 14:00", "2025-06-11 15:30", "Client Call")

        self.ops.add_resource(r1)
        self.ops.add_resource(r2)
        self.ops.add_customer(cust1)
        self.ops.add_customer(cust2)
        self.ops.make_reservation(r1)
        self.ops.make_reservation(r2)

    def test_export_to_dict(self):
        data = self.ops.export()
        self.assertIn("resources", data)
        self.assertEqual(len(data["resources"]), 2)
        self.assertIn("customers", data)
        self.assertEqual(len(data["customers"]), 2)
        self.assertIn("reservations", data)
        self.assertEqual(len(data["reservations"]), 2)

    def test_import_from_dict(self):
        original = self.ops.export()
        new_ops = BookingOps.import_(original)

        self.assertEqual(len(new_ops.resources), 2)
        self.assertEqual(len(new_ops.customers), 2)
        self.assertEqual(len(new_ops.reservations), 2)

        res_name, res_type = list(new_ops.resources[0].items())[:2]
        self.assertEqual(res_name, "RoomA")
        self.assertEqual(res_type, "Conference")

    def test_round_trip_preserves_conflicts(self):
        """Export/import should keep conflict detection working."""
        data = self.ops.export()
        restored = BookingOps.import_(data)

        r1a, r2a = list(restored.reservations[0].items())[:2]
        r1b, r2b = list(restored.reservations[1].items())[:2]

        conflict = restored.check_conflict(r1a, r2a)
        self.assertFalse(conflict)  # different resources → no conflict


if __name__ == "__main__":
    unittest.main()
