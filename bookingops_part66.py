# === Stage 66: Add export of a short status dashboard ===
# Project: BookingOps
def status_dashboard(resources, reservations):
    """Print a compact dashboard: resource utilization and booking summary."""
    print("=" * 50)
    print(" BOOKINGOPS STATUS DASHBOARD")
    print("=" * 50)
    
    # Resource utilization table
    print("\n--- Resource Utilization ---")
    for res in resources:
        booked = sum(1 for r in reservations if r['resource'] == res['name'])
        total_slots = res['capacity'] * (res['end_date'] - res['start_date']).days + 1
        used_slots = sum(r.get('slots', {}).get(res['name'], []) for r in reservations if r['resource'] == res['name'])
        utilization = f"{booked}/{total_slots}"
        print(f"  {res['name']:20s} | Slots: {utilization}")

    # Booking summary
    print("\n--- Booking Summary ---")
    total_bookings = len(reservations)
    unique_customers = set(r['customer'] for r in reservations)
    print(f"  Total Reservations: {total_books}")
    print(f"  Unique Customers:   {len(unique_customers)}")

    # Conflict count
    conflicts = [r for r in reservations if r.get('conflict')]
    print(f"\n--- Conflicts ---")
    print(f"  Active Conflicts:   {len(conflicts)}")
    
    return {"total_bookings": total_bookings, "unique_customers": len(unique_customers), "conflicts": len(conflicts)}

# Example usage (uncomment to run):
if __name__ == "__main__":
    resources = [
        {"name": "Room A", "capacity": 10, "start_date": "2024-01-01", "end_date": "2024-12-31"},
        {"name": "Room B", "capacity": 5, "start_date": "2024-01-01", "end_date": "2024-12-31"}
    ]
    reservations = [
        {"resource": "Room A", "customer": "Alice", "slots": {"Room A": ["Jan"]}, "conflict": False},
        {"resource": "Room B", "customer": "Bob", "slots": {"Room B": ["Feb"]}, "conflict": True}
    ]
    status_dashboard(resources, reservations)
