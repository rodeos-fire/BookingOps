# === Stage 64: Add validation for relationship references ===
# Project: BookingOps
class ReferenceValidator:
    """Validates that reservation references to resources and customers exist."""

    @staticmethod
    def validate_references(reservations, resources, customers):
        errors = []
        for res in reservations:
            if res.resource_id not in resources:
                errors.append(f"Reservation {res.id} references non-existent resource {res.resource_id}")
            if res.customer_id and res.customer_id not in [c.id for c in customers]:
                errors.append(f"Reservation {res.id} references non-existent customer {res.customer_id}")
        return errors

    @staticmethod
    def assert_references(reservations, resources, customers):
        errors = ReferenceValidator.validate_references(reservations, resources, customers)
        if errors:
            raise ValueError("Invalid relationship references in reservations")
