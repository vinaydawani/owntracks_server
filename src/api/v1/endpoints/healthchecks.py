"""Healthcheck related endpoints"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
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
    try:
        db.execute(text("SELECT 1"))
    except Exception as exc:
        raise HTTPException(status_code=404, detail=exc)
    # TODO: Check if db is healthy and working fine
