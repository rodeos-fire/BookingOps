# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: BookingOps
def clear_all(confirmed: bool = False) -> dict:
    """Reset every resource to idle and wipe all reservations."""
    if not confirmed:
        return {"error": "Confirmation required", "status": 403}
    for r in resources:
        r["status"] = "idle"
        r["booked_until"] = None
        r["last_customer"] = None
    reservations.clear()
    conflicts.clear()
    utilization_summary = {"total_resources": len(resources),
                            "active_reservations": 0,
                            "conflicts_detected": 0}
    return {"status": "cleared", "summary": utilization_summary}
