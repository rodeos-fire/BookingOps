# === Stage 13: Add file save support using a configurable path ===
# Project: BookingOps
import json, os
from pathlib import Path

class Config:
    def __init__(self):
        self.data_dir = Path("data")
        self.cache_file = self.data_dir / "booking_ops.json"
    
    def ensure_dirs(self):
        if not self.data_dir.exists():
            self.data_dir.mkdir(parents=True)
    
    def save_state(self, state: dict):
        self.ensure_dirs()
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2)

config = Config()
