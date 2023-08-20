from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api import deps
from src.crud.crud_location_data import location_data
from src.schemas.location import LocationInsert

router = APIRouter()

@router.post("/", status_code=201)
async def collect(
    *, loc_in: LocationInsert, db: Annotated[Session, Depends(deps.get_db)]
):
    location_data.create(_db=db, obj_in=loc_in)
    print(loc_in)
