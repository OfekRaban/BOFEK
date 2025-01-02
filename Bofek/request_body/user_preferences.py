from pydantic import BaseModel
from typing import Optional

class UserPreferencesRequestBody(BaseModel):
    phone_number: str
    job_type: Optional[str] = None
    field: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None

    model_config = {
        "from_attributes": True
    }