from aiogram import Bot, Dispatcher
from aiogram.types import ContentType
from sqlalchemy import URL

from core.handlers.basic import get_start, get_webapp
from core.settings import settings
import asyncio
import logging
from aiogram import F
from aiogram.filters import Command, CommandStart
from core.db import BaseModel, create_async_engine, get_session_maker, proceed_schemas


async def start():
    dp = Dispatcher()
    logging.basicConfig(level=logging.INFO, )
    bot = Bot(token=settings.bots.bot_token)

    dp.message.register(get_start, CommandStart())
    dp.message.register(get_webapp, F.content_type == ContentType.WEB_APP_DATA)

    postgres_ulr = URL.create(
        'postgresql+asyncpg',
        username=settings.db_connects.username,
        password=settings.db_connects.password,
        host=settings.db_connects.host,
        port=settings.db_connects.port,
        database=settings.db_connects.name
    )

    async_engine = create_async_engine(postgres_ulr)
    session_maker = get_session_maker(async_engine)

    await proceed_schemas(async_engine, BaseModel.metadata)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
