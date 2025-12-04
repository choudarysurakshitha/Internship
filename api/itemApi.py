from fastapi import APIRouter, HTTPException
from services.itemService import ItemService

router = APIRouter(prefix="/items", tags=["Items"])
service = ItemService()

@router.get("/")
def get_items():
    return service.get_all_items()

@router.get("/{item_id}")
def get_item(item_id: int):
    item = service.get_item_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/")
def create_item(item: dict):
    return service.add_item(item)

@router.put("/{item_id}")
def update_item(item_id: int, updated_data: dict):
    updated = service.update_item(item_id, updated_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated

@router.delete("/{item_id}")
def delete_item(item_id: int):
    deleted = service.delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return deleted

