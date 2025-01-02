from sqlalchemy import Column, Integer, String, DateTime
from database.database import Base

class JobORM(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    description = Column(String, nullable=True)
    location = Column(String, nullable=False)
    posted_date = Column(DateTime, nullable=False)

