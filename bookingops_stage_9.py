# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: BookingOps
from operator import itemgetter, attrgetter
def sort_bookings(bookings, key):
    if key == 'title': return sorted(bookings, key=attrgetter('customer_name'))
    if key == 'date': return sorted(bookings, key=lambda b: (b['start_date'], b.get('end_date', '')))
    if key == 'priority': return sorted(bookings, key=itemgetter('priority'), reverse=True)
    if key == 'last_update': return sorted(bookings, key=attrgetter('updated_at'))
    return bookings
