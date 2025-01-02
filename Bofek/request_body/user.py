from pydantic import BaseModel

class User(BaseModel):
    phone_number: str

    model_config = {"from_attributes": True}
