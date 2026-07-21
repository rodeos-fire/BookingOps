# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: BookingOps
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from bookingops_grid import BookingOpsGrid

def main():
    grid = BookingOpsGrid()
    print("=== BookingOps Self-Check ===")
    resources = [("Room 1", "Conference"), ("Room 2", "Training"), ("Room 3", "Meeting")]
    customers = [("Alice Corp", "alice@example.com"), ("Bob Ltd", "bob@company.org")]
    reservations = [
        {"customer": "Alice Corp", "resource": "Room 1", "start": "09:00", "end": "10:30"},
        {"customer": "Bob Ltd", "resource": "Room 2", "start": "14:00", "end": "15:00"}
    ]
    grid.add_resources(resources)
    grid.add_customers(customers)
    grid.add_reservations(reservations)

    for r in resources:
        print(f"Resource {r[0]} ({r[1]})")
    for c in customers:
        print(f"Customer {c[0]} ({c[1]})")
    for res in reservations:
        print(f"Reservation: {res['customer']} @ {res['resource']} [{res['start']}-{res['end']}]")

    conflicts = grid.find_conflicts()
    if conflicts:
        print("Conflicts detected:", conflicts)
    else:
        print("No conflicts found.")

    utilization = grid.get_utilization_report()
    for r in resources:
        pct = utilization[r[0]]
        bar = "#" * int(pct / 5)
        print(f"{r[0]}: {pct}% [{bar}]")

    grid.validate()
    print("Validation passed.")
    print("=== Self-check complete ===")

if __name__ == "__main__":
    main()
