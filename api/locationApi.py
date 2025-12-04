from fastapi import APIRouter, HTTPException
from services.locationService import LocationService

router = APIRouter(prefix="/locations", tags=["Locations"])
service = LocationService()

@router.get("/")
def get_locations():
    return service.get_all_locations()

@router.get("/{location_id}")
def get_location(location_id: int):
    loc = service.get_location_by_id(location_id)
    if not loc:
        raise HTTPException(status_code=404, detail="Location not found")
    return loc

@router.post("/")
def create_location(location: dict):
    return service.add_location(location)

@router.put("/{location_id}")
def update_location(location_id: int, updated_data: dict):
    updated = service.update_location(location_id, updated_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Location not found")
    return updated

@router.delete("/{location_id}")
def delete_location(location_id: int):
    deleted = service.delete_location(location_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Location not found")
    return deleted

