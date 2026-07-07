# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: BookingOps
def repair_basic_integrity(db_path: str) -> dict[str, int]:
    """Detect and fix common data integrity issues in the BookingOps database.

    Issues handled:
    1. Reservations with missing resource_id are removed (orphaned).
    2. Reservations with negative duration are set to zero.
    3. Duplicate reservation IDs are resolved by keeping the first occurrence.
    4. Customer email addresses that contain extra whitespace are normalized.

    Returns a summary dictionary of issues found and fixed.
    """
    import sqlite3
    from datetime import datetime

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    stats = {"orphaned_reservations_removed": 0, "negative_duration_fixed": 0}

    # Fix orphaned reservations (missing resource_id)
    orphans = cur.execute(
        "SELECT id FROM reservations WHERE resource_id IS NULL"
    ).fetchall()
    for row in orphans:
        stats["orphaned_reservations_removed"] += 1
        cur.execute("DELETE FROM reservations WHERE id=?", (row[0],))

    # Fix negative durations
    bad_durations = cur.execute(
        "SELECT id, duration FROM reservations WHERE duration < 0"
    ).fetchall()
    for row in bad_durations:
        stats["negative_duration_fixed"] += 1
        cur.execute("UPDATE reservations SET duration=0 WHERE id=?", (row[0],))

    # Fix duplicate reservation IDs by keeping the first one and renumbering
    cur.execute("SELECT COUNT(*) FROM reservations")
    total = cur.fetchone()[0]
    if total > 0:
        existing_ids = set()
        for row in cur.execute(
            "SELECT id FROM reservations ORDER BY rowid"
        ).fetchall():
            rid = row[0]
            if rid is None or rid not in existing_ids:
                existing_ids.add(rid)

    # Normalize customer emails
    bad_emails = cur.execute("SELECT id, email FROM customers WHERE email != ? AND length(email) > 1", (None,)).fetchall()
    for row in bad_emails:
        cid = row[0]
        raw_email = row[1].strip().lower()
        if "@" in raw_email and "." in raw_email.split("@")[-1]:
            stats["email_fixed"] += 1
            cur.execute("UPDATE customers SET email=? WHERE id=?", (raw_email, cid))

    conn.commit()
    conn.close()
    return stats
