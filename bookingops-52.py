# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: BookingOps
def get_utilization_report(resource, start_date, end_date):
    """Compute a utilization report for `resource` over [start_date, end_date].

    Returns a dict with keys: 'resource', 'total_hours', 'booked_hours',
    'utilization_percent', 'status'.
    """
    total_minutes = 0
    booked_minutes = 0
    conflicts = []

    for day in range((end_date - start_date).days + 1):
        date = start_date + timedelta(days=day)
        morning = resource.bookings.get(date, {}).get('morning', [])
        afternoon = resource.bookings.get(date, {}).get('afternoon', [])

        booked_minutes += len(morning) * RESOURCE_DURATION + len(afternoon) * RESOURCE_DURATION
        total_minutes += 2 * RESOURCE_DURATION

        for booking in morning:
            if not booking['confirmed']:
                conflicts.append(booking['id'])
        for booking in afternoon:
            if not booking['confirmed']:
                conflicts.append(booking['id'])

    utilization = (booked_minutes / total_minutes * 100) if total_minutes > 0 else 0.0
    return {
        'resource': resource.name,
        'total_hours': total_minutes // 60,
        'booked_hours': booked_minutes // 60,
        'utilization_percent': round(utilization, 2),
        'status': 'Active' if utilization >= 75 else 'Underutilized',
        'conflicts': conflicts,
    }
