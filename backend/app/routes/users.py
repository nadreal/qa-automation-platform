from fastapi import APIRouter, HTTPException, status
from ..models import User

router = APIRouter()

# In-memory demo storage
users_db: dict[int, dict] = {}

@router.get("/")
def list_users():
    return list(users_db.values())

@router.post("/", status_code=201)
def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User exists")
    users_db[user.id] = user.model_dump()
    return users_db[user.id]

@router.get("/{user_id}")
def get_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]