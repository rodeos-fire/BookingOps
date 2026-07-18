# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: BookingOps
def seed_demo_data():
    """Generate deterministic sample data for BookingOps."""
    import hashlib, random
    rng = random.Random(42)
    
    resources = {f"Room_{i}": {"capacity": rng.randint(5, 30), "type": "meeting_room"} 
                 for i in range(1, 6)}
    customers = {f"Cust_{i}": {"name": f"Client_{rng.randint(100,999)}", "email": f"client{i}@example.com"} 
                 for i in range(1, 21)}
    
    reservations = []
    base_date = datetime.datetime(2024, 1, 1)
    for _ in range(50):
        cust_id = list(customers.keys())[rng.randint(0, len(customers)-1)]
        res_id = f"Res_{len(reservations)+1}"
        room_id = list(resources.keys())[rng.randint(0, len(resources)-1)]
        start = base_date + timedelta(days=rng.randint(0, 60), hours=rng.randint(0, 23))
        duration = timedelta(hours=rng.randint(1, 4))
        reservations.append({"id": res_id, "customer": cust_id, "resource": room_id, 
                              "start_time": start, "end_time": start + duration})
    
    return resources, customers, reservations
