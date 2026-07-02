# === Stage 25: Add daily summary calculations ===
# Project: BookingOps
from datetime import date, timedelta
def calculate_daily_summary(reservations):
    today = date.today()
    summary = {}
    for r in reservations:
        if r['start_date'] <= today <= r['end_date']:
            resource_id = r['resource_id']
            customer_name = r['customer_name']
            duration_hours = (r['end_time'].hour - r['start_time'].hour) or 1
            summary[resource_id] = summary.get(resource_id, {'total_bookings': 0, 'hours_used': 0})
            summary[resource_id]['total_bookings'] += 1
            summary[resource_id]['hours_used'] += duration_hours
    return {k: v for k, v in sorted(summary.items())}
