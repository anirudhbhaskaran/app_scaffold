from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # App
    app_name: str = "Backend API"
    debug: bool = False

    # MongoDB
    mongodb_url: str = "mongodb://admin:admin_secret@localhost:27017/maindb?authSource=admin"
    mongodb_db: str = "maindb"

    # Redis
    redis_url: str = "redis://:admin_secret@localhost:6379/0"

    # Keycloak / Auth
    keycloak_url: str = "http://localhost:8080"
    keycloak_realm: str = "app"
    keycloak_client_id: str = "app-api"

    # Vault
    vault_url: str = "http://localhost:8200"

    # Anthropic
    anthropic_api_key: str = ""

    # Stripe
    stripe_secret_key: str = ""
    stripe_webhook_secret: str = ""

    # Resend
    resend_api_key: str = ""

    # CORS
    cors_origins: list[str] = ["http://localhost:3000"]


settings = Settings()
