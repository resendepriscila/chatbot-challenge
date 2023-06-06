from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    chatgpt_api_token: str
    ttl_time_out: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    return Settings()
