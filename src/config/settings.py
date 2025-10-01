from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    api_key: str
    dw_name: str
    dw_user: str
    dw_password: str
    dw_host: str
    dw_port: str

    @computed_field  # type: ignore
    @property
    def db_url(self) -> str:
        # postgresql+drivername://user:password@host:port/database_name
        return f"postgresql+psycopg2://{self.dw_user}:{self.dw_password}@{self.dw_host}:{self.dw_port}/{self.dw_name}"


settings = Settings()
