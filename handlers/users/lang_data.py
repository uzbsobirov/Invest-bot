from loader import dp

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text="uz", state='*')
async def uz_lang(call: types.CallbackQuery, state: FSMContext):
    print(call.data)

@dp.callback_query_handler(text="ru", state='*')
async def uz_lang(call: types.CallbackQuery, state: FSMContext):
    print(call.data)