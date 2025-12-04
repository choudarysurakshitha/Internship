from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import json
from pathlib import Path

app = FastAPI(title="Lost & Found Management System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_FILE = Path("db.json")

class LostItem(BaseModel):
    item_name: str
    description: Optional[str] = None
    location_lost: str

class FoundItem(BaseModel):
    item_name: str
    description: Optional[str] = None
    location_found: str
    email: Optional[str] = None

def load_data():
    if DB_FILE.exists():
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            return data.get("lost_items", []), data.get("found_items", [])
    return [], []

def save_data():
    with open(DB_FILE, "w") as f:
        json.dump({
            "lost_items": lost_items_db,
            "found_items": found_items_db
        }, f, indent=4)

lost_items_db, found_items_db = load_data()
lost_id_counter = max([item["id"] for item in lost_items_db], default=0) + 1
found_id_counter = max([item["id"] for item in found_items_db], default=0) + 1

@app.get("/")
def home():
    return {"message": "Lost & Found API Running"}

@app.post("/lost", response_model=dict)
def add_lost_item(item: LostItem):
    global lost_id_counter
    new_item = {"id": lost_id_counter, **item.dict()}
    lost_items_db.append(new_item)
    lost_id_counter += 1
    save_data()
    return new_item

@app.get("/lost", response_model=List[dict])
def get_all_lost_items():
    return lost_items_db

@app.get("/lost/{item_id}", response_model=dict)
def get_lost_item(item_id: int):
    for item in lost_items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Lost item not found")

@app.put("/lost/{item_id}", response_model=dict)
def update_lost_item(item_id: int, updated_item: LostItem):
    for i, item in enumerate(lost_items_db):
        if item["id"] == item_id:
            lost_items_db[i].update(updated_item.dict())
            save_data()
            return lost_items_db[i]
    raise HTTPException(status_code=404, detail="Lost item not found")

@app.delete("/lost/{item_id}", response_model=dict)
def delete_lost_item(item_id: int):
    for i, item in enumerate(lost_items_db):
        if item["id"] == item_id:
            deleted = lost_items_db.pop(i)
            save_data()
            return {"message": "Deleted successfully", "item": deleted}
    raise HTTPException(status_code=404, detail="Lost item not found")

@app.post("/found", response_model=dict)
def add_found_item(item: FoundItem):
    global found_id_counter
    new_item = {"id": found_id_counter, **item.dict()}
    found_items_db.append(new_item)
    found_id_counter += 1
    save_data()
    return new_item

@app.get("/found", response_model=List[dict])
def get_all_found_items():
    return found_items_db

@app.get("/found/{item_id}", response_model=dict)
def get_found_item(item_id: int):
    for item in found_items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Found item not found")

@app.put("/found/{item_id}", response_model=dict)
def update_found_item(item_id: int, updated_item: FoundItem):
    for i, item in enumerate(found_items_db):
        if item["id"] == item_id:
            found_items_db[i].update(updated_item.dict())
            save_data()
            return found_items_db[i]
    raise HTTPException(status_code=404, detail="Found item not found")

@app.delete("/found/{item_id}", response_model=dict)
def delete_found_item(item_id: int):
    for i, item in enumerate(found_items_db):
        if item["id"] == item_id:
            deleted = found_items_db.pop(i)
            save_data()
            return {"message": "Deleted successfully", "item": deleted}
    raise HTTPException(status_code=404, detail="Found item not found")












