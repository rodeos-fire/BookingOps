# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: BookingOps
def update_resource_status(resource_id, new_status):
    if resource_id in resources:
        old = resources[resource_id].copy()
        resources[resource_id]['status'] = new_status
        return {'success': True, 'old': old, 'new': resources[resource_id]}
    else:
        raise ValueError(f"Resource {resource_id} not found")

def update_reservation_details(reservation_id, field_name, value):
    for res in reservations:
        if res['id'] == reservation_id and field_name in res:
            old_val = res[field_name]
            res[field_name] = value
            return {'success': True, 'old': old_val, 'new': value}
    raise ValueError(f"Reservation {reservation_id} or field {field_name} not found")

def delete_reservation(reservation_id):
    for i, res in enumerate(reservations):
        if res['id'] == reservation_id:
            del reservations[i]
            return {'success': True, 'deleted': reservation_id}
    raise ValueError(f"Reservation {reservation_id} does not exist")

def add_customer(customer_data):
    cust_id = customer_data.get('name') or f"CUST_{len(customers) + 1}"
    customers[cust_id] = {'id': cust_id, **customer_data}
    return {'success': True, 'created': customers[cust_id]}
