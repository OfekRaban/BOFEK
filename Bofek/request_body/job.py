from pydantic import BaseModel
from typing import Optional
from datetime import datetime

 #DTO

class Job(BaseModel):
    title: Optional[str] = None  # Optional job title for updates
    company: Optional[str] = None  # Optional company for updates
    description: Optional[str] = None  # Optional job description for updates
    location: Optional[str] = None  # Optional location for updates
    posted_date: Optional[datetime] = None
