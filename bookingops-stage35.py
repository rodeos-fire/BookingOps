# === Stage 35: Add active user switching and user-specific records ===
# Project: BookingOps
class UserContextManager:
    def __init__(self, db):
        self.db = db
        self._active_user_id = None
        
    @property
    def active_user(self):
        if self._active_user_id is None:
            return None
        user = self.db.get("users", {"id": self._active_user_id})
        return user
    
    def switch_to_user(self, user_id):
        """Switch the context to a specific user and load their records."""
        self._active_user_id = user_id
        
    def get_my_reservations(self):
        if not self.active_user:
            return []
        res_list = self.db.get("reservations", [])
        return [r for r in res_list if r.get("user_id") == self._active_user_id]
        
    def get_my_conflicts(self):
        if not self.active_user:
            return []
        conflict_list = self.db.get("conflicts", [])
        return [c for c in conflict_list if c.get("user_id") == self._active_user_id]
        
    def get_utilization_report(self, period_days=7):
        """Generate a utilization report specific to the active user."""
        if not self.active_user:
            return {"status": "no_active_user"}
        
        reservations = self.get_my_reservations()
        total_slots = sum(r.get("duration", 0) for r in reservations)
        conflict_count = len(self.get_my_conflicts())
        
        return {
            "user_id": self._active_user_id,
            "total_bookings": len(reservations),
            "slots_used": total_slots,
            "conflict_incidents": conflict_count,
            "efficiency_score": max(0.0, 1.0 - (conflict_count / max(len(reservations), 1))) if reservations else 1.0
        }
