import json
import os

DB_FILE = os.path.join(os.path.dirname(__file__), '..', 'db.json')

class LocationService:
    def _read_db(self):
        with open(DB_FILE, 'r') as f:
            return json.load(f)

    def _write_db(self, data):
        with open(DB_FILE, 'w') as f:
            json.dump(data, f, indent=2)

    def get_all_locations(self):
        db = self._read_db()
        return db.get("locations", [])

    def get_location_by_id(self, location_id):
        db = self._read_db()
        for loc in db.get("locations", []):
            if loc.get("id") == location_id:
                return loc
        return None

    def add_location(self, location):
        db = self._read_db()
        locations = db.get("locations", [])
        location["id"] = len(locations) + 1
        locations.append(location)
        db["locations"] = locations
        self._write_db(db)
        return location

    def update_location(self, location_id, updated_data):
        db = self._read_db()
        for idx, loc in enumerate(db.get("locations", [])):
            if loc.get("id") == location_id:
                db["locations"][idx].update(updated_data)
                self._write_db(db)
                return db["locations"][idx]
        return None

    def delete_location(self, location_id):
        db = self._read_db()
        locations = db.get("locations", [])
        for idx, loc in enumerate(locations):
            if loc.get("id") == location_id:
                deleted_loc = locations.pop(idx)
                db["locations"] = locations
                self._write_db(db)
                return deleted_loc
        return None


