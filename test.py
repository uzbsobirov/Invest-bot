from pathlib import Path
from typing import Tuple, Any

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.i18n import I18nMiddleware

TOKEN = "5762026535:AAEHgZLyM1iMXR8CFUPFItGFnMZn0YMzDhg"
I18N_DOMAIN = "mybot"

BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / "locales"

bot = Bot(TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


LANG_STORAGE = {}
LANGS = ["ru", "en", "uz"]


class Localization(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        """
        User locale getter
        You can override the method if you want to use different way of getting user language.
        :param action: event name
        :param args: event arguments
        :return: locale name
        """
        user: types.User = types.User.get_current()

        if LANG_STORAGE.get(user.id) is None:
            LANG_STORAGE[user.id] = "en"
        *_, data = args
        language = data['locale'] = LANG_STORAGE[user.id]
        print(language)
        return language


# Setup i18n middleware
i18n = Localization(I18N_DOMAIN, LOCALES_DIR)
dp.middleware.setup(i18n)

# Alias for gettext method
_ = i18n.lazy_gettext


START_KEYBOARD = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(_("One"))],
        [types.KeyboardButton(_("Two"))],
        [types.KeyboardButton(_("Three"))],
    ],
    resize_keyboard=True,
)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer(
        _("Hello, <b>{user}</b>!").format(user=message.from_user.full_name),
        reply_markup=START_KEYBOARD,
    )


@dp.message_handler(commands="lang")
async def cmd_lang(message: types.Message, locale):
    await message.answer(
        _("Your current language: <i>{language}</i>").format(language=locale)
    )


@dp.message_handler(commands="setlang")
async def cmd_setlang(message: types.Message):
    lang = message.get_args()

    if not lang:
        return await message.answer(_("Specify your language.\nExample: /setlang en"))
    if lang not in LANGS:
        return await message.answer(_("This language is not available. Use en or ru"))

    LANG_STORAGE[message.from_user.id] = lang
    print(LANG_STORAGE)

    await message.answer(_("Language set.", locale=lang), reply_markup=START_KEYBOARD)


@dp.message_handler(text=_("One"))
async def text_one(message: types.Message):
    await message.answer(_("Really one"))


@dp.message_handler(text=_("Two"))
async def text_two(message: types.Message):
    await message.answer(_("Really two"))


@dp.message_handler(text=_("Three"))
async def text_three(message: types.Message):
    await message.answer(_("Really three"))


executor.start_polling(dp)