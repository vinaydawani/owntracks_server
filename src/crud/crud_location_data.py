from src.crud.base import CRUDBase
from src.models.location_data import Location
from src.schemas.location import LocationInsert


class CRUDLocation(CRUDBase[Location, LocationInsert]):
    ...


location_data = CRUDLocation(Location)
