from typing import Union
from aiogram import Bot


async def check_is_admin(channel: Union[str, int]):
    bot = Bot.get_current()
    member = await bot.get_chat_administrators(chat_id=channel)
    return member