import json
import os

DB_FILE = os.path.join(os.path.dirname(__file__), '..', 'db.json')

class StatusService:
    def _read_db(self):
        with open(DB_FILE, 'r') as f:
            return json.load(f)

    def _write_db(self, data):
        with open(DB_FILE, 'w') as f:
            json.dump(data, f, indent=2)

    def get_all_status(self):
        db = self._read_db()
        return db.get("status", [])

    def get_status_by_id(self, status_id):
        db = self._read_db()
        for s in db.get("status", []):
            if s.get("id") == status_id:
                return s
        return None

    def add_status(self, status):
        db = self._read_db()
        statuses = db.get("status", [])
        status["id"] = len(statuses) + 1
        statuses.append(status)
        db["status"] = statuses
        self._write_db(db)
        return status

    def update_status(self, status_id, updated_data):
        db = self._read_db()
        for idx, s in enumerate(db.get("status", [])):
            if s.get("id") == status_id:
                db["status"][idx].update(updated_data)
                self._write_db(db)
                return db["status"][idx]
        return None

    def delete_status(self, status_id):
        db = self._read_db()
        statuses = db.get("status", [])
        for idx, s in enumerate(statuses):
            if s.get("id") == status_id:
                deleted_status = statuses.pop(idx)
                db["status"] = statuses
                self._write_db(db)
                return deleted_status
        return None


