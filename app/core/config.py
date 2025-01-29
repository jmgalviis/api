from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    import os

    ENV = os.getenv("ENV", "testing")

    if ENV == "testing":
        DATABASE_URL = "sqlite://"
    else:
        DATABASE_URL = "postgresql://user:password@localhost/library_db"

    class Config:
        env_file = ".env"


settings = Settings()
