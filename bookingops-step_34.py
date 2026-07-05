# === Stage 34: Add support for multiple local user profiles ===
# Project: BookingOps
from pathlib import Path
import json, uuid

class UserProfiles:
    def __init__(self):
        self._profiles = {}
        self._current_profile = None
        self._storage_path = Path("bookingops_profiles.json")
    
    @property
    def current(self) -> dict | None:
        if not self._current_profile or self._current_profile not in self._profiles:
            return None
        return self._profiles[self._current_profile]
    
    def load(self):
        try:
            data = json.loads(self._storage_path.read_text())
            for name, profile_data in data.items():
                profile_data["id"] = uuid.UUID(profile_data.get("uuid", str(uuid.uuid4())))
                self._profiles[name] = profile_data
        except FileNotFoundError:
            pass
    
    def save(self):
        if not self._profiles:
            return
        clean_data = {name: {k: v for k, v in p.items() if k != "id"} for name, p in self._profiles.items()}
        self._storage_path.write_text(json.dumps(clean_data, indent=2))
    
    def create(self, name: str) -> dict:
        profile = {"name": name, "uuid": str(uuid.uuid4()), "resources": [], "reservations": []}
        self._profiles[name] = profile
        if not self._current_profile:
            self.switch(name)
        return profile
    
    def switch(self, name: str):
        self._current_profile = name
        return self.current
