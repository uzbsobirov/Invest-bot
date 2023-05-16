from loader import dp, db

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text="uz", state='*')
async def uz_lang(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    await call.answer(text="🇺🇿 O'zbek tili tanlandi", cache_time=3)

    await db.update_user_language(lang='uz', user_id=user_id)



@dp.callback_query_handler(text="ru", state='*')
async def uz_lang(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    await call.answer(text="🇷🇺 Выбран русский язык", cache_time=3)

    await db.update_user_language(lang='ru', user_id=user_id)
