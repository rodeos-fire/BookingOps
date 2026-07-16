# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: BookingOps
def evaluate_reservation_priority(reservation):
    """Assign a priority score to a reservation based on operational criteria."""
    score = 0
    if reservation.get("customer_tier", "standard") == "premium":
        score += 40
    elif reservation.get("customer_tier", "standard") == "vip":
        score += 70
    if reservation.get("duration_hours", 1) >= 3:
        score += 25
    elif reservation.get("duration_hours", 1) < 1:
        score -= 15
    if reservation.get("resource_type") == "high_demand":
        score += 30
    return score

def recommend_booking_order(reservations):
    """Sort and return reservations by descending priority score."""
    scored = [(evaluate_reservation_priority(r), r) for r in reservations]
    scored.sort(key=lambda x: x[0], reverse=True)
    return [res for _, res in scored]
