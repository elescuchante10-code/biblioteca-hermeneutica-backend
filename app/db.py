from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Base declarativa (ya validada en 4.1)
Base = declarative_base()

# URL de la base de datos
DATABASE_URL = "sqlite:///./biblioteca.db"

# Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Session local
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

