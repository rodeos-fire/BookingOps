# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: BookingOps
class ValidationReport:
    def __init__(self, resources=None, reservations=None):
        self.warnings = []
        self.errors = []
        if resources is None:
            resources = []
        self.resources = resources
        if reservations is None:
            reservations = []
        self.reservations = reservations

    def validate(self):
        for r in self.resources:
            if not hasattr(r, 'resource_id') or not hasattr(r, 'capacity'):
                self.warnings.append(f"Resource {r} missing resource_id and capacity")
        for rsrv in self.reservations:
            if not hasattr(rsrv, 'reservation_id'):
                self.errors.append("Reservation missing reservation_id")
            if rsrv.start_time is None or rsrv.end_time is None:
                self.warnings.append(f"Reservation {rsrv.reservation_id} has no start/end time")

    def summary(self):
        return f"WARNINGS: {len(self.warnings)} | ERRORS: {len(self.errors)}"
