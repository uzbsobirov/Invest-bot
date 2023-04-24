from aiogram.dispatcher.filters.state import StatesGroup, State

class Buy(StatesGroup):
    crypto = State()
    photo = State()
    checking = State()
    money = State()

class EveryDay(StatesGroup):
    paytime = State()