from typing import Generator

from src.db.session import SessionLocal


def get_db() -> Generator:
    """yield db session"""
    
    _db = SessionLocal()
    _db.current_user_id = None
    try:
        yield _db
    finally:
        _db.close()
