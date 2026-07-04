# === Stage 31: Add compact table rendering for long lists ===
# Project: BookingOps
def render_compact_table(data, columns=None):
    if not data: return ""
    if columns is None: columns = list(data[0].keys())
    header = "  ".join(f"{c[:12]:<12}" for c in columns) + "\n"
    row_fmt = lambda r: "  ".join(str(r.get(c, ''))[:12] if isinstance(r.get(c), str) else str(r.get(c))[:12] for c in columns) + "\n"
    lines = [header]
    for item in data:
        try:
            lines.append(row_fmt(item))
        except Exception:
            continue
    return "".join(lines).strip()
