from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_TITLE: str = "Recruitment Website Api"
    PROJECT_VERSION: str = "0.1.1"
    # database_hostname: str
    # database_port: str
    # database_password: str
    # database_name: str
    # database_username: str
    secret_key: str

    class Config:
        env_file = ".env"


settings = Settings()
