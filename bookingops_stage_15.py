# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: BookingOps
class CommandDispatcher:
    def __init__(self, grid):
        self.grid = grid
        self.handlers = {
            'list_resources': lambda args: self._execute('resources', None),
            'add_resource': lambda args: self._execute('resource_add', {'name': args.get('name')}),
            'book_slot': lambda args: self._execute('reservation_create', {'resource_id': args['resource_id'], 'customer_name': args['customer_name']}),
        }

    def _execute(self, action, payload):
        if action in self.handlers:
            try:
                result = self.grid[action](payload)
                print(f"OK: {result}")
            except Exception as e:
                print(f"ERROR: {e}")
        else:
            print(f"UNKNOWN COMMAND: {action}")

    def dispatch(self, command_text):
        parts = command_text.strip().split(maxsplit=1)
        if not parts[0]: return
        action = parts[0].replace('_', '')
        payload = {}
        try:
            payload_str = parts[1] if len(parts) > 1 else ''
            for key, val in [('resource_id', int), ('customer_name', str)]:
                if f'{key}=' in payload_str:
                    k, v = payload_str.split(f'{key}=')
                    payload[key] = val(v.strip())
        except ValueError:
            pass
        self.handlers.get(action.replace('_', ''), lambda args: print("INVALID ARGS"))(payload)
