# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: BookingOps
def pretty_print_booking_ops():
    print("=" * 50)
    print("BookingOps - Utilization Report")
    print("=" * 50)
    
    # Example customer data
    customers = [
        {"name": "Alice Johnson", "email": "alice@example.com"},
        {"name": "Bob Smith", "email": "bob@example.com"},
        {"name": "Carol Davis", "email": "carol@example.com"}
    ]
    
    # Example resource data
    resources = [
        {"id": 1, "type": "Conference Room A", "capacity": 20},
        {"id": 2, "type": "Office Space B", "capacity": 50}
    ]
    
    # Calculate utilization
    total_capacity = sum(r["capacity"] for r in resources)
    occupied_slots = 15 + 30  # Example: slots used across reservations
    
    print(f"\nTotal Resources: {len(resources)}")
    print(f"Total Capacity: {total_capacity} seats")
    print(f"Occupied Slots: {occupied_slots}")
    print(f"Utilization Rate: {(occupied_slots/total_capacity)*100:.1f}%")
    
    print("\nCustomers:")
    for c in customers:
        print(f"  - {c['name']} ({c['email']})")
    
    print("=" * 50)

# Example usage
pretty_print_booking_ops()
