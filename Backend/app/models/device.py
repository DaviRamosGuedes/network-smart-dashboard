from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime, timezone

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String)
    mac = Column(String, unique=True, index=True)
    hostname = Column(String)
    status = Column(String)
    last_seen = Column(DateTime, default=datetime.now(timezone.utc))