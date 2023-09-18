from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, InlineKeyboardButton, \
    InlineKeyboardMarkup, WebAppInfo
from core.settings import settings


reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Scan', web_app=WebAppInfo(url=settings.api_connects.webapp_url)
        )
    ]
])

inline_btn = InlineKeyboardButton(text='Open scanner', web_app=WebAppInfo(url=settings.api_connects.webapp_url))
inline_kb = InlineKeyboardMarkup(inline_keyboard=[[inline_btn]])