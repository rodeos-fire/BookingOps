# === Stage 63: Add relationships between records where useful ===
# Project: BookingOps
def build_relationships(records: list) -> dict:
    """Map records to their relationships: customer->reservations, reservation->resources."""
    rel = {}
    for r in records:
        if 'customer_name' in r and 'booking_id' in r:
            key = (r['customer_name'], r.get('status', 'pending'))
            rel.setdefault(key, []).append(r)
    return rel
