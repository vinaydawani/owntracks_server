from datetime import datetime

from sqlalchemy import Column, DateTime, Double, Float, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY

from src.db.base_class import Base


class LocationData(Base):
    __tablename__ = "general_loc_data"

    id: Column(Integer, primary_key=True, autoincrement="auto")
    accuracy_m = Column(Integer(), nullable=True)
    altitude_m = Column(Integer(), nullable=True)
    battery_per = Column(Integer(), nullable=True)
    battery_status = Column(Integer(), nullable=True)
    course_over_ground = Column(Integer(), nullable=True)
    latitude = Column(Double())
    longitude = Column(Double())
    radius_m = Column(Integer(), nullable=True)
    trigger = Column(String(2), nullable=True)
    tracker_id = Column(String())
    timestamp = Column(Integer())
    vertical_accuracy_m = Column(Integer(), nullable=True)
    velocity_kmh = Column(Integer(), nullable=True)
    barometric_pressure_kpa = Column(Float(), nullable=True)
    poi_name = Column(String(), nullable=True)
    conn = Column(String(2), nullable=True)
    tag = Column(String(), nullable=True)
    topic = Column(String(255), nullable=True)
    inregions = Column(ARRAY(String), nullable=True)
    inrids = Column(ARRAY(String), nullable=True)
    SSID = Column(String(), nullable=True)
    BSSID = Column(String(), nullable=True)
    created_at = Column(DateTime(), nullable=True)
    created_on = Column(DateTime(), default=datetime.now)
    monitoring_mode = Column(Integer(), nullable=True)
