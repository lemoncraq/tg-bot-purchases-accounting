from aiogram import Bot, Dispatcher
from aiogram.types import ContentType

from core.handlers.basic import get_start, get_webapp
from core.settings import settings
import asyncio
import logging
from aiogram import F
from aiogram.filters import Command, CommandStart


async def start():
    dp = Dispatcher()
    logging.basicConfig(level=logging.INFO, )
    bot = Bot(token=settings.bots.bot_token)

    dp.message.register(get_start, CommandStart())
    dp.message.register(get_webapp, F.content_type == ContentType.WEB_APP_DATA)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
