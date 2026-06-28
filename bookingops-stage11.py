# === Stage 11: Add JSON export for the current application state ===
# Project: BookingOps
def export_state_to_json(self, filename="bookingops_state.json"):
    import json
    state = {
        "resources": [r.to_dict() for r in self.resources],
        "reservations": [rv.to_dict() for rv in self.reservations],
        "customers": list(set(c.id for c in self.customers)),
        "conflicts": len(self.conflict_log),
        "utilization_summary": {k: v for k, v in self.utilization_metrics.items()}
    }
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2)
