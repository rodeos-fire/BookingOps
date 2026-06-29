# === Stage 14: Add file load support with fallback demo data ===
# Project: BookingOps
def load_data(path=None):
    if path and os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {
            "resources": [{"id": 1, "name": "Room A", "capacity": 20}, {"id": 2, "name": "Lab B", "capacity": 30}],
            "customers": [{"id": 1, "name": "Alice Corp"}, {"id": 2, "name": "Bob Inc"}],
            "reservations": [],
            "conflicts": []
        }
