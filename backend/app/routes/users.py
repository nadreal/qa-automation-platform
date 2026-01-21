from fastapi import APIRouter, HTTPException, status
from ..models import User
from backend.app.dependencies import user_service

router = APIRouter()

@router.get("/")
def list_users():
    return user_service.list_users()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    try:
        return user_service.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}")
def get_user(user_id: int):
    try:
        return user_service.get_user(user_id)
    except KeyError:    
        raise HTTPException(status_code=404, detail="User not found")    

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    try:
        return user_service.delete_user(user_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="User not found") 