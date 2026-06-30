# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: BookingOps
class DryRunMixin:
    def __init__(self, dry_run=False):
        self._dry_run = dry_run
    
    @property
    def is_dry_run(self):
        return self._dry_run
    
    def _execute_action(self, action_name, func, *args, **kwargs):
        if self.is_dry_run:
            print(f"[DRY-RUN] Would {action_name}: {func.__name__}({', '.join(repr(a) for a in args)})")
            return None
        else:
            return func(*args, **kwargs)

    def create_resource(self, resource_data):
        return self._execute_action("create", self.resources.create, resource_data)

    def reserve_slot(self, resource_id, customer_id, start_time, duration):
        return self._execute_action("reserve", self.reservations.reserve, 
                                   resource_id, customer_id, start_time, duration)

    def cancel_reservation(self, reservation_id):
        return self._execute_action("cancel", self.reservations.cancel, reservation_id)

    def generate_report(self, report_type="utilization"):
        if not self.is_dry_run:
            print(f"Generating {report_type} report...")
            # Actual logic here
            pass
        else:
            print(f"[DRY-RUN] Would generate {report_type} report.")

    def add_customer(self, customer_data):
        return self._execute_action("add", self.customers.add, customer_data)
