# === Stage 32: Add pagination helpers for long console output ===
# Project: BookingOps
def paginate_output(data, max_lines=15):
    if len(data) <= max_lines:
        print('\n'.join(str(item) for item in data))
        return
    print(f"Showing first {max_lines} of {len(data)} items...")
    for i, item in enumerate(data[:max_lines], 1):
        print(f"{i}. {item}")

def paginate_output_with_summary(data, max_lines=10, summary_key=None):
    if not data:
        return
    total = len(data)
    preview = '\n'.join(str(item) for item in data[:max_lines])
    remaining = total - max_lines
    print(preview)
    if remaining > 0 and summary_key:
        summaries = [str(getattr(item, summary_key)) or str(item) for item in data[max_lines:]]
        print(f"\n... ({remaining} more items)\n")
        print("Summaries:")
        for s in summaries[:5]:
            print(f"  - {s}")

def paginate_output_with_stats(data, max_lines=10):
    if not data:
        return
    total = len(data)
    preview = '\n'.join(str(item) for item in data[:max_lines])
    remaining = total - max_lines
    print(preview)
    if remaining > 0:
        stats = {k: sum(getattr(item, k, 0) or 0 for item in data) / total for k in dir(data[0]) if not k.startswith('_')}
        print(f"\nStats (first {max_lines} shown):")
        for k, v in stats.items():
            print(f"  {k}: {v:.2f}")
