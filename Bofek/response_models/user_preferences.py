from pydantic import BaseModel
from typing import Optional

class UserPreferencesResponse(BaseModel):
    phone_number: str
    job_type: Optional[str] = None
    field: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None

    class Config:
        from_attributes = True  # Enable ORM support if needed for serialization
