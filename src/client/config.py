from pydantic import BaseSettings


class Settings(BaseSettings):
    TOKEN: str
    UA: str = 'Mozilla/5.0 (Linux; Android 11; motorola one vision Build/RSAS31.Q1-48-36-14; wv) AppleWebKit/537.36 (' \
              'KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74'

    class Config:
        env_file = '.env'


settings = Settings()
