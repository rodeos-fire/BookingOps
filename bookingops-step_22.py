# === Stage 22: Add favorite records and quick favorite listing ===
# Project: BookingOps
from typing import Optional, List
import json
from datetime import date

class FavoriteManager:
    def __init__(self, db_path: str = "favorites.json"):
        self.db_path = db_path
        self.favorites: dict[str, set] = {}
        self._load()

    def _load(self):
        try:
            with open(self.db_path) as f:
                data = json.load(f)
                for res_id, items in data.items():
                    self.favorites[res_id] = {item["id"] for item in items}
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def _save(self):
        with open(self.db_path, "w") as f:
            json.dump(dict(self.favorites), f)

    def add_favorite(self, resource_id: str, record_id: int):
        if resource_id not in self.favorites:
            self.favorites[resource_id] = set()
        self.favorites[resource_id].add(record_id)
        self._save()

    def remove_favorite(self, resource_id: str, record_id: int):
        if resource_id in self.favorites and record_id in self.favorites[resource_id]:
            self.favorites[resource_id].remove(record_id)
            self._save()

    def get_favorites_for_resource(self, resource_id: str) -> List[int]:
        return list(self.favorites.get(resource_id, set()))

    def list_all_favorites(self) -> dict[str, List[tuple]]:
        result = {}
        for res_id, ids in self.favorites.items():
            if ids:
                result[res_id] = [{"id": rid} for rid in sorted(ids)]
        return result
