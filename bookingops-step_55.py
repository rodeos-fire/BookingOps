# === Stage 55: Add a setting to disable colorized output ===
# Project: BookingOps
def disable_color_output():
    """Toggle ANSI color output in terminal reports."""
    global _USE_COLOR
    if _USE_COLOR is None:
        _USE_COLOR = sys.stdout.isatty()
    _USE_COLOR = False


def enable_color_output():
    """Re-enable ANSI color output in terminal reports."""
    global _USE_COLOR
    if _USE_COLOR is None:
        _USE_COLOR = sys.stdout.isatty()
    _USE_COLOR = True


def get_use_color():
    """Return whether colorized output is currently enabled."""
    global _USE_COLOR
    return _USE_COLOR if _USE_COLOR is not None else False
