from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.application.use_case.consumption_use_case import ConsumptionUseCase
from app.application.use_case.invoice_use_case import InvoiceUseCase
from app.application.use_case.system_load_use_case import SystemLoadUseCase
from app.domain.schema import InvoiceRequest
from app.infrastructure.database import get_db, SessionLocal
from app.infrastructure.repositories.sqla_repositories.sqla_consumption_repository import SQLAConsumptionRepository
from app.infrastructure.repositories.sqla_repositories.sqla_injection_repository import SQLAInjectionRepository
from app.infrastructure.repositories.sqla_repositories.sqla_service_repository import SQLAServiceRepository
from app.infrastructure.repositories.sqla_repositories.sqla_tariffs_repository import SQLATariffsRepository
from app.infrastructure.repositories.sqla_repositories.sqla_xmdatahourly_per_agent_repository import \
    SQLAXMDataHourlyPerAgentRepository

router = APIRouter()

@router.post(
    "/calculate-invoice",
    summary="Calcular factura",
    description="Genera una factura para un cliente en base al mes especificado y el consumo/inyección registrado.",
    response_model=dict,
    responses={
        200: {"description": "Factura calculada correctamente."},
        400: {"description": "Error en los datos proporcionados."},
        500: {"description": "Error interno del servidor."},
    },
)
def calculate_invoice(request: InvoiceRequest, db: Session = Depends(get_db)):
    """
        Endpoint para calcular la factura de un cliente.

        - **month**: Mes en formato YYYY-MM.
        - **client_id**: ID del cliente para el cálculo.
    """
    invoice_use_case = InvoiceUseCase(
        service_repository=SQLAServiceRepository(db),
        tariffs_repository=SQLATariffsRepository(db),
        injection_repository=SQLAInjectionRepository(db),
        consumption_repository=SQLAConsumptionRepository(db),
        xm_data_hourly_per_agent_repository=SQLAXMDataHourlyPerAgentRepository(db)
    )
    try:
        invoice = invoice_use_case.create_invoice(request.month, request.client_id)
        return invoice
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/client-statistics/{client_id}",
    summary="Obtener estadísticas del cliente",
    description="Devuelve las estadísticas de consumo e inyección de un cliente específico.",
    response_model=dict,
    responses={
        200: {"description": "Estadísticas obtenidas correctamente."},
        500: {"description": "Error interno del servidor."},
    },
)
def client_statistics(client_id: int, db: Session = Depends(get_db)):
    """
        Endpoint para obtener las estadísticas de un cliente.

        - **client_id**: ID del cliente.
    """
    consumption_use_case = ConsumptionUseCase(
        consumption_repository=SQLAConsumptionRepository(db),
        injection_repository=SQLAInjectionRepository(db)
    )
    try:
        return consumption_use_case.get_consumption(client_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/system-load",
    summary="Obtener carga del sistema",
    description="Devuelve la carga horaria del sistema para el rango disponible.",
    response_model=dict,
    responses={
        200: {"description": "Carga del sistema obtenida correctamente."},
        500: {"description": "Error interno del servidor."},
    },
)
def system_load():
    """
        Endpoint para obtener la carga horaria del sistema.
    """
    session = SessionLocal()
    system_load_use_case = SystemLoadUseCase(SQLAXMDataHourlyPerAgentRepository(session))
    try:
        return system_load_use_case.get_hourly_load()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()

