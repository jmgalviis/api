from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.infrastructure.api.router import router
from app.infrastructure.database import engine, Base

app = FastAPI(
    title="API ERCO",
    description="API for ERCO",
    version="1.0.0",
    contact={
        "name": "Juan Manuel Galvis",
        "email": "jmgalviis@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(router, prefix="/api/v1", tags=["api"])
