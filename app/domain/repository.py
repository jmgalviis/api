from abc import ABCMeta, abstractmethod
from datetime import datetime


class ServiceRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_by_id(self, id_service: int):
        pass

class ConsumptionRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_sum_by_client_id_and_date(self, client_id: int, start_date: datetime, end_date: datetime):
        pass

    @abstractmethod
    def get_sum_by_client_id(self, client_id: int):
        pass

class InjectionRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_sum_by_client_id_and_date(self, client_id: int, start_date: datetime, end_date: datetime):
        pass

    @abstractmethod
    def get_sum_by_client_id(self, client_id: int):
        pass

class TariffsRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_by_id_market(self, id_market: int):
        pass

class XMDataHourlyPerAgentRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_hourly_load(self):
        pass
