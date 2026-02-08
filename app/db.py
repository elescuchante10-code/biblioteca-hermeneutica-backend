from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Base declarativa
Base = declarative_base()

# Base de datos (SQLite por ahora)
DATABASE_URL = "sqlite:///./biblioteca.db"

# Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Sesión local
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


