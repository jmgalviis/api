from app.domain.repository import ConsumptionRepository, InjectionRepository


class ConsumptionUseCase:
    def __init__(
            self,
            consumption_repository: ConsumptionRepository,
            injection_repository: InjectionRepository
    ):
        self._consumption_repository = consumption_repository
        self._injection_repository = injection_repository

    def get_consumption(self, client_id: int) -> dict:
        consumption_sum = self._consumption_repository.get_sum_by_client_id(client_id)
        injection_sum = self._injection_repository.get_sum_by_client_id(client_id)
        return {
            "total_consumption": consumption_sum,
            "total_injection": injection_sum
        }
