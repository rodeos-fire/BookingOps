# === Stage 73: Add a lightweight HTML report export ===
# Project: BookingOps
def export_html_report(self):
    """Export current booking grid state to a self-contained HTML page."""
    lines = ["<html><head><meta charset='utf-8'><title>BookingOps Report</title>",
             "<style>body{font-family:monospace;margin:20px}table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:4px 8px;text-align:left}</style></head><body>",
             f"<h1>BookingOps Report</h1>",
             f"<p>Generated: {self._now()}</p>",
             f"<table><tr><th>Resource</th><th>Status</th><th>Utilization</th></tr>"]
    for r in self.resources.values():
        lines.append(f"<tr><td>{r.name}</td><td>{'🟢' if r.status == 'available' else '🔴'} {r.current_status}</td>"
                      f"<td>{100 * r.booked_slots / max(r.total_slots, 1):.0f}%</td></tr>")
    lines.append("</table>")
    for c in self.customers.values():
        lines.append(f"<p><b>{c.name}</b>: {len(c.reservations)} reservations — "
                      f"{', '.join(sorted(c.reservations))}</p>")
    lines.extend(["<hr>", "<footer>BookingOps v1.0 | Open-source educational project</footer></body></html>"])
    return "\n".join(lines)
