# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: BookingOps
def reset_demo_data():
    """Reset all demo data to initial state for manual testing."""
    resources = [
        {"id": "room-a", "type": "meeting_room", "capacity": 10, "status": "available"},
        {"id": "room-b", "type": "meeting_room", "capacity": 5, "status": "occupied"},
        {"id": "conf-room", "type": "conference", "capacity": 30, "status": "available"},
    ]
    customers = [
        {"id": "alice", "name": "Alice Johnson", "email": "alice@example.com"},
        {"id": "bob", "name": "Bob Smith", "email": "bob@example.com"},
        {"id": "charlie", "name": "Charlie Brown", "email": "charlie@example.com"},
    ]
    reservations = [
        {
            "id": "res-1",
            "customer_id": "alice",
            "resource_id": "room-a",
            "start_time": "2024-06-01T09:00:00",
            "end_time": "2024-06-01T10:30:00",
        },
        {
            "id": "res-2",
            "customer_id": "bob",
            "resource_id": "room-b",
            "start_time": "2024-06-01T09:00:00",
            "end_time": "2024-06-01T10:00:00",
        },
    ]
    conflicts = []
    utilization = {
        "room-a": 0.3,
        "room-b": 0.5,
        "conf-room": 0.0,
    }

    with open("booking_ops_data.json", "w") as f:
        json.dump(
            {"resources": resources, "customers": customers, "reservations": reservations, "conflicts": conflicts, "utilization": utilization},
            f, indent=2
        )

    print("[OK] Demo data reset to initial state.")
