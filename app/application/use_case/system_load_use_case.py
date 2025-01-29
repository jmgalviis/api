from app.domain.repository import XMDataHourlyPerAgentRepository


class SystemLoadUseCase:
    def __init__(self, data_hour_repository: XMDataHourlyPerAgentRepository):
        self._repository = data_hour_repository

    def get_hourly_load(self):
        return self._repository.get_hourly_load()