from sqlalchemy import Column, Integer, Float, PrimaryKeyConstraint, ForeignKeyConstraint

from app.infrastructure.database import Base


class Tariff(Base):
    __tablename__ = 'tariffs'

    id_market = Column(Integer, nullable=False)
    cdi = Column(Integer, nullable=False)
    voltage_level = Column(Integer, nullable=False)
    g = Column(Float)
    t = Column(Float)
    d = Column(Float)
    r = Column(Float)
    c = Column(Float)
    p = Column(Float)
    cu = Column(Float)

    __table_args__ = (
        PrimaryKeyConstraint('id_market', 'cdi', 'voltage_level', name='pk_tariffs'),
        ForeignKeyConstraint(['id_market', 'cdi', 'voltage_level'],
                             ['services.id_market', 'services.cdi', 'services.voltage_level']),
    )
