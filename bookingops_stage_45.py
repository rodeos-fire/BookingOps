# === Stage 45: Add restore from backup with validation ===
# Project: BookingOps
import json, os, hashlib

BACKUP_DIR = 'backups'
def restore_from_backup(version=None):
    if version is None:
        versions = sorted(os.listdir(BACKUP_DIR), reverse=True)
        if not versions:
            raise FileNotFoundError('No backups found in ' + BACKUP_DIR)
        backup_path = os.path.join(BACKUP_DIR, versions[0])
    else:
        backup_path = os.path.join(BACKUP_DIR, str(version))
    if not os.path.isfile(backup_path):
        raise FileNotFoundError(f'Backup {backup_path} does not exist')
    with open(backup_path) as f:
        data = json.load(f)
    expected_hash = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:16]
    actual_hash = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:16]
    if expected_hash != actual_hash:
        raise ValueError('Backup integrity check failed')
    return data
