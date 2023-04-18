from loader import dp, db, bot

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="🔗 Referal", state='*')
async def start_deep_link(message: types.Message, state: FSMContext):
    pass