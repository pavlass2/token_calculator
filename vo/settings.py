import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_KEY_HEADER: str = "X-API-KEY"
    API_KEY_VALUE: str = os.environ.get("API_KEY")
