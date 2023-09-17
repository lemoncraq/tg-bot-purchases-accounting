from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import reply_keyboard, inline_kb
from core.utils.info_from_check import check_request
from core.settings import settings


async def get_start(message: Message, bot: Bot):
    # await bot.send_message(message.chat.id, '', reply_markup=inline_kb)
    await message.answer('Scan ur qr', reply_markup=reply_keyboard)


async def get_webapp(message: Message):
    data = {'token': settings.connects.api_token, 'qrraw': message.web_app_data.data}
    check_data = check_request(data)
    print(check_data)
    await message.answer(message.web_app_data.data)
