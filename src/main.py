"""main file"""

from fastapi import APIRouter, FastAPI

from src.schema import LocationData

app = FastAPI(title="Location collection and querying", openapi_url="/openapi.json")
router = APIRouter()


@router.get("/", status_code=200)
async def root():
    return {"message": "Hello World"}


@router.post("/", status_code=201)
async def collect(*, request: LocationData):
    # zz = await request.body()
    print(request)


app.include_router(router=router)
