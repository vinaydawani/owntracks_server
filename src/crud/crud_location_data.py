from src.crud.base import CRUDBase
from src.models.location_data import LocationData
from src.schemas.location import LocationInsert

class CRUDLocationData(CRUDBase[LocationData, LocationInsert]):
    ...

location_data = CRUDLocationData(LocationData)
