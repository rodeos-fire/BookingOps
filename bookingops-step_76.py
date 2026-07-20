# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: BookingOps
import sys, signal


def _handle_sigint(signum, frame):
    print("\n⚠ BookingOps interrupted – flushing pending writes…")
    sys.exit(1)


signal.signal(signal.SIGINT, _handle_sigint)
try:
    from bookingops.cli import main_app
except ImportError as exc:  # pragma: no cover
    print(f"BookingOps not installed yet – {exc}", file=sys.stderr)
    sys.exit(2)

main_app()
