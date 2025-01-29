from pydantic import BaseModel


class InvoiceRequest(BaseModel):
    client_id: int
    month: str