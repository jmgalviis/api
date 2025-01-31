from sqlalchemy import func

from app.domain.models import XMDataHourlyPerAgent, Record, Consumption
from app.domain.repository import XMDataHourlyPerAgentRepository


class SQLAXMDataHourlyPerAgentRepository(XMDataHourlyPerAgentRepository):
    def __init__(self, db):
        self._db = db

    def get_hourly_load(self) -> dict:
        try:
            hourly_load = self._db.query(XMDataHourlyPerAgent.record_timestamp, func.sum(Consumption.value))\
                .join(Record, Record.record_timestamp == XMDataHourlyPerAgent.record_timestamp)\
                .group_by(XMDataHourlyPerAgent.record_timestamp).all()
            return {"hourly_load": [{"timestamp": record[0], "load": record[1]} for record in hourly_load]}
        except Exception as e:
            print(f"Error retrieving hourly load: {e}")
            return {"hourly_load": []}