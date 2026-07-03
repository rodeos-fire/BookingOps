# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: BookingOps
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
import json

class ReminderHelper:
    def __init__(self, booking_ops):
        self.booking_ops = booking_ops
    
    def get_upcoming_reservations(self, resource_id: str, days_ahead: int = 7) -> List[Dict[str, Any]]:
        cutoff_date = datetime.now() + timedelta(days=days_ahead)
        upcoming = []
        for res in self.booking_ops.reservations.values():
            if res.resource_id == resource_id and res.start_time <= cutoff_date:
                remaining = (res.end_time - datetime.now()).total_seconds() / 3600
                if remaining > 0:
                    upcoming.append({**res, 'hours_remaining': round(remaining, 1)})
        return sorted(upcoming, key=lambda x: x['start_time'])
    
    def get_upcoming_customers(self, days_ahead: int = 7) -> List[Dict[str, Any]]:
        cutoff_date = datetime.now() + timedelta(days=days_ahead)
        upcoming = []
        for cust in self.booking_ops.customers.values():
            if cust.reservations and any(r.start_time <= cutoff_date for r in cust.reservations):
                next_booking = min((r for r in cust.reservations if r.start_time <= cutoff_date), key=lambda x: x['start_time'])
                upcoming.append({**cust, 'next_booking': next_booking})
        return sorted(upcoming, key=lambda x: x['next_booking']['start_time'])

def load_reminders(booking_ops_file: str = "booking_ops.json") -> Dict[str, Any]:
    with open(booking_ops_file) as f:
        data = json.load(f)
    
    booking_ops = BookingOps(data.get('resources', []), 
                              data.get('reservations', []), 
                              data.get('customers', []))
    
    helper = ReminderHelper(booking_ops)
    
    upcoming_res = helper.get_upcoming_reservations("all_resources") # Simplified for demo, use specific ID in real usage
    upcoming_custs = helper.get_upcoming_customers()
    
    return {
        "upcoming_reservations": upcoming_res[:5],
        "upcoming_customers": upcoming_custs[:10]
    }

if __name__ == "__main__":
    try:
        reminders = load_reminders()
        print(json.dumps(reminders, indent=2))
    except FileNotFoundError:
        print("BookingOps data file not found.")
