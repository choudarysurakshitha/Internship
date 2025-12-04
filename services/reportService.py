import json
import os

DB_FILE = os.path.join(os.path.dirname(__file__), '..', 'db.json')

class ReportService:
    def _read_db(self):
        with open(DB_FILE, 'r') as f:
            return json.load(f)

    def _write_db(self, data):
        with open(DB_FILE, 'w') as f:
            json.dump(data, f, indent=2)

    def get_all_reports(self):
        db = self._read_db()
        return db.get("reports", [])

    def get_report_by_id(self, report_id):
        db = self._read_db()
        for report in db.get("reports", []):
            if report.get("id") == report_id:
                return report
        return None

    def add_report(self, report):
        db = self._read_db()
        reports = db.get("reports", [])
        report["id"] = len(reports) + 1
        reports.append(report)
        db["reports"] = reports
        self._write_db(db)
        return report

    def update_report(self, report_id, updated_data):
        db = self._read_db()
        for idx, report in enumerate(db.get("reports", [])):
            if report.get("id") == report_id:
                db["reports"][idx].update(updated_data)
                self._write_db(db)
                return db["reports"][idx]
        return None

    def delete_report(self, report_id):
        db = self._read_db()
        reports = db.get("reports", [])
        for idx, report in enumerate(reports):
            if report.get("id") == report_id:
                deleted_report = reports.pop(idx)
                db["reports"] = reports
                self._write_db(db)
                return deleted_report
        return None


