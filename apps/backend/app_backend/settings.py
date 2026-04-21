from pydantic_settings import BaseSettings
from functools import lru_cache


class BaseConfig(BaseSettings):
    # App
    APP_NAME: str = "App Backend"
    DEBUG: bool = False

    # Keycloak
    KEYCLOAK_BASE_URL: str
    KEYCLOAK_REALM: str
    KEYCLOAK_CLIENT_ID: str
    KEYCLOAK_CLIENT_SECRET: str

    # JWT
    JWT_ALGORITHM: str = "RS256"

    # Database
    DATABASE_URL: str

    class Config:
        env_file = ".env"
        case_sensitive = True


class DevelopmentConfig(BaseConfig):
    ENV: str = "dev"
    DEBUG: bool = True


class ProductionConfig(BaseConfig):
    ENV: str = "prod"
    DEBUG: bool = False


@lru_cache()
def get_settings():
    import os

    env = os.getenv("ENV", "dev")

    if env == "prod":
        return ProductionConfig()
    return DevelopmentConfig()


settings = get_settings()