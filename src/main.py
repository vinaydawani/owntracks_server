"""main file"""

from typing import Annotated

from fastapi import APIRouter, Depends, FastAPI
from sqlalchemy.orm import Session

from src import deps
from src.crud.crud_location_data import location_data
from src.schemas.location import LocationInsert

app = FastAPI(title="Location collection and querying", openapi_url="/openapi.json")
router = APIRouter()


@router.get("/", status_code=200)
async def root():
    """root method

    Returns
    -------
    str
        generic msg
    """
    return {"message": "Hello World"}


@router.post("/", status_code=201)
async def collect(
    *, loc_in: LocationInsert, db: Annotated[Session, Depends(deps.get_db)]
):
    location_data.create(_db=db, obj_in=loc_in)
    print(loc_in)


app.include_router(router=router)
