# === Stage 60: Add saved views for frequently used filters ===
# Project: BookingOps
class SavedView:
    """A named filter preset that can be restored to the grid."""
    def __init__(self, name, filters=None):
        self.name = name
        self.filters = filters or {}  # e.g., {"resource": "R1", "date": "2025-04"}

    def apply(self, grid):
        """Apply saved filter to the existing grid state."""
        for key, value in self.filters.items():
            grid.set_filter(key, value)
