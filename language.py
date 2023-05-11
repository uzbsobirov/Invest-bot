from pathlib import Path
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

        user_data = db.select_user(user_id=user.id)
        # print(user_data)
        if user_data is None:
            db.add_user_lang(full_name=user.full_name, username=user.username, user_id=user.id, lang='ru')
            # LANG_STORAGE[user.id] = "en"
        *_, data = args
        language = data['locales'] = db.get_lang(user_id=user.id)[0]

        return language


# Setup i18n middleware
i18n = Localization(I18N_DOMAIN, LOCALES_DIR)
dp.middleware.setup(i18n)