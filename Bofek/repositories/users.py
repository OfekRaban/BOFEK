from typing import Optional
from sqlalchemy.orm import Session
from models_orm.user import UserORM
from request_body.user import User as UserRequestBody
from request_body.user_preferences import UserPreferencesRequestBody
from models_orm.user_preferences import UserPreferencesORM


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_user(self, phone_number: str):
        try:
            new_user = UserORM(phone_number=phone_number)
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            return UserRequestBody.model_validate(new_user)
        except Exception as e:
            self.db.rollback()
            raise e

    def get_user_by_phone(self, phone_number: str):
        user = self.db.query(UserORM).filter(UserORM.phone_number == phone_number).first()
        if user:
            return UserRequestBody.model_validate(user)
        return None

    def update_user_preferences(self, phone_number: str, preferences: dict) -> Optional[UserORM]:
        orm_user = self.get_user_by_phone(phone_number)
        if not orm_user:
            return None

        for key, value in preferences.items():
            if hasattr(orm_user, key):
                setattr(orm_user, key, value)
        self.db.commit()
        self.db.refresh(orm_user)
        return orm_user  # Return the actual ORM object

    def delete_user(self, phone_number: str):
        user = self.get_user_by_phone(phone_number)
        if user:
            try:
                self.db.delete(user)
                self.db.commit()
                return UserRequestBody.model_validate(user)
            except Exception as e:
                self.db.rollback()
                raise e
        return None

    def get_user_preferences_by_phone(self, phone_number: str) -> dict:
        user_preferences = self.db.query(UserPreferencesORM).filter_by(phone_number=phone_number).first()

        if not user_preferences:
            raise ValueError(f"User with phone number {phone_number} does not have preferences.")

        return UserPreferencesRequestBody.model_validate(user_preferences)

