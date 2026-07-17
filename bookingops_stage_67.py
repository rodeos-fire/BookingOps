# === Stage 67: Add a function that returns key project metrics ===
# Project: BookingOps
def project_metrics(reservations, resource_pools):
    """Return key BookingOps metrics: total bookings, active resources, utilization %, peak hour."""
    if not reservations and not resource_pools:
        return {"total_reservations": 0, "utilization_pct": 0.0, "peak_hour": None}

    total = len(reservations)
    active_resources = sum(1 for r in resource_pools if any(r.booked_at <= res.start < r.booked_at + r.duration for res in reservations))
    utilization = (active_resources / len(resource_pools) * 100.0) if resource_pools else 0.0

    hour_counts = {}
    for res in reservations:
        h = int(res.start.hour)
        hour_counts[h] = hour_counts.get(h, 0) + 1
    peak_hour = max(hour_counts, key=hour_counts.get) if hour_counts else None

    return {"total_reservations": total, "utilization_pct": round(utilization, 2), "peak_hour": peak_hour}
