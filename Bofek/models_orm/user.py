from sqlalchemy import Column, String
from database.database import Base

class UserORM(Base):
    __tablename__ = "users"
##TODO- append to talbe the id

    phone_number = Column(String, primary_key=True)

