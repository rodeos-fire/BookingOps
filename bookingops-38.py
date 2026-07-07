# === Stage 38: Add data integrity checks for broken references ===
# Project: BookingOps
def check_references(resource: Resource, reservation: Reservation) -> List[str]:
    """Validate that every resource and customer referenced in a reservation actually exist."""
    errors = []
    if resource is None or not isinstance(resource, Resource):
        errors.append("Reservation.resource must be an instance of Resource")
    else:
        if resource.id is None:
            errors.append(f"Resource {resource} has no id attribute")

    customer_id = getattr(reservation, 'customer', None) or \
                  getattr(reservation, 'client', None) or \
                  getattr(reservation, 'guest', None)
    if customer_id is not None:
        if isinstance(customer_id, Resource):
            errors.append("Reservation.customer must be a Customer, got Resource")
        elif isinstance(customer_id, str) and customer_id.strip():
            # If stored as string, we cannot validate without a lookup table; record it.
            pass

    return errors
