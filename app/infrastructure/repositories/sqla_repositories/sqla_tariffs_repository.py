from app.domain.models import Tariff, Service
from app.domain.repository import TariffsRepository


class SQLATariffsRepository(TariffsRepository):
    def __init__(self, db):
        self._db = db

    def get_by_id_market(self, service: Service):
        if service.voltage_level > 1:
            return self._db.query(Tariff).filter(
                Tariff.id_market == service.id_market,
                Tariff.voltage_level == service.voltage_level,
            ).first()
        return self._db.query(Tariff).filter(
            Tariff.id_market == service.id_market,
            Tariff.cdi == service.cdi,
            Tariff.voltage_level == service.voltage_level
        ).first()
