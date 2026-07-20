# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: BookingOps
def _format_utilization_table(utilizations):
    """Render a formatted utilization table from a list of dicts."""
    lines = ["Resource", "Total Slots", "Booked", "Free"]
    for u in utilizations:
        total = sum(u["bookings"]) + u["free_slots"]
        booked = sum(u["bookings"])
        free = u["free_slots"]
        lines.append(f"{u['resource']:<20} {total:>10} {booked:>6} {free}")
    return "\n".join(lines)


def _detect_conflicts(reservations):
    """Find overlapping reservations for the same resource."""
    conflicts = []
    for i, r1 in enumerate(reservations):
        for j, r2 in enumerate(reservations):
            if i >= j:
                continue
            if (r1["resource"] == r2["resource"] and
                    not (r1["end_time"] <= r2["start_time"] or
                         r2["end_time"] <= r1["start_time"])):
                conflicts.append({
                    "conflicting": [r1, r2],
                    "shared_resource": r1["resource"],
                    "overlap_start": max(r1["start_time"], r2["start_time"]),
                    "overlap_end": min(r1["end_time"], r2["end_time"]),
                })
    return conflicts


def _calculate_profit(revenue, cost):
    """Compute profit from revenue and associated costs."""
    return round(revenue - cost, 2)


def _generate_summary_report(reservations, customers, utilizations):
    """Build a compact summary report combining key metrics."""
    total_revenue = sum(r["price"] for r in reservations if "price" in r)
    unique_customers = len(set(c["id"] for c in customers))
    return {
        "total_reservations": len(reservations),
        "unique_customers_served": unique_customers,
        "total_revenue": total_revenue,
        "utilization_summary": _format_utilization_table(utilizations),
    }
