# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: BookingOps
SETTINGS = {
    "max_reservation_duration": 180,
    "allowed_resources": ["room_a", "room_b", "projector"],
    "reporting_interval_minutes": 60,
    "conflict_resolution_strategy": "first_come_first_served"
}

def update_settings(key: str, value):
    if key in SETTINGS and isinstance(value, type(SETTINGS[key])) or (key == "allowed_resources" and isinstance(value, list)):
        SETTINGS[key] = value
        return True
    raise ValueError(f"Invalid setting '{key}' or incorrect type for value.")

def get_setting(key: str):
    if key in SETTINGS:
        return SETTINGS[key]
    raise KeyError(f"Setting '{key}' not found.")

def reset_settings():
    global SETTINGS
    SETTINGS = {
        "max_reservation_duration": 180,
        "allowed_resources": ["room_a", "room_b", "projector"],
        "reporting_interval_minutes": 60,
        "conflict_resolution_strategy": "first_come_first_served"
    }

def validate_settings():
    required_keys = {"max_reservation_duration", "allowed_resources", "reporting_interval_minutes"}
    if not required_keys.issubset(SETTINGS.keys()):
        raise ValueError("Missing required settings.")
    return True
