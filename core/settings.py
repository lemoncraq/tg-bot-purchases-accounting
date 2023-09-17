from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: int


@dataclass
class Connects:
    webapp_url: str
    api: str
    api_token: str


@dataclass
class Settings:
    bots: Bots
    connects: Connects


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("TOKEN"), admin_id=env.int("ADMIN_ID")
        ),
        connects=Connects(
            webapp_url=env.str("WEBAPP_URL"), api=env.str("API"),api_token=env.str("API_TOKEN")
        )
    )


settings = get_settings('input')
