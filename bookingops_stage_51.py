# === Stage 51: Add unit tests for search and filter behavior ===
# Project: BookingOps
import unittest
from bookingops import BookingOps, Resource, Reservation

class TestSearchAndFilter(unittest.TestCase):
    def setUp(self):
        self.ops = BookingOps()
        res_a = Resource("Room A", "2024-01-01", 2)
        res_b = Resource("Room B", "2024-01-02", 3)
        self.ops.add_resource(res_a, {"Customer X": Reservation(0, 6)})
        self.ops.add_resource(res_b, {"Customer Y": Reservation(0, 8)})

    def test_search_by_customer(self):
        result = self.ops.search("Customer X")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].resource.name, "Room A")

    def test_search_nonexistent_customer(self):
        result = self.ops.search("Nobody")
        self.assertEqual(len(result), 0)

    def test_filter_by_date_range(self):
        ops2 = BookingOps()
        r1 = Resource("Desk", "2024-03-01", 5)
        r2 = Resource("Table", "2024-06-15", 8)
        ops2.add_resource(r1, {"A": Reservation(0, 4)})
        ops2.add_resource(r2, {"B": Reservation(0, 7)})
        filtered = ops2.search_all("2024-03-01", "2024-06-15")
        self.assertEqual(len(filtered), 2)

    def test_filter_outside_date_range(self):
        ops3 = BookingOps()
        r1 = Resource("Desk", "2024-01-01", 5)
        ops3.add_resource(r1, {"C": Reservation(0, 6)})
        result = ops3.search_all("2024-07-01", "2024-12-31")
        self.assertEqual(len(result), 0)

if __name__ == "__main__":
    unittest.main()
