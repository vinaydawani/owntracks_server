"""Collection of all endpoints"""

from fastapi import APIRouter

from src.api.v1.endpoints import publish, healthchecks

v1_router = APIRouter()
v1_router.include_router(
    publish.router, prefix="/publish", tags=["publish", "location"]
)
v1_router.include_router(healthchecks.router, prefix="/hc", tags=["Healthcheck"])
