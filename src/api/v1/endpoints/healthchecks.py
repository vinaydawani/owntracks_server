"""Healthcheck related endpoints"""

from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from src.api import deps

router = APIRouter()


@router.get("/db", status_code=200)
async def check_db_health(*, db: Annotated[Session, Depends(deps.get_db)]):
    """Checks the health of the database and returns the status.

    Parameters
    ----------
    db : Annotated[Session, Depends
        Injecting the database and usuing it
    """
    db.execute(text("SELECT 1"))
    # TODO: Check if db is healthy and working fine
