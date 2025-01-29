import pytest
from datetime import datetime
from fastapi import status
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.domain.models import Service, Tariff, Record, Injection, Consumption, XMDataHourlyPerAgent
from app.domain.schema import InvoiceRequest


# Fixture para crear datos de prueba
@pytest.fixture
def setup_data(db_session: Session):
    # Crear un servicio
    service = Service(id_service=1, id_market=1, cdi=1, voltage_level=1)
    db_session.add(service)

    # Crear una tarifa
    tariff = Tariff(id_market=1, cdi=1, voltage_level=1, cu=0.1, c=0.05)
    db_session.add(tariff)

    # Crear un registro
    record = Record(id_record=1, id_service=1, record_timestamp=datetime(2023, 10, 1, 0, 0))
    db_session.add(record)

    # Crear un consumo
    consumption = Consumption(id_record=1, value=100)
    db_session.add(consumption)

    # Crear una inyección
    injection = Injection(id_record=1, value=50)
    db_session.add(injection)

    xm_data = XMDataHourlyPerAgent(
        record_timestamp=datetime(2023, 10, 1, 0, 0),
        value=100.0
    )
    db_session.add(xm_data)

    record = Record(
        id_record=2,
        id_service=1,
        record_timestamp=datetime(2023, 10, 1, 0, 0)
    )
    db_session.add(record)

    db_session.commit()


def test_calculate_invoice(client, setup_data):
    invoice_request = InvoiceRequest(month="2023-10", client_id=1)
    response = client.post("/api/v1/calculate-invoice", json=invoice_request.dict())
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "EA": 10.0,
        "EC": 2.5,
        "EE1": -5.0,
        "EE2": 0.0,
    }



def test_client_statistics(client, setup_data):
    response = client.get("/api/v1/client-statistics/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "total_consumption": 100,
        "total_injection": 50,
    }


def test_system_load(client, setup_data):
    response = client.get("/api/v1/system-load")
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    assert "hourly_load" in response_data
    assert isinstance(response_data["hourly_load"], list)

def test_table_creation(db_session):
    # Usa text() para envolver la consulta en SQL textual
    tables = db_session.execute(
        text("SELECT name FROM sqlite_master WHERE type='table';")
    ).fetchall()
    table_names = [table[0] for table in tables]
    assert "xm_data_hourly_per_agent" in table_names
    assert "records" in table_names
    assert "consumption" in table_names