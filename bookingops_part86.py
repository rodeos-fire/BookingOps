# === Stage 86: Add sample command transcripts for the main CLI workflows ===
# Project: BookingOps
import sys, io

# Sample CLI transcripts for BookingOps main workflows
SAMPLES = [
    "BookingOps --help",
    "BookingOps resources list",
    "BookingOps reservations create --resource=R101 --customer=C-42 --date=2025-06-15 --time=14:00",
    "BookingOps conflicts check --start=2025-06-15 13:00 --end=2025-06-15 15:00",
    "BookingOps utilization report --resource=R101 --days=7",
]

if __name__ == "__main__":
    for s in SAMPLES:
        print(s)
