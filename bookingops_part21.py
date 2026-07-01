# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: BookingOps
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

ARCHIVE_DIR = "archive"
RETENTION_DAYS = 365

def archive_completed_records(db_path: str) -> int:
    """Move records older than RETENTION_DAYS to the archive directory."""
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)
    
    moved_count = 0
    with open(db_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    cutoff_date = datetime.now() - timedelta(days=RETENTION_DAYS)
    new_lines = []
    
    for line in lines:
        if not line.strip():
            new_lines.append(line)
            continue
        
        try:
            record = json.loads(line)
            status = record.get("status", "")
            completed_at_str = record.get("completed_at")
            
            if status == "COMPLETED" and completed_at_str:
                completed_at = datetime.fromisoformat(completed_at_str.replace("Z", "+00:00"))
                if completed_at < cutoff_date:
                    archive_path = os.path.join(ARCHIVE_DIR, f"{record['id']}.json")
                    with open(archive_path, "w", encoding="utf-8") as af:
                        af.write(line)
                    moved_count += 1
            else:
                new_lines.append(line)
        except json.JSONDecodeError:
            new_lines.append(line)
    
    if moved_count > 0:
        with open(db_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        
        return moved_count
    
    return 0

def restore_from_archive(archive_id: str, db_path: str) -> bool:
    """Restore a specific record from the archive back to the main database."""
    if not os.path.exists(os.path.join(ARCHIVE_DIR, f"{archive_id}.json")):
        raise FileNotFoundError(f"Record {archive_id} not found in archive.")
    
    with open(os.path.join(ARCHIVE_DIR, f"{archive_id}.json"), "r", encoding="utf-8") as af:
        content = af.read()
    
    # Remove the file from archive
    os.remove(os.path.join(ARCHIVE_DIR, f"{archive_id}.json"))
    
    with open(db_path, "a+", encoding="utf-8") as f:
        f.write(content)
        f.flush()
        
    return True
