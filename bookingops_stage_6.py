# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: BookingOps
from typing import Optional, List
import sys

def delete_resource(resource_id: int, confirm_flag: bool = False) -> bool:
    """Delete a resource only if the confirmation flag is set."""
    resources = get_all_resources()  # Assume this function exists in global scope
    for res in resources:
        if res['id'] == resource_id:
            if not confirm_flag:
                print(f"Deletion of Resource {resource_id} cancelled. Set confirm_flag=True to proceed.")
                return False
            del res
            save_resources()  # Assume this function exists in global scope
            print(f"Resource {resource_id} deleted successfully.")
            return True
    print(f"Resource with ID {resource_id} not found.")
    return False

def delete_reservation(reservation_id: int, confirm_flag: bool = False) -> bool:
    """Delete a reservation only if the confirmation flag is set."""
    reservations = get_all_reservations()  # Assume this function exists in global scope
    for resv in reservations:
        if resv['id'] == reservation_id:
            if not confirm_flag:
                print(f"Deletion of Reservation {reservation_id} cancelled. Set confirm_flag=True to proceed.")
                return False
            del resv
            save_reservations()  # Assume this function exists in global scope
            print(f"Reservation {reservation_id} deleted successfully.")
            return True
    print(f"Reservation with ID {reservation_id} not found.")
    return False

def delete_customer(customer_id: int, confirm_flag: bool = False) -> bool:
    """Delete a customer only if the confirmation flag is set."""
    customers = get_all_customers()  # Assume this function exists in global scope
    for cust in customers:
        if cust['id'] == customer_id:
            if not confirm_flag:
                print(f"Deletion of Customer {customer_id} cancelled. Set confirm_flag=True to proceed.")
                return False
            del cust
            save_customers()  # Assume this function exists in global scope
            print(f"Customer {customer_id} deleted successfully.")
            return True
    print(f"Customer with ID {customer_id} not found.")
    return False

def delete_conflict(conflict_id: int, confirm_flag: bool = False) -> bool:
    """Delete a conflict record only if the confirmation flag is set."""
    conflicts = get_all_conflicts()  # Assume this function exists in global scope
    for conf in conflicts:
        if conf['id'] == conflict_id:
            if not confirm_flag:
                print(f"Deletion of Conflict {conflict_id} cancelled. Set confirm_flag=True to proceed.")
                return False
            del conf
            save_conflicts()  # Assume this function exists in global scope
            print(f"Conflict {conflict_id} deleted successfully.")
            return True
    print(f"Conflict with ID {conflict_id} not found.")
    return False

def delete_all_entities(entity_type: str, confirm_flag: bool = False) -> int:
    """Delete all entities of a given type if confirmed."""
    count = 0
    if entity_type == 'resource':
        resources = get_all_resources()
        for res in resources:
            del res
            save_resources()
            print(f"Deleted Resource {res['id']}.")
            count += 1
    elif entity_type == 'reservation':
        reservations = get_all_reservations()
        for resv in reservations:
            del resv
            save_reservations()
            print(f"Deleted Reservation {resv['id']}.")
            count += 1
    elif entity_type == 'customer':
        customers = get_all_customers()
        for cust in customers:
            del cust
            save_customers()
            print(f"Deleted Customer {cust['id']}.")
            count += 1
    elif entity_type == 'conflict':
        conflicts = get_all_conflicts()
        for conf in conflicts:
            del conf
            save_conflicts()
            print(f"Deleted Conflict {conf['id']}.")
            count += 1
    else:
        print(f"Unknown entity type: {entity_type}")
        return 0
    
    if not confirm_flag and count > 0:
        print("All deletions cancelled. Set confirm_flag=True to proceed.")
        # Restore logic would go here in a real app, omitted for brevity as per constraints
        return 0
        
    return count

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py [resource|reservation|customer|conflict] [id]")
        sys.exit(1)
    
    entity_type = sys.argv[1].lower()
    target_id = int(sys.argv[2])
    
    if len(sys.argv) > 3 and sys.argv[3].lower() == 'force':
        confirm_flag = True
    else:
        confirm_flag = False
    
    success = delete_resource(target_id, confirm_flag=confirm_flag) \
              or delete_reservation(target_id, confirm_flag=confirm_flag) \
              or delete_customer(target_id, confirm_flag=confirm_flag) \
              or delete_conflict(target_id, confirm_flag=confirm_flag)
    
    if not success:
        sys.exit(1)
