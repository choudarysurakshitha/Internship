import json
import os

DB_FILE = os.path.join(os.path.dirname(__file__), '..', 'db.json')

class UserService:
    def _read_db(self):
        with open(DB_FILE, 'r') as f:
            return json.load(f)

    def _write_db(self, data):
        with open(DB_FILE, 'w') as f:
            json.dump(data, f, indent=2)

    def get_all_users(self):
        db = self._read_db()
        return db.get("users", [])

    def get_user_by_id(self, user_id):
        db = self._read_db()
        for user in db.get("users", []):
            if user.get("id") == user_id:
                return user
        return None

    def add_user(self, user):
        db = self._read_db()
        users = db.get("users", [])
        user["id"] = len(users) + 1
        users.append(user)
        db["users"] = users
        self._write_db(db)
        return user

    def update_user(self, user_id, updated_data):
        db = self._read_db()
        for idx, user in enumerate(db.get("users", [])):
            if user.get("id") == user_id:
                db["users"][idx].update(updated_data)
                self._write_db(db)
                return db["users"][idx]
        return None

    def delete_user(self, user_id):
        db = self._read_db()
        users = db.get("users", [])
        for idx, user in enumerate(users):
            if user.get("id") == user_id:
                deleted_user = users.pop(idx)
                db["users"] = users
                self._write_db(db)
                return deleted_user
        return None


