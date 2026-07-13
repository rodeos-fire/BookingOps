# === Stage 53: Add command help text and usage examples ===
# Project: BookingOps
HELP_TEXT = """\
Usage: python -m bookingops [command] [options]

Commands:
  run             Run the simulation and print results.
  report          Print utilization reports for resources.
  conflicts       List all reservation conflicts (if any).

Options:
  --resources     Comma-separated list of resource names (default: 4 rooms)
  --duration      Duration in minutes per booking (default: 60)
  --count         Number of bookings to generate (default: 20)
  --seed          Random seed for reproducibility

Examples:
  python -m bookingops run --resources "A,B,C" --duration 45 --count 10
  python -m bookingops report --resources "A,B,C,D,E"
  python -m bookingops conflicts --resources "X,Y,Z,W,V,U,T,S,R"
"""
