# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: BookingOps
import re
from datetime import datetime

def generate_changelog(activity_log_path="activity.log"):
    """Generate a compact changelog from an activity log."""
    with open(activity_log_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    
    changes = []
    for line in lines:
        match = re.match(r"(\d{4}-\d{2}-\d{2}).*?(?:Added|Modified|Fixed|Rename)", line)
        if match:
            date, description = match.group(1), re.sub(r".*?", "", line).split(":", 1)[1]
            changes.append({"date": date, "description": description.strip()})
    
    return "\n\n".join(f"{c['date']}: {c['description']}" for c in changes) if changes else "No changes found."

changelog = generate_changelog()
print(changelog[:500])
