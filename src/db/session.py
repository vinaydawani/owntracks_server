from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

try:
    from src.core.config import config
    from src.db.base_class import Base
except ImportError:
    from core.config import config
    from db.base_class import Base

# from decouple import config

if config.DATABASE.lower() == "postgres":
    SQLALCHEMY_DATABASE_URI = URL.create(
        drivername="postgresql",
        username=config.POSTGRES_USERNAME,
        password=config.POSTGRES_PASSWORD,
        host=config.POSTGRES_HOST,
        port=config.POSTGRES_PORT,
        database=config.POSTGRES_DB,
    )
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
elif config.DATABASE.lower() == "sqlite":
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{config.SQLITE_DATA_DIR}"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
    )
    Base.metadata.create_all(engine)


# engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args=conn_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
