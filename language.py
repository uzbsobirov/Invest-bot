import logging
from pathlib import Path

import asyncpg
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from typing import Tuple, Any
from aiogram import types
from loader import dp, db

BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / "locales"

# LANG_STORAGE = {}
LANGS = ["ru", "uz"]
I18N_DOMAIN = "mybot"


class Localization(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        """
        User locales getter
        You can override the method if you want to use different way of getting user language.
        :param action: event name
        :param args: event arguments
        :return: locales name
        """
        user: types.User = types.User.get_current()

        user_data = await db.select_user_lang(user_id=int(user.id))
        if user_data is None or user_data == []:
            try:
                await db.add_user_lang(full_name=user.full_name, username=user.username, user_id=int(user.id),
                                       lang='null')
            except asyncpg.exceptions.UniqueViolationError as uve:
                logging.info(uve)

        *_, data = args
        user_lang = (await db.get_lang(user_id=int(user.id)))[0][0]
        language = user_lang
        return language


# Setup i18n middleware
i18n = Localization(I18N_DOMAIN, LOCALES_DIR)
dp.middleware.setup(i18n)