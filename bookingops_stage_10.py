# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: BookingOps
class SearchFilter:
    def __init__(self, data):
        self.data = data
    
    def search(self, query, fields=None):
        if fields is None:
            fields = ['name', 'resource_name', 'customer_name', 'status']
        lower_query = query.lower()
        results = [item for item in self.data]
        for field in fields:
            try:
                key = field.split('_')[0].lower() if '_' in field else field.lower()
                if hasattr(item, '__getitem__'):
                    val = str(getattr(item, 'name' if field == 'resource_name' or field == 'customer_name' else field)).lower()
                elif isinstance(item, dict):
                    val = str(item.get(field, '')).lower()
                else:
                    continue
            except (AttributeError, TypeError, KeyError):
                continue
            results = [r for r in results if lower_query in getattr(r, 'name', getattr(r, field, '')) or 
                      (isinstance(r, dict) and lower_query in str(r.get(field, '')).lower())]
        return results

    def get_utilization(self):
        total_slots = sum(len(item.get('slots', [])) for item in self.data if isinstance(item, dict))
        booked_slots = sum(1 for item in self.data if isinstance(item, dict) and any(r['status'] == 'booked' for r in item.get('reservations', [])))
        return f"Total Slots: {total_slots}, Booked: {booked_slots}, Utilization: {(booked_slots/total_slots*100) if total_slots else 0:.2f}%"
