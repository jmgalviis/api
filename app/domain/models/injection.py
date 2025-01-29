from sqlalchemy import Integer, ForeignKey, Column, Float

from app.infrastructure.database import Base


class Injection(Base):
    __tablename__ = 'injection'

    id_record = Column(Integer, ForeignKey('records.id_record'), primary_key=True)
    value = Column(Float)
