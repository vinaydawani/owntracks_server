from datetime import datetime

from sqlalchemy import Column, DateTime, Double, Float, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY

from src.db.base_class import Base


class LocationData(Base):
    __tablename__ = "general_loc_data"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    acc = Column(Integer(), nullable=True)
    alt = Column(Integer(), nullable=True)
    batt = Column(Integer(), nullable=True)
    bs = Column(Integer(), nullable=True)
    cog = Column(Integer(), nullable=True)
    lat = Column(Double())
    lon = Column(Double())
    rad = Column(Integer(), nullable=True)
    t = Column(String(2), nullable=True)
    tid = Column(String())
    tst = Column(Integer())
    vac = Column(Integer(), nullable=True)
    vel = Column(Integer(), nullable=True)
    p = Column(Float(), nullable=True)
    poi = Column(String(), nullable=True)
    conn = Column(String(2), nullable=True)
    tag = Column(String(), nullable=True)
    topic = Column(String(255), nullable=True)
    inregions = Column(ARRAY(String), nullable=True)
    inrids = Column(ARRAY(String), nullable=True)
    SSID = Column(String(), nullable=True)
    BSSID = Column(String(), nullable=True)
    created_at = Column(Integer(), nullable=True)
    created_on = Column(DateTime(), default=datetime.now)
    m = Column(Integer(), nullable=True)
