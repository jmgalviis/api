from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP

from app.infrastructure.database import Base


class Record(Base):
    __tablename__ = 'records'

    id_record = Column(Integer, primary_key=True)
    id_service = Column(Integer, nullable=False)
    record_timestamp = Column(TIMESTAMP, ForeignKey('xm_data_hourly_per_agent.record_timestamp'), nullable=False)

