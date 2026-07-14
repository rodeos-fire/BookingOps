# === Stage 56: Add compact error classes for domain failures ===
# Project: BookingOps
class BookingError(Exception):
    """Base exception for all booking-related errors."""
    pass


class ResourceConflict(BookingError):
    """Raised when a reservation overlaps an existing one on the same resource."""
    def __init__(self, resource_id: str, start_time: str, end_time: str, existing_id: str) -> None:
        self.resource_id = resource_id
        self.start_time = start_time
        self.end_time = end_time
        self.existing_id = existing_id

        super().__init__(f"Conflict on {resource_id} [{existing_id}] "
                          f"({start_time}-{end_time})")


class CustomerNotFound(BookingError):
    """Raised when a customer ID does not exist in the system."""
    def __init__(self, customer_id: str) -> None:
        self.customer_id = customer_id

        super().__init__(f"No customer with id '{customer_id}'")


class ResourceUnavailable(BookingError):
    """Raised when a resource is marked unavailable or missing from catalog."""
    def __init__(self, resource_id: str, reason: str) -> None:
        self.resource_id = resource_id

        super().__init__(f"Resource {resource_id} is unavailable — {reason}")


class CapacityExceeded(BookingError):
    """Raised when a reservation would exceed the maximum capacity of a resource."""
    def __init__(self, resource_id: str, current_capacity: int, max_capacity: int) -> None:
        self.resource_id = resource_id

        super().__init__(f"Resource {resource_id}: "
                          f"capacity {current_capacity}/{max_capacity}")


class ReservationInvalid(BookingError):
    """Raised when a reservation contains bad data (negative duration, etc.)."""
    def __init__(self, detail: str) -> None:
        super().__init__(f"Invalid reservation — {detail}")
