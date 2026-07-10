# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: BookingOps
def demo():
    from resources import Resource, ResourceType
    from reservations import Reservation

    # Resources
    r1 = Resource("Room A", ResourceType.HALLWAY)
    r2 = Resource("Conference Room B", ResourceType.CONFERENCE)
    r3 = Resource("Lobby", ResourceType.LOBBY)

    # Customers
    c1 = "Alice"
    c2 = "Bob"
    c3 = "Charlie"

    # Reservations with conflicts
    res1 = Reservation(r1, c1, 9.0, 10.30)
    res2 = Reservation(r2, c2, 11.0, 12.30)
    res3 = Reservation(r3, c3, 8.0, 17.0)

    # Create bookings with conflicts
    booking1 = {"customer": c1, "resource": r1, "start": 9.0, "end": 10.30}
    booking2 = {"customer": c2, "resource": r2, "start": 11.0, "end": 12.30}
    booking3 = {"customer": c3, "resource": r3, "start": 8.0, "end": 17.0}

    # Check for conflicts between bookings
    has_conflict_1_2 = check_conflict(booking1, booking2)
    has_conflict_1_3 = check_conflict(booking1, booking3)
    has_conflict_2_3 = check_conflict(booking2, booking3)

    print(f"Booking 1 and 2 conflict: {has_conflict_1_2}")
    print(f"Booking 1 and 3 conflict: {has_conflict_1_3}")
    print(f"Booking 2 and 3 conflict: {has_conflict_2_3}")

    # Calculate utilization for each resource
    util_1 = calculate_utilization(r1, [booking1])
    util_2 = calculate_utilization(r2, [booking2])
    util_3 = calculate_utilization(r3, [booking3])

    print(f"Room A utilization: {util_1}")
    print(f"Conference Room B utilization: {util_2}")
    print(f"Lobby utilization: {util_3}")


demo()
