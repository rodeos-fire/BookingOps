# === Stage 61: Add performance timing for core list and search operations ===
# Project: BookingOps
import timeit
from bookingops import Resource, Reservation

# Benchmark core list and search operations
setup_code = """
resources = [Resource("Room-A", "Large") for _ in range(50)] + \
             [Resource("Room-B", "Small") for _ in range(30)]
reservations = []
for r in resources[:20]:
    reservations.append(Reservation(r, "Alice", start=100, end=200))
for r in resources[25:]:
    reservations.append(Reservation(r, "Bob", start=150, end=300))
"""

# 1. List operations
list_append = timeit.repeat(lambda: resources.append(Resource("Room-C", "Medium")), number=10_000, repeat=3)
print(f"append 10k resources: {min(list_append)*1e6:.2f} µs")

# 2. Search by name (linear scan)
search_name = timeit.repeat(lambda: next(r for r in resources if r.name == "Room-A"), number=5_000, repeat=3)
print(f"find resource by name: {min(search_name)*1e6:.2f} µs")

# 3. Search reservations by customer (linear scan)
search_customer = timeit.repeat(lambda: next(r for r in reservations if r.customer == "Alice"), number=5_000, repeat=3)
print(f"find reservation by customer: {min(search_customer)*1e6:.2f} µs")

# 4. Conflict detection across all reservations (nested loops)
conflict_count = timeit.repeat(lambda: sum(1 for a in reservations for b in reservations if id(a)!=id(b) and a.start<b.end and a.end>b.start), number=500, repeat=3)
print(f"O(n²) conflict scan: {min(conflict_count)*1e6:.2f} µs")
