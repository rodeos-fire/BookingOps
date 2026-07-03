# === Stage 27: Add monthly summary calculations ===
# Project: BookingOps
from datetime import timedelta, date
def calculate_monthly_summary(reservations):
    monthly_stats = {}
    for res in reservations:
        month_key = f"{res['start_date'].year}-{res['start_date'].month:02d}"
        if month_key not in monthly_stats:
            monthly_stats[month_key] = {'total_bookings': 0, 'unique_customers': set(), 'resources_used': set()}
        monthly_stats[month_key]['total_bookings'] += 1
        monthly_stats[month_key]['unique_customers'].add(res['customer_id'])
        monthly_stats[month_key]['resources_used'].add(res['resource_id'])
    summary = []
    for month in sorted(monthly_stats.keys()):
        stats = monthly_stats[month]
        utilization = len(stats['resources_used']) / max(len(set(r['resource_id'] for r in reservations if res['start_date'].year == res['start_date'].year and res['start_date'].month == res['start_date'].month), default=1)) * 100
        summary.append({
            'month': month,
            'bookings': stats['total_bookings'],
            'customers': len(stats['unique_customers']),
            'resources_used': len(stats['resources_used']),
            'utilization_percent': round(utilization, 2)
        })
    return summary
