# === Stage 81: Add final README text as a module string with usage examples ===
# Project: BookingOps
# BookingOps — quick-start usage examples (append to README)

from bookingops import Resource, Reservation, Customer, ConflictDetector, UtilizationReport

# 1. Create a resource and two customers
room = Resource("A", "Meeting Room A", capacity=50)
alice = Customer("Alice")
bob   = Customer("Bob")

# 2. Book a reservation for Alice (morning slot)
r1 = Reservation(room, alice, start="2024-06-01T09:00:00", end="2024-06-01T10:00:00")

# 3. Try to book Bob in the same slot → conflict
r2 = Reservation(room, bob, start="2024-06-01T09:30:00", end="2024-06-01T10:30:00")

# 4. Detect conflicts
detector = ConflictDetector()
conflicts = detector.find(r1, r2)      # returns [r1, r2] (overlap detected)
print(f"Conflicts found: {len(conflicts)}")

# 5. Generate a utilization report for the day
report = UtilizationReport(room, start="2024-06-01T00:00:00", end="2024-06-01T23:59:59")
report.add(r1)                         # add valid reservation
print(f"Utilization: {report.calculate()}")  # e.g. "30/60 min used (50%) in Meeting Room A"

# That's it — BookingOps is ready to run without any external dependencies!
