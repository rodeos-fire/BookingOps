# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: BookingOps
def validate_id(value):
    if not isinstance(value, str) or len(value) < 3:
        raise ValueError("ID must be a string of at least 3 characters")
    return value.lower().replace("-", "").replace("_", "")

def validate_email(value):
    pattern = r"^[^@]+@[^@]+\.[^@]+$"
    if not re.match(pattern, value):
        raise ValueError("Invalid email format")
    return value.strip()

def validate_phone(value):
    cleaned = re.sub(r"[^\d+]", "", value)
    if len(cleaned) < 10:
        raise ValueError("Phone number too short")
    return "+" + "".join([c for c in cleaned if c.isdigit()])[:15]

def validate_short_text(value, max_len=256):
    text = str(value).strip()
    if len(text) > max_len:
        raise ValueError(f"Text exceeds {max_len} characters")
    return text
