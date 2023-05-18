from typing import Optional, List

from pydantic import BaseModel, Field

class LocationData(BaseModel):
    _type: str = Field(default=None)
    acc: Optional[int] = Field(default=None)
    alt: Optional[int] = Field(default=None)
    batt: Optional[int] = Field(default=None)
    bs: int = Field(default=None)
    cog: Optional[int] = Field(default=None)
    lat: float = Field(default=None)
    lon: float = Field(default=None)
    rad: Optional[int] = Field(default=None)
    t: Optional[str] = Field(default=None)
    tid: str = Field(default=None)
    tst: int = Field(default=None)
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

    