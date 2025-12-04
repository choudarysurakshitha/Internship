from fastapi import APIRouter, HTTPException
from services.statusService import StatusService

router = APIRouter(prefix="/status", tags=["Status"])
service = StatusService()

@router.get("/")
def get_all_status():
    return service.get_all_status()

@router.get("/{status_id}")
def get_status(status_id: int):
    stat = service.get_status_by_id(status_id)
    if not stat:
        raise HTTPException(status_code=404, detail="Status not found")
    return stat

@router.post("/")
def create_status(status: dict):
    return service.add_status(status)

@router.put("/{status_id}")
def update_status(status_id: int, updated_data: dict):
    updated = service.update_status(status_id, updated_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Status not found")
    return updated

@router.delete("/{status_id}")
def delete_status(status_id: int):
    deleted = service.delete_status(status_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Status not found")
    return deleted

