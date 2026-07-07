# === Stage 40: Add plain text report export ===
# Project: BookingOps
def export_report_text(self):
    """Export booking report as plain text."""
    import io
    buf = io.StringIO()
    def w(line=''):
        print(line, file=buf)
    w('BookingOps Report')
    w('=' * 30)
    for res in self.resources:
        w(f'Resource: {res.name}')
        if hasattr(res, 'capacity'):
            w(f'  Capacity: {res.capacity} units')
        if hasattr(res, 'status'):
            w(f'  Status: {res.status}')
        w()
    for cust in self.customers:
        w(f'Customer: {cust.name} ({cust.email})')
        if hasattr(cust, 'phone'):
            w(f'  Phone: {cust.phone}')
        w()
    for res in self.resources:
        reserved = sum(1 for r in self.reservations if r.resource == res)
        total = sum(r.capacity for r in self.reservations if r.resource == res)
        util = (total / res.capacity * 100) if res.capacity else 0
        w(f'Utilization: {util:.1f}%')
    return buf.getvalue()
