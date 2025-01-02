# routers/users.py

from fastapi import APIRouter, HTTPException
from request_body.user import User as UserSchema
from response_models.user_preferences import UserPreferencesResponse  # New response model
from services.users import UserService

router = APIRouter()

@router.post("/{phone_number}", response_model=UserSchema)
def ensure_user_exists(phone_number: str):
    user = UserService.ensure_user_exists(phone_number)
    return user

@router.get("/{phone_number}/preferences", response_model=UserPreferencesResponse)  # Use the new response model here
def get_user_preferences(phone_number: str):
    try:
        preferences = UserService.get_user_preferences(phone_number)
        return preferences
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))



@router.patch("/{user_id}/preferences")
def update_user_preferences(user_id: str, user_preferences: UserPreferencesResponse):
    updated_preferences = UserService.update_user_preferences(user_id, user_preferences)
    return updated_preferences

@router.delete("/{phone_number}", response_model=dict)
def delete_user(phone_number: str):
    try:
        message = UserService.delete_user(phone_number)
        return {"message": message}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/")
def create_user(user: UserSchema):
    return
