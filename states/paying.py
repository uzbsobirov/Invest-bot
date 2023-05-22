from aiogram.dispatcher.filters.state import StatesGroup, State


class Pay(StatesGroup):
    id = State()
    crypto = State()
    money = State()


class PayTime(StatesGroup):
    id = State()
    money = State()
