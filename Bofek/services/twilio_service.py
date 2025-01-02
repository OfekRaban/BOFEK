from services.users import UserService
from sqlalchemy.orm import Session


class TwilioService:
    def __init__(self, db: Session):
        self.user_service = UserService(db)

    async def handle_twilio_message(self, from_number: str, message: str) -> str:
        user_input = message.strip().lower()

        if "show my preferences" in user_input:
            return await self.user_service.get_user_preferences(from_number)

        elif "update preferences" in user_input:
            # Try to parse preferences first
            preferences = parse_preferences(
                message.replace("update preferences", "").strip()
            )

            # Validate critical fields
            if "job_type" not in preferences or "field" not in preferences:
                return (
                    "To set preferences and start using the amazing BOFEK, "
                    "please copy and fulfill this template:\n"
                    "job_type:\n"
                    "field:\n"
                    "company (optional):\n"
                    "location (optional):\n"
                )
            else:
                return await self.user_service.update_user_preferences(from_number, preferences)

        elif "get jobs" in user_input:
            return await self.user_service.get_jobs_by_preferences(from_number)

        elif "get newest jobs" in user_input:
            return await self.user_service.get_new_jobs_by_preferences(from_number)

        elif "help" in user_input:
            return (
                "Available commands:\n"
                "- Show My Preferences\n"
                "- Update Preferences\n"
                "- Get Jobs\n"
                "- Get Newest Jobs\n"
                "- Help\n"
            )

        else:
            return "Sorry, I didn't understand that. Type 'help' for available commands."


def parse_preferences(message: str) -> dict:
    preferences = {}
    for line in message.split("\n"):
        parts = line.split(":", 1)
        if len(parts) == 2:
            key, value = parts
            preferences[key.strip().lower()] = value.strip()
    return preferences
