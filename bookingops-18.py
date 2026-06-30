# === Stage 18: Add an activity log with timestamps and action names ===
# Project: BookingOps
class ActivityLog:
    def __init__(self, log_file="booking_ops.log"):
        self.file = open(log_file, "a", encoding="utf-8")

    def _format(self, action):
        return f"[{datetime.now().isoformat()}] {action}"

    def log_action(self, action: str) -> None:
        line = self._format(action) + "\n"
        self.file.write(line)
        self.file.flush()
