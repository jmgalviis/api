from sqlalchemy import Column, Integer, UniqueConstraint

from app.infrastructure.database import Base


class Service(Base):
    __tablename__ = 'services'

    id_service = Column(Integer, primary_key=True)
    id_market = Column(Integer, nullable=False)
    cdi = Column(Integer, nullable=False)
    voltage_level = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint('id_market', 'cdi', 'voltage_level', name='uq_market_cdi_voltage'),
    )
