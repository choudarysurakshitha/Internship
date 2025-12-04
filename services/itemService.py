import json
import os

DB_FILE = os.path.join(os.path.dirname(__file__), '..', 'db.json')

class ItemService:
    def _read_db(self):
        with open(DB_FILE, 'r') as f:
            return json.load(f)

    def _write_db(self, data):
        with open(DB_FILE, 'w') as f:
            json.dump(data, f, indent=2)

    def get_all_items(self):
        db = self._read_db()
        return db.get("items", [])

    def get_item_by_id(self, item_id):
        db = self._read_db()
        for item in db.get("items", []):
            if item.get("id") == item_id:
                return item
        return None

    def add_item(self, item):
        db = self._read_db()
        items = db.get("items", [])
        item["id"] = len(items) + 1
        items.append(item)
        db["items"] = items
        self._write_db(db)
        return item

    def update_item(self, item_id, updated_data):
        db = self._read_db()
        for idx, item in enumerate(db.get("items", [])):
            if item.get("id") == item_id:
                db["items"][idx].update(updated_data)
                self._write_db(db)
                return db["items"][idx]
        return None

    def delete_item(self, item_id):
        db = self._read_db()
        items = db.get("items", [])
        for idx, item in enumerate(items):
            if item.get("id") == item_id:
                deleted_item = items.pop(idx)
                db["items"] = items
                self._write_db(db)
                return deleted_item
        return None


