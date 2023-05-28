from typing import Any, List

from pydantic import BaseModel

# class LocationData(BaseModel):
#     acc: Optional[int] = Field(default=None)


class LocationBase(BaseModel):
    _type: str
    bs: int
    lat: float
    lon: float
    tid: str
    tst: int


class LocationOptionals(BaseModel):
    acc: int | None
    alt: int | None
    batt: int | None
    cog: int | None
    rad: int | None
    t: str | None
    vac: int | None
    vel: int | None
    p: float | None
    poi: str | None
    conn: str | None
    tag: str | None
    topic: str | None
    inregions: List[str] | None
    inrids: List[str] | None
    SSID: str | None
    BSSID: str | None
    created_at: Any | None
    m: int | None


class LocationInsert(LocationBase, LocationOptionals):
    pass


class LocationData(LocationBase, LocationOptionals):
    ...
