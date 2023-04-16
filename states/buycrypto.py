from aiogram.dispatcher.filters.state import StatesGroup, State

class Buy(StatesGroup):
    crypto = State()