"""Declarative base class for sql alchemy models"""

from typing import Any, Dict

from sqlalchemy.ext.declarative import as_declarative, declared_attr

class_registry: Dict = {}


@as_declarative(class_registry=class_registry)
class Base:
    """Base class inherited by all models"""
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str: # noqa: E213
        return cls.__name__.lower()
