from app.domain.models import Service
from app.domain.repository import ServiceRepository
from app.infrastructure.database import SessionLocal


class SQLAServiceRepository(ServiceRepository):
    def __init__(self, db):
        self._db = db

    def get_by_id(self, id_service: int):
        return self._db.query(Service).filter(id_service == id_service).first()
