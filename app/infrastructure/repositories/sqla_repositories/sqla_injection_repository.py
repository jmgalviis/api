from datetime import datetime

from sqlalchemy import func

from app.domain.models import Injection, Record
from app.domain.repository import InjectionRepository


class SQLAInjectionRepository(InjectionRepository):
    def __init__(self, db):
        self._db = db

    def get_sum_by_client_id_and_date(self, client_id: int, start_date: datetime, end_date: datetime):
        return self._db.query(func.sum(Injection.value))\
            .join(Record, Record.id_record == Injection.id_record)\
            .filter(Record.id_service == client_id, Record.record_timestamp.between(start_date, end_date)).scalar() or 0

    def get_sum_by_client_id(self, client_id: int):
        return self._db.query(func.sum(Injection.value))\
            .join(Record, Record.id_record == Injection.id_record)\
            .filter(Record.id_service == client_id).scalar() or 0

    def get_data_by_client_id_and_date(self, client: int, start_date: datetime, end_date: datetime) -> dict:
        result = (
            self._db.query(Injection.value, Record.record_timestamp)
            .join(Record, Injection.id_record == Record.id_record)
            .filter(
                Record.id_service == client,
                Record.record_timestamp.between(start_date, end_date)
            )
            .all()
        )
        result_dicts = [{"value": row[0], "record_timestamp": row[1]} for row in result]

        return result_dicts