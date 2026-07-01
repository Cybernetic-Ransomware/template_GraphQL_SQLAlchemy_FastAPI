from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Database backend configuration, see .env.template for the supported modes."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    database_url: str = "sqlite:///./test.db"
    turso_auth_token: str | None = None
    turso_sync_url: str | None = None


settings = Settings()
