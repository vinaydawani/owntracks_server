from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import Response
from sqlalchemy.orm import Session

from src.api import deps
from src.crud.crud_location_data import location_data
from src.schemas.cmd import CmdBase
from src.schemas.location import LocationInsert

router = APIRouter()


@router.post("/", status_code=201)
async def collect(
    *,
    loc_in: LocationInsert | CmdBase,
    db: Annotated[Session, Depends(deps.get_db)],
    req: Request
):
    """Endpoint to collect all the data published through owntracks clients
    """
    # Pydantic v1 models don't pick up protected variables so "_type" needs to be
    # extracted from request body and assigned manually
    _type = (await req.json())["_type"]

    if _type == "cmd" and loc_in.action == "reportLocation":
        return Response(status_code=status.HTTP_200_OK)

    if _type != "location":
        raise HTTPException(status_code=400, detail="Not a valid location publish")

    location_data.create(_db=db, obj_in=loc_in)
