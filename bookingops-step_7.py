# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: BookingOps
def format_resource(r):
    return f"[{r.id}] {r.name} ({r.type})"

def format_reservation(res):
    return f"{format_resource(res.resource)} | {res.customer_name} | {res.start_time} - {res.end_time}"

def format_conflict(conf):
    res1 = format_resource(conf.reservation_1)
    res2 = format_resource(conf.reservation_2)
    return f"CONFLICT: {res1} overlaps with {res2}"

def print_grid(resources, reservations, conflicts):
    print("\n=== RESOURCES ===")
    for r in resources:
        print(f"{format_resource(r)}")
    
    print("\n=== RESERVATIONS ===")
    for res in sorted(reservations, key=lambda x: x.start_time):
        print(f"  {format_reservation(res)}")
    
    if conflicts:
        print("\n=== CONFLICTS ===")
        for c in conflicts:
            print(f"  ! {format_conflict(c)}")

def format_utilization_report(total_slots, booked_slots):
    utilization = (booked_slots / total_slots * 100) if total_slots > 0 else 0
    status = "HIGH" if utilization >= 80 else "NORMAL" if utilization >= 50 else "LOW"
    return f"Utilization: {utilization:.1f}% [{status}]"
