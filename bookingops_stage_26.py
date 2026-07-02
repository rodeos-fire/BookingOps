# === Stage 26: Add weekly summary calculations ===
# Project: BookingOps
def calculate_weekly_summary(resources, reservations):
    from datetime import date, timedelta
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(weeks=1)
    
    weekly_usage = {r['id']: 0 for r in resources}
    total_slots_available = sum(r.get('capacity', 0) * (week_end - week_start).days for r in resources)
    total_slots_booked = 0
    
    for res_id, usage in weekly_usage.items():
        current_reservations = [r for r in reservations if r['resource_id'] == res_id and week_start <= date.fromtimestamp(r.get('start_time', 0)) < week_end]
        booked_hours = sum((min(date.fromtimestamp(r.get('end_time', float('inf')), year=week_end.year, month=week_end.month, day=week_end.day) if r.get('end_time') else week_end, date.fromtimestamp(r.get('start_time', 0), year=week_start.year, month=week_start.month, day=week_start.day)) - max(week_start, date.fromtimestamp(r.get('start_time', 0)), year=week_start.year, month=week_start.month, day=week_start.day)).total_seconds() / 3600 for r in current_reservations)
        weekly_usage[res_id] = booked_hours
    
    utilization_rates = {res['id']: (usage / res.get('capacity', 1)) * 100 if usage > 0 else 0 for res, usage in zip(resources, weekly_usage.values())}
    
    summary_report = {
        'week_start': week_start.isoformat(),
        'week_end': week_end.isoformat(),
        'total_resources': len(resources),
        'total_slots_available': total_slots_available,
        'total_slots_booked': sum(weekly_usage.values()),
        'average_utilization': (sum(utilization_rates.values()) / len(utilization_rates)) if utilization_rates else 0,
        'resource_details': list(zip([r['id'] for r in resources], weekly_usage, utilization_rates)),
    }
    
    return summary_report
