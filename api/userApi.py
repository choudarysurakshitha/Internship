from fastapi import APIRouter, HTTPException
from services.userService import UserService

router = APIRouter(prefix="/users", tags=["Users"])
service = UserService()

@router.get("/")
def get_users():
    return service.get_all_users()

@router.get("/{user_id}")
def get_user(user_id: int):
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/")
def create_user(user: dict):
    return service.add_user(user)

@router.put("/{user_id}")
def update_user(user_id: int, updated_data: dict):
    updated = service.update_user(user_id, updated_data)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}")
def delete_user(user_id: int):
    deleted = service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted

