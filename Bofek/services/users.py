from request_body.user import User
from repositories.users import UserRepository
from sqlalchemy.orm import Session
from services.jobs import JobService
from request_body.user_preferences import UserPreferencesRequestBody



class UserService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def ensure_user_exists(self, phone_number: str) -> User:
        user = self.user_repo.get_user_by_phone(phone_number)
        if not user:
            user = self.user_repo.add_user(phone_number)
        return user

    def get_user_preferences(self, phone_number: str) -> UserPreferencesRequestBody:
        pref = self.user_repo.get_user_preferences_by_phone(phone_number)
        if not pref:
            raise ValueError(f"User with phone number {phone_number} does not exist.")
        return UserPreferencesRequestBody.model_validate(pref)


    def update_user_preferences(self, phone_number: str, preferences: dict) -> UserPreferencesRequestBody:
        self.ensure_user_exists(phone_number)
        updated_user = self.user_repo.update_user_preferences(phone_number, preferences)
        return UserPreferencesRequestBody.model_validate(updated_user)

    def delete_user(self, phone_number: str) -> str:
        result = self.user_repo.delete_user(phone_number)
        if not result:
            raise ValueError(f"User with phone number {phone_number} does not exist.")
        return f"User with phone number {phone_number} has been successfully deleted."

    def get_jobs_by_preferences(self, phone_number: str):
        pref = self.get_user_preferences(phone_number)
        preferences_dict = pref.model_dump()

        job_service = JobService(self.user_repo.db)
        jobs = job_service.get_jobs_by_preferences(preferences_dict)
        return jobs

    def get_new_jobs_by_preferences(self, phone_number: str):
        pref = self.get_user_preferences(phone_number)
        preferences_dict = pref.model_dump()
        jobs = JobService.get_jobs_by_preferences(preferences_dict)
        return jobs


    def get_user_by_phone(self, phone_number: str) -> User:
        user = self.user_repo.get_user_by_phone(phone_number)
        if not user:
            raise ValueError(f"User with phone number {phone_number} does not exist.")
        return user
