# === Stage 20: Add duplicate detection for newly created records ===
# Project: BookingOps
class DuplicateChecker:
    def __init__(self, db):
        self.db = db
    
    def check_resource_duplicate(self, resource_name, resource_type):
        query = f"SELECT id FROM resources WHERE name='{resource_name}' AND type='{resource_type}'"
        cursor = self.db.cursor()
        try:
            cursor.execute(query)
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error checking resource duplicate: {e}")
            return False
    
    def check_customer_duplicate(self, customer_name):
        query = "SELECT id FROM customers WHERE name=%s"
        cursor = self.db.cursor()
        try:
            cursor.execute(query, (customer_name,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error checking customer duplicate: {e}")
            return False
    
    def check_reservation_duplicate(self, resource_id, start_time, end_time):
        query = "SELECT id FROM reservations WHERE resource_id=%s AND start_time>%s AND end_time<%s"
        cursor = self.db.cursor()
        try:
            cursor.execute(query, (resource_id, start_time.isoformat(), end_time.isoformat()))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error checking reservation duplicate/conflict: {e}")
            return False
