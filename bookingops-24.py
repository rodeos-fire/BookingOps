# === Stage 24: Add grouped summaries by category or status ===
# Project: BookingOps
from collections import defaultdict, Counter

def generate_grouped_summary(reservations: list[dict], group_by: str = "status") -> dict[str, dict]:
    groups = defaultdict(list)
    for r in reservations:
        key = r.get(group_by, "unknown")
        groups[key].append(r)
    
    summary = {}
    total_slots = sum(r["duration"] * (r.get("resource_count", 1)) for r in reservations if r.get("status"))
    
    for status, items in sorted(groups.items()):
        active_items = [i for i in items if i.get("status")]
        completed_items = [i for i in items if not i.get("status")]
        
        summary[status] = {
            "count": len(items),
            "active_count": len(active_items),
            "completed_count": len(completed_items),
            "total_duration_hours": sum(i["duration"] for i in active_items),
            "utilization_pct": round((summary.get("total_slots", 1) and (sum(i["duration"] for i in items)) / summary["total_slots"]) * 100 or 0, 2) if status == "all" else None,
        }
    
    return dict(summary)
