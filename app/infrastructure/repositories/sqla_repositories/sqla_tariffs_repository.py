from app.domain.models import Tariff
from app.domain.repository import TariffsRepository


class SQLATariffsRepository(TariffsRepository):
    def __init__(self, db):
        self._db = db

    def get_by_id_market(self, id_market: int):
        return self._db.query(Tariff).filter(Tariff.id_market == id_market).first()