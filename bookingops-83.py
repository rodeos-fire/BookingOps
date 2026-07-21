# === Stage 83: Add regression tests for the final demo workflow ===
# Project: BookingOps
import unittest


class TestDemoWorkflow(unittest.TestCase):
    """Regression tests for the final demo workflow."""

    def setUp(self):
        from bookingops.resources import Resource
        from bookingops.reservations import Reservation, BookingStatus
        self.resource = Resource("Room-A", 10)
        res1 = Reservation(BookingStatus.CONFIRMED, "Alice", [self.resource], start=9, end=10)
        res2 = Reservation(BookingStatus.CONFIRMED, "Bob",   [self.resource], start=10, end=11)
        self.reservations = [res1, res2]

    def test_no_conflicts(self):
        conflicts = Resource.findConflicts(self.resource, self.reservations)
        self.assertEqual(conflicts, [])

    def test_utilization_report(self):
        report = Resource.generateUtilizationReport(self.resource, self.reservations)
        self.assertIn("Room-A", report)
        self.assertIn("Alice", report)
        self.assertIn("Bob", report)
        self.assertEqual(report["total_slots"], 20)

    def test_add_resource_to_grid(self):
        grid = Resource.buildGrid([self.resource])
        self.assertIn(self.resource, grid)


if __name__ == "__main__":
    unittest.main()
