from typing import Any, Generic, List, Optional, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from src.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, _db: Session, _id: Any) -> Optional[ModelType]:
        return _db.query(self.model).filter(self.model.id == _id).first()

    def get_multi(
        self, _db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return _db.query(self.model).offset(skip).limit(limit).all()

    def create(self, _db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        _db.add(db_obj)
        _db.commit()
        _db.refresh(db_obj)
        return db_obj

    def remove(self, _db: Session, *, _id: int) -> ModelType:
        obj = _db.query(self.model).get(_id)
        _db.delete(obj)
        _db.commit()
        return obj
