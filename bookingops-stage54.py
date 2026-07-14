# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: BookingOps
def colorize(text, color):
    """Return text wrapped in ANSI escape codes for terminal coloring."""
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
    }
    reset = '\033[0m'
    if color not in colors:
        raise ValueError(f"Unsupported color: {color}")
    return f"{colors[color]}{text}{reset}"

def print_utilization_report(reservations, resources):
    """Print a colorized utilization report showing resource usage."""
    for res in sorted(resources.values(), key=lambda r: r['name']):
        total = len([r for r in reservations if r['resource'] == res['name']])
        used = len([r for r in reservations if r['resource'] == res['name'] and r['status'] != 'cancelled'])
        pct = (used / total * 100) if total else 0
        bar_len = int(pct / 5)
        if bar_len > 20:
            bar_len = 20
        filled = '#' * bar_len + '.' * (20 - bar_len)
        status_color = 'green' if pct < 80 else ('yellow' if pct < 90 else 'red')
        print(f"  {colorize(res['name'], 'cyan')} [{filled}] {pct:.1f}% ({used}/{total})")

print_utilization_report(reservations, resources)
