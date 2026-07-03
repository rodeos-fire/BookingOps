# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: BookingOps
def parse_date(date_str: str) -> datetime.date | None:
    """Parse date string with clear error messages."""
    if not date_str.strip():
        raise ValueError("Empty date string provided.")
    
    formats = [
        ("%Y-%m-%d", "YYYY-MM-DD"),
        ("%d.%m.%Y", "DD.MM.YYYY"),
        ("%B %d, %Y", "Month DD, YYYY"),
        ("%b %d, %Y", "Mon DD, YYYY"),
    ]
    
    for fmt, label in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    
    raise ValueError(f"Unable to parse '{date_str}'. Supported formats: {', '.join(label for _, label in formats)}")
