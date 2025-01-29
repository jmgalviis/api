from sqlalchemy import Column, Integer, Float, ForeignKey

from app.infrastructure.database import Base


class Consumption(Base):
    __tablename__ = 'consumption'

    id_record = Column(Integer, ForeignKey('records.id_record'), primary_key=True)
    value = Column(Float)
