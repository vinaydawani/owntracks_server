from typing import List, Optional

from pydantic import BaseModel, Field

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
    acc: Optional[int] = Field(default=None)
    alt: Optional[int] = Field(default=None)
    batt: Optional[int] = Field(default=None)
    cog: Optional[int] = Field(default=None)
    rad: Optional[int] = Field(default=None)
    t: Optional[str] = Field(default=None)
    vac: Optional[int] = Field(default=None)
    vel: Optional[int] = Field(default=None)
    p: Optional[float] = Field(default=None)
    poi: Optional[str] = Field(default=None)
    conn: Optional[str] = Field(default=None)
    tag: Optional[str] = Field(default=None)
    topic: Optional[str] = Field(default=None)
    inregions: Optional[List[str]] = Field(default=None)
    inrids: Optional[List[str]] = Field(default=None)
    SSID: Optional[str] = Field(default=None)
    BSSID: Optional[str] = Field(default=None)
    created_at: Optional[int] = Field(default=None)
    m: Optional[int] = Field(default=None)


class LocationInsert(LocationBase, LocationOptionals):
    class Config:
        orm_mode = True


class LocationData(LocationBase, LocationOptionals):
    ...
