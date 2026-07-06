# === Stage 36: Add templates for quickly creating common records ===
# Project: BookingOps
class BookingOpsQuickCreate:
    """Utility to quickly create common records in BookingOps."""

    @staticmethod
    def new_resource(name, capacity=1, unit="hour"):
        return Resource(name=name, capacity=capacity, unit=unit)

    @staticmethod
    def new_reservation(resource_name, customer_id, start_time, end_time):
        return Reservation(
            resource_name=resource_name, customer_id=customer_id,
            start_time=start_time, end_time=end_time
        )

    @staticmethod
    def new_customer(first_name, last_name, email=""):
        return Customer(first_name=first_name, last_name=last_name, email=email)

    @staticmethod
    def new_conflict(booking_id_1, booking_id_2):
        return Conflict(booking_id_1=booking_id_1, booking_id_2=booking_id_2)

    @staticmethod
    def quick_report(resource_names=None):
        """Generate a simple utilization report."""
        if resource_names is None:
            resource_names = ["R0", "R1"]
        return {"resources": list(resource_names), "utilization_pct": 0}
