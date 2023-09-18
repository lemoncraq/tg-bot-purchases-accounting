from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: int


@dataclass
class ApiConnects:
    webapp_url: str
    api: str
    api_token: str


@dataclass
class DbConnects:
    username: str
    password: str
    host: str
    name: str
    port: int


@dataclass
class Settings:
    bots: Bots
    api_connects: ApiConnects
    db_connects: DbConnects


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("TOKEN"), admin_id=env.int("ADMIN_ID")
        ),
        api_connects=ApiConnects(
            webapp_url=env.str("WEBAPP_URL"), api=env.str("API"), api_token=env.str("API_TOKEN")
        ),
        db_connects=DbConnects(
            username=env.str("USERNAME"), password=env.str("PASSWORD"),
            host=env.str("HOST"), name=env.str("NAME"), port=env.int("PORT")
        )
    )


settings = get_settings('input')
