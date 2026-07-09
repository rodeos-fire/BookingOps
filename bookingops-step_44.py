# === Stage 44: Add backup creation for the data file ===
# Project: BookingOps
def backup_data_file(source_path, backup_dir=None):
    """Create a timestamped backup of the data file."""
    if backup_dir is None:
        backup_dir = "backups"
    os.makedirs(backup_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(backup_dir, f"{os.path.basename(source_path)}.bak_{ts}")
    shutil.copy2(source_path, dest)
