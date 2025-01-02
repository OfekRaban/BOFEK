from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from database.database import Base

class UserPreferencesORM(Base):
    __tablename__ = "user_preferences"

    # Define columns
    phone_number = Column(String , ForeignKey("users.phone_number"),  primary_key=True, unique=True, nullable=False)
    job_type = Column(String, nullable=True)
    field = Column(String, nullable=True)
    company = Column(String, nullable=True)
    location = Column(String, nullable=True)

    def __repr__(self):
        return f"<UserPreferences(phone_number={self.phone_number}, job_type={self.job_type}, field={self.field}, company={self.company}, location={self.location})>"
