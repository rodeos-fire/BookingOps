# === Stage 46: Add a schema version field and migration helper ===
# Project: BookingOps
SCHEMA_VERSION = "1"


def migrate_to_v1(resources, reservations):
    """Mark every resource as initialized and log a migration event."""
    global SCHEMA_VERSION
    for r in resources:
        if not r.get("initialized"):
            r["initialized"] = True
    reservations.setdefault("_migrations", [])
    reservations["_migrations"].append({
        "version": SCHEMA_VERSION,
        "applied_at": _now(),
        "description": "Added schema_version field and initialized flag."
    })


def _now():
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).isoformat()
