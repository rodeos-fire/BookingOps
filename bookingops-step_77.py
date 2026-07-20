# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: BookingOps
def find_conflicts(reservations: list[Reservation]) -> list[tuple[str, str]]:
    """Return pairs of reservation IDs that overlap on the same resource."""
    conflicts = []
    for i in range(len(reservations)):
        for j in range(i + 1, len(reservations)):
            if reservations[i].resource_id == reservations[j].resource_id and _overlap(
                reservations[i].start_time, reservations[i].end_time,
                reservations[j].start_time, reservations[j].end_time):
                conflicts.append((reservations[i].id, reservations[j].id))
    return conflicts


def calculate_utilization(reservations: list[Reservation], resources: list[Resource]) -> dict[str, float]:
    """Return utilization percentage per resource based on total booked time."""
    utilization = {}
    for res in resources:
        if not res.start_time or not res.end_time:
            continue
        duration = (res.end_time - res.start_time).total_seconds()
        if duration <= 0:
            continue
        booked = sum(1 for r in reservations if r.resource_id == res.id and _overlap(r.start_time, r.end_time, res.start_time, res.end_time))
        utilization[res.id] = round((booked / duration) * 100, 2)
    return utilization


def format_report(report: dict[str, Any]) -> str:
    """Format a booking operations report into a readable string."""
    lines = []
    lines.append("=== Booking Operations Report ===")
    if "resources" in report:
        lines.append(f"\nTotal Resources: {len(report['resources'])}")
        for r in report["resources"]:
            lines.append(f"  - {r.get('id', 'N/A')}: {r.get('name', 'N/A')}")
    if "reservations" in report:
        lines.append(f"\nTotal Reservations: {len(report['reservations'])}")
        for r in report["reservations"]:
            lines.append(
                f"  - {r.get('id', 'N/A')}: {r.get('customer_name', 'Unknown')} - "
                f"{r.get('resource_id', 'N/A')} on {r.get('start_time', 'N/A')} to {r.get('end_time', 'N/A')}"
            )
    if "conflicts" in report:
        lines.append(f"\nConflicts Detected: {len(report['conflicts'])}")
        for c in report["conflicts"]:
            lines.append(f"  - {c[0]} conflicts with {c[1]}")
    if "utilization" in report:
        lines.append("\nResource Utilization:")
        for rid, pct in report["utilization"].items():
            lines.append(f"  - Resource {rid}: {pct}% utilized")
    return "\n".join(lines)


def load_reservations_from_json(path: str) -> list[Reservation]:
    """Load reservations from a JSON file."""
    with open(path, "r") as f:
        data = json.load(f)
    reservations = []
    for item in data:
        r = Reservation(
            id=item["id"],
            customer_name=item.get("customer_name", ""),
            resource_id=item["resource_id"],
            start_time=parse_datetime(item["start_time"]),
            end_time=parse_datetime(item["end_time"]),
        )
        reservations.append(r)
    return reservations


def load_resources_from_json(path: str) -> list[Resource]:
    """Load resources from a JSON file."""
    with open(path, "r") as f:
        data = json.load(f)
    resources = []
    for item in data:
        r = Resource(id=item["id"], name=item.get("name", ""), start_time=parse_datetime(item.get("start_time")), end_time=parse_datetime(item.get("end_time")))
        resources.append(r)
    return resources


def run_full_analysis(reservations_path: str, resources_path: str) -> dict[str, Any]:
    """Run the full analysis pipeline and return a comprehensive report."""
    reservations = load_reservations_from_json(reservations_path)
    resources = load_resources_from_json(resources_path)
    conflicts = find_conflicts(reservations)
    utilization = calculate_utilization(reservations, resources)
    return {
        "resources": resources,
        "reservations": reservations,
        "conflicts": conflicts,
        "utilization": utilization,
    }


if __name__ == "__main__":
    report = run_full_analysis("data_reservations.json", "data_resources.json")
    print(format_report(report))
