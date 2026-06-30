# === Stage 19: Add undo support for the last simple mutation ===
# Project: BookingOps
import json, os, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from booking_ops.models.resource import Resource
from booking_ops.models.reservation import Reservation
from booking_ops.services.booker import Booker
from booking_ops.utils.storage import Storage

class UndoManager:
    def __init__(self):
        self.history = []
        self.max_history = 10
    
    def record(self, action_type: str, data: dict) -> None:
        entry = {"action": action_type, "data": data}
        self.history.append(entry)
        if len(self.history) > self.max_history:
            self.history.pop(0)

def undo_last(storage: Storage, booker: Booker):
    manager = UndoManager()
    
    # Load current state from storage to reconstruct context for rollback
    resources_data = json.loads(storage.read("resources"))
    reservations_data = json.loads(storage.read("reservations"))
    
    resources = [Resource.from_dict(d) for d in resources_data]
    reservations = [Reservation.from_dict(d) for d in reservations_data]
    
    # Check if there is anything to undo
    if not manager.history:
        return
    
    last_action = manager.history.pop()
    action_type = last_action["action"]
    data = last_action["data"]
    
    try:
        if action_type == "create_resource":
            resource_id = data.get("id")
            for res in resources:
                if res.id == resource_id:
                    storage.write("resources", json.dumps([r.to_dict() for r in resources]))
                    return
        
        elif action_type == "delete_reservation":
            reservation_id = data.get("reservation_id")
            reservations = [r for r in reservations if r.id != reservation_id]
            storage.write("reservations", json.dumps([r.to_dict() for r in reservations]))
            
        elif action_type == "cancel_reservation":
            # Re-add the cancelled reservation to its original state
            reservation_id = data.get("reservation_id")
            status = data.get("status")
            start_time = data.get("start_time")
            end_time = data.get("end_time")
            
            new_res = Reservation(
                id=reservation_id,
                resource_id=data["resource_id"],
                customer_name=data["customer_name"],
                start=start_time,
                end=end_time,
                status=status
            )
            reservations.append(new_res)
            storage.write("reservations", json.dumps([r.to_dict() for r in reservations]))
            
        elif action_type == "update_resource":
            resource_id = data.get("resource_id")
            updated_fields = {k: v for k, v in data.items() if k != "id"}
            for res in resources:
                if res.id == resource_id:
                    for key, value in updated_fields.items():
                        setattr(res, key, value)
                    storage.write("resources", json.dumps([r.to_dict() for r in resources]))
                    
    except Exception as e:
        print(f"Undo failed: {e}")

if __name__ == "__main__":
    # Example usage hook if run directly with a valid environment setup
    pass
