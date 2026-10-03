from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# Database Configuration
DATABASE_URL = "sqlite:///./users.db"


# Engine Initialization (check_same_thread=False is required for SQLite in FastAPI)
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
)


# Session Setup
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

# Declarative Base for ORM models
Base = declarative_base()


# Dependency to get DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()