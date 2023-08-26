"""main file"""

from fastapi import APIRouter, FastAPI

from src.api.v1.api import v1_router
from src.core.config import config

app = FastAPI(title="Location collection and querying", openapi_url="/openapi.json")
root_router = APIRouter()


@root_router.get("/", status_code=200)
async def root():
    """root method

    Returns
    -------
    str
        generic msg
    """
    return {"message": "Hello World"}


app.include_router(router=root_router)
app.include_router(router=v1_router, prefix=config.API_V1_STR)
