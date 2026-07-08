# === Stage 42: Add CSV export without external dependencies ===
# Project: BookingOps
class CSVExporter:
    def export(self, resources=None, reservations=None, customers=None):
        import csv
        from io import StringIO
        output = StringIO()
        writer = csv.writer(output)
        if resources:
            for r in resources.values():
                writer.writerow([r["id"], r["type"], r.get("capacity", 0)])
        if reservations:
            for resv in reservations.values():
                writer.writerow([resv["id"], resv["resource_id"], resv["start"], resv["end"]])
        if customers:
            for c in customers.values():
                writer.writerow([c["id"], c.get("name", ""), c["email"]])
        return output.getvalue()

    def export_to_file(self, filename, resources=None, reservations=None, customers=None):
        with open(filename, "w", newline="") as f:
            f.write(self.export(resources, reservations, customers))
