# === Stage 72: Add Markdown report export ===
# Project: BookingOps
def export_markdown_report(grid):
    """Export a compact markdown summary of the booking grid."""
    lines = []
    for r, name in grid.resources.items():
        lines.append(f"## Resource: {name}")
        lines.append("")
        lines.append("| Reservation | Start | End | Customer | Status |")
        lines.append("|---|---|---|---|---|")
        for res_id, res_info in sorted(grid.reservations.values()):
            if res_info['resource'] == r:
                lines.append(
                    f"| {res_id} | {res_info['start']} | {res_info['end']} "
                    f"| {res_info.get('customer','?')} | {res_info['status']} |"
                )
        lines.append("")

    conflicts = grid.conflicts
    if not conflicts:
        lines.append("## Conflicts: none")
    else:
        lines.append("## Conflicts:")
        for c in conflicts:
            lines.append(
                f"- **{c['resource']}**: {c['start']}–{c['end']} "
                f"(customers: {', '.join(c.get('customers', []))})"
            )

    util = grid.utilization
    if util:
        lines.append("## Utilization:")
        for res_id, pct in sorted(util.items()):
            bar = "#" * int(pct / 5)
            lines.append(f"- {res_id}: [{bar}] {pct:.1f}%")

    return "\n".join(lines) + "\n"
