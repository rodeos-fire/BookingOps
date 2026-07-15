# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: BookingOps
def bulk_delete(reservations, confirm=False):
    """Delete multiple reservations at once only when confirmed."""
    if not confirm:
        raise ValueError("Bulk delete requires user confirmation (set confirm=True).")
    deleted = []
    for res in reservations:
        if res.status == "confirmed":
            res.status = "deleted"
            deleted.append(res)
    return deleted
