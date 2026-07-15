# === Stage 58: Add bulk update behavior for selected records ===
# Project: BookingOps
def bulk_update_records(self, records):
    """Update multiple records in a single operation."""
    for record in records:
        self._update_record(record)
    return len(records)
