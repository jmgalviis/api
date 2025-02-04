from app.core.utils import get_month_range
from app.domain.repository import ServiceRepository, TariffsRepository, InjectionRepository, ConsumptionRepository, \
    XMDataHourlyPerAgentRepository


class InvoiceUseCase:
    def __init__(
            self,
            service_repository: ServiceRepository,
            tariffs_repository: TariffsRepository,
            injection_repository: InjectionRepository,
            consumption_repository: ConsumptionRepository,
            xm_data_hourly_per_agent_repository: XMDataHourlyPerAgentRepository
    ):
        self._service_repository = service_repository
        self._tariffs_repository = tariffs_repository
        self._injection_repository = injection_repository
        self._consumption_repository = consumption_repository
        self._xm_data = xm_data_hourly_per_agent_repository

    def create_invoice(self, month, client_id) -> dict:
        start_date, end_date = get_month_range(month)
        service = self._service_repository.get_by_id(id_service=client_id)
        consumption_sum = self._consumption_repository.get_sum_by_client_id_and_date(client_id, start_date, end_date)
        injection_sum = self._injection_repository.get_sum_by_client_id_and_date(client_id, start_date, end_date)
        injections = self._injection_repository.get_data_by_client_id_and_date(client_id, start_date, end_date)
        tariffs = self._tariffs_repository.get_by_id_market(service)
        if not tariffs:
            raise ValueError(f'No tariff found for the client {service.id_market}')
        ea = consumption_sum

        ea_total = consumption_sum * tariffs.cu
        ec_total = injection_sum * tariffs.c
        if injection_sum <= consumption_sum:
            ee1 = injection_sum * (-tariffs.cu)
        else:
            ee1 = consumption_sum * (-tariffs.cu)
        if injection_sum <= consumption_sum:
            ee2 = 0.0
        else:
            sumar = 0.0
            exceso_total = 0.0
            for injection in injections:
                sumar = sumar + injection.get('value')
                if sumar > ea:
                    exceso_inicio = sumar - ea
                    xm_data_value = self._xm_data.get_data_by_client_id(client_id, injection.get('record_timestamp'))
                    multiplicar = exceso_inicio * xm_data_value.get('value')
                    exceso_total = exceso_total + multiplicar
            ee2 = exceso_total
        return {
            "EA": ea_total,
            "EC": ec_total,
            "EE1": ee1,
            "EE2": ee2,
        }