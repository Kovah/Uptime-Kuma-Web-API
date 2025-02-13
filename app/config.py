from pydantic import AnyHttpUrl, BaseSettings
from typing import List
import secrets
import logging
import os

logger = logging.getLogger("uvicorn.error")
access_token_expire_default = 60 * 24 * 8 #8 days

class Settings(BaseSettings):
    PROJECT_NAME: str="Uptime-Kuma-API"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    
    ACCESS_TOKEN_EXPIRE: int = int(os.environ.get('ACCESS_TOKEN_EXPIRE') or access_token_expire_default)
    SECRET_KEY: str = secrets.token_urlsafe(32)

    KUMA_SERVER: str = os.environ.get('KUMA_SERVER')
    KUMA_USERNAME: str = os.environ.get('KUMA_USERNAME')
    KUMA_PASSWORD: str = os.environ.get('KUMA_PASSWORD')

    ADMIN_PASSWORD: str = os.environ.get('ADMIN_PASSWORD')


    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()