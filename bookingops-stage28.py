# === Stage 28: Add overdue item detection based on due dates ===
# Project: BookingOps
from datetime import date, timedelta

def detect_overdue_reservations(reservations: list[dict], current_date: date = None) -> list[tuple[str, str]]:
    if current_date is None:
        current_date = date.today()
    overdue_items = []
    for res in reservations:
        due = res.get("due_date")
        customer_id = res.get("customer_id", "unknown")
        resource_name = res.get("resource_name", "unknown")
        if isinstance(due, str):
            try:
                parsed_due = date.fromisoformat(due)
                if parsed_due < current_date:
                    overdue_items.append((customer_id, f"{resource_name} (due {parsed_due.isoformat()})"))
            except ValueError:
                pass
        elif isinstance(due, date):
            if due < current_date:
                overdue_items.append((customer_id, f"{resource_name} (due {due.isoformat()})"))
    return overdue_items

if __name__ == "__main__":
    sample_reservations = [
        {"reservation_id": "R001", "customer_id": "CUST_42", "resource_name": "ConferenceRoom_A", "start_date": date(2023, 1, 15), "due_date": date(2023, 1, 20)},
        {"reservation_id": "R002", "customer_id": "CUST_99", "resource_name": "Projector_X", "start_date": date(2024, 6, 1), "due_date": date(2024, 6, 5)},
        {"reservation_id": "R003", "customer_id": "CUST_101", "resource_name": "Laptop_Lab", "start_date": date(2024, 7, 1), "due_date": date(2024, 8, 1)},
    ]
    
    overdue = detect_overdue_reservations(sample_reservations)
    if overdue:
        print("Overdue reservations detected:")
        for cust_id, desc in overdue:
            print(f"  - Customer {cust_id}: {desc}")
    else:
        print("No overdue reservations found.")
