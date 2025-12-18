from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GEMINI_API_KEY: str = Field(alias="GOOGLE_API_KEY")
    GEMINI_MODEL: str = Field(alias="GOOGLE_API_MODEL")
    GEMINI_TEMPERATURE: float = Field(alias="TEMPERATURE")


    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()
