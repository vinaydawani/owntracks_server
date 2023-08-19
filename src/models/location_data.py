"""Table model to store location data generically. _type=location"""

from datetime import datetime

from sqlalchemy import DateTime, Double, Float, Integer, String
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import ARRAY

from src.db.base_class import Base


class Location(Base):
    """Location class inheriting from base. Declares all the columns"""

    id = mapped_column(Integer, primary_key=True, autoincrement="auto")
    acc = mapped_column(Integer(), nullable=True)
    alt = mapped_column(Integer(), nullable=True)
    batt = mapped_column(Integer(), nullable=True)
    bs = mapped_column(Integer(), nullable=True)
    cog = mapped_column(Integer(), nullable=True)
    lat = mapped_column(Double())
    lon = mapped_column(Double())
    rad = mapped_column(Integer(), nullable=True)
    t = mapped_column(String(2), nullable=True)
    tid = mapped_column(String())
    tst = mapped_column(Integer())
    vac = mapped_column(Integer(), nullable=True)
    vel = mapped_column(Integer(), nullable=True)
    p = mapped_column(Float(), nullable=True)
    poi = mapped_column(String(), nullable=True)
    conn = mapped_column(String(2), nullable=True)
    tag = mapped_column(String(), nullable=True)
    topic = mapped_column(String(255), nullable=True)
    inregions = mapped_column(ARRAY(String), nullable=True)
    inrids = mapped_column(ARRAY(String), nullable=True)
    SSID = mapped_column(String(), nullable=True)
    BSSID = mapped_column(String(), nullable=True)
    created_at = mapped_column(Integer(), nullable=True)
    created_on = mapped_column(DateTime(), default=datetime.now)
    m = mapped_column(Integer(), nullable=True)
