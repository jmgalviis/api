from sqlalchemy import Column, Float, TIMESTAMP

from app.infrastructure.database import Base


class XMDataHourlyPerAgent(Base):
    __tablename__ = "xm_data_hourly_per_agent"

    value = Column(Float)
    record_timestamp = Column(TIMESTAMP, unique=True, primary_key=True)
