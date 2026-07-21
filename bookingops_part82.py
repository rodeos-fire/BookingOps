# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: BookingOps
def run_demo():
    """End-to-end demonstration of BookingOps."""
    from resources import Resource
    from reservations import Reservation
    from conflicts import ConflictDetector
    from customers import Customer, CustomerService
    from reports import UtilizationReport
    from scheduler import Scheduler
    
    # --- Customers ---
    alice = Customer("Alice", "alice@example.com")
    bob = Customer("Bob", "bob@example.com")

    # --- Resources ---
    room_a = Resource("Room A", capacity=5)
    room_b = Resource("Room B", capacity=3)

    # --- Reservations ---
    res1 = Reservation(alice, room_a, start="2024-06-15 09:00", end="2024-06-15 10:00")
    res2 = Reservation(bob, room_a, start="2024-06-15 10:30", end="2024-06-15 11:30")

    # --- Conflict Detection ---
    detector = ConflictDetector()
    conflicts = detector.check([res1, res2], room_a)
    print(f"Conflicts in Room A: {conflicts}")

    # --- Scheduling ---
    scheduler = Scheduler(room_a, capacity=5)
    scheduled_reservations = scheduler.schedule(res1, res2)
    print(f"Scheduled reservations for Room A: {scheduled_reservations}")

    # --- Utilization Report ---
    report = UtilizationReport()
    utilization = report.generate([room_a, room_b], [res1, res2])
    print(f"Utilization Report:\n{utilization}")

    # --- Customer Service ---
    service = CustomerService()
    recommendations = service.get_recommendations(alice, res1)
    print(f"Recommendations for Alice: {recommendations}")
