# === Stage 41: Add plain text import for a simple line-based format ===
# Project: BookingOps
import csv


class PlainTextParser:
    def parse(self, text):
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        records = []
        for i in range(0, len(lines), 3):
            resource_line = lines[i] if i + 2 < len(lines) else ""
            reservation_line = lines[i+1] if i + 1 < len(lines) else ""
            customer_line = lines[i+2] if i + 2 < len(lines) else ""
            records.append({
                'resource': resource_line,
                'reservation': reservation_line,
                'customer': customer_line,
            })
        return records


def load_plain_text(filename):
    with open(filename, 'r') as f:
        text = f.read()
    parser = PlainTextParser()
    return parser.parse(text)
