# === Stage 43: Add CSV import for the primary record type ===
# Project: BookingOps
def csv_import(filename, record_type="resource"):
    """Import records from a CSV file into the BOOKINGOPS_REGISTRY."""
    import csv
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rec = {}
            for col in reader.fieldnames:
                val = row[col].strip()
                try:
                    rec[col] = int(val) if val.isdigit() else float(val) if "." in val else val
                except (ValueError, AttributeError):
                    rec[col] = val
            BOOKINGOPS_REGISTRY[record_type].append(rec)
