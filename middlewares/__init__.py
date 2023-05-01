from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .check_subs import BigBrother


if __name__ == "middlewares":
    dp.middleware.setup(BigBrother())
    dp.middleware.setup(ThrottlingMiddleware())

