"""Import all the models, so that Base has them before being imported by Alembic"""
from src.db.base_class import Base  # noqa: F401
from src.models.location_data import Location  # noqa: F401
