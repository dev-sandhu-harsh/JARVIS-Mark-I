from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "JARVIS"
    enviornment: str = "dev"
    version: str = "Mark-I"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
