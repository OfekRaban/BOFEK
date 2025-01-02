from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLAlchemy Base
Base = declarative_base()

# SQLite database file path
DATABASE_URL = "sqlite:///C:/Users/ofekr/OneDrive/שולחן העבודה/אופק/bot_project/projectDB.db"

# Create the engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
