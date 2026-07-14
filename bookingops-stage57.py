# === Stage 57: Add structured result objects for command handlers ===
# Project: BookingOps
class BookingResult:
    """Structured result for command handlers."""

    def __init__(self, status: str, message: str = "", data=None):
        self.status = status          # "ok" | "error" | "warning"
        self.message = message
        self.data = data or {}

    @property
    def success(self) -> bool:
        return self.status == "ok"

    def to_dict(self) -> dict:
        out = {"status": self.status, "message": self.message}
        if self.data is not None:
            out["data"] = self.data
        return out

    def __repr__(self):
        return f"<BookingResult status={self.status!r}>"


class ConflictError(BookingResult):
    """Raised when a reservation overlaps an existing one."""

    def __init__(self, resource_id: str, overlap_start=None, overlap_end=None):
        super().__init__(status="error", message=f"Conflict on {resource_id}")
        self.resource_id = resource_id
        self.overlap_start = overlap_start
        self.overlap_end = overlap_end

    def to_dict(self) -> dict:
        d = {"status": "error", "message": f"Conflict on {self.resource_id}"}
        if self.overlap_start is not None:
            d["overlap"] = (self.overlap_start, self.overlap_end)
        return d
