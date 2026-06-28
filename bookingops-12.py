# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: BookingOps
import json, os
from pathlib import Path

def load_json_safe(path: str) -> dict | list:
    """Load JSON with graceful handling for malformed files."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[WARN] File not found: {path}")
        return {}
    except json.JSONDecodeError as e:
        error_msg = str(e).split('\n')[0].strip()
        print(f"[ERROR] Malformed JSON in '{path}': {error_msg}")
        # Attempt to extract the line number if available for better UX
        import re
        match = re.search(r'line (\d+)', error_msg)
        if match:
            print(f"  -> Check around line {match.group(1)}")
        return {}

def save_json_safe(path: str, data):
    """Save JSON with atomic write to prevent corruption on crash."""
    temp_path = f"{path}.tmp"
    try:
        with open(temp_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        os.replace(temp_path, path)  # Atomic rename on POSIX
    except Exception as e:
        print(f"[ERROR] Failed to save {path}: {e}")
        if os.path.exists(temp_path):
            os.remove(temp_path)
