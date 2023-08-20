from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

try:
    from src.core.config import config
except ImportError:
    from core.config import config

# from decouple import config

SQLALCHEMY_DATABASE_URI = URL.create(
    drivername="postgresql",
    username=config.POSTGRES_USERNAME,
    password=config.POSTGRES_PASSWORD,
    host=config.POSTGRES_HOST,
    port=config.POSTGRES_PORT,
    database=config.POSTGRES_DB,
)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
