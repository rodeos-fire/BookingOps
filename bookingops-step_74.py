# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: BookingOps
def snapshot_diff(old_state, new_state):
    """Compact helper that returns a readable before/after diff of two snapshots.

    Parameters
        old_state: dict with keys 'resources', 'reservations', 'conflicts'.
        new_state: dict with the same structure after some modifications.

    Returns
        str containing a formatted comparison suitable for logging or reports.

    Example
        >>> s1 = {'resources': ['R1','R2'], 'reservations': [], 'conflicts': []}
        >>> s2 = {'resources': ['R1','R2','R3'], 'reservations': [('R1', 10)], 'conflicts': []}
        >>> snapshot_diff(s1, s2)
        '--- Before ---\\nresources: R1, R2\\nreservations: (none)\\nconflicts: (none)\\n'
        '+++ After ----\\nresources: R1, R2, R3\\nreservations: (R1, 10)\\nconflicts: (none)\\n'

    Raises
        TypeError: if either argument is not a dict.
    """
    if not isinstance(old_state, dict):
        raise TypeError("old_state must be a dict")
    if not isinstance(new_state, dict):
        raise TypeError("new_state must be a dict")

    required = ('resources', 'reservations', 'conflicts')
    for key in required:
        if key not in old_state or key not in new_state:
            raise ValueError(f"Both states must contain keys {required}")

    def fmt_res(src):
        return ", ".join(sorted(src)) if src else "(none)"

    lines = []
    lines.append("--- Before ---")
    lines.append(f"resources : {fmt_res(old_state['resources'])}")
    lines.append(f"reservations: {fmt_res(old_state['reservations'])}")
    lines.append(f"conflicts  : {fmt_res(old_state['conflicts'])}")

    lines.append("+++ After ----")
    lines.append(f"resources : {fmt_res(new_state['resources'])}")
    lines.append(f"reservations: {fmt_res(new_state['reservations'])}")
    lines.append(f"conflicts  : {fmt_res(new_state['conflicts'])}")

    return "\n".join(lines)
