from loader import dp, db

from aiogram.dispatcher import FSMContext
from aiogram import types

@dp.message_handler(text="💰 Balans", state='*')
async def uer_balance(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    select_user = await db.select_one_user(user_id=user_id)
    input_money = select_user[0][6]
    crypto = select_user[0][4]
    percent = select_user[0][7]

    text = f"💰 Kiritgan summa: {input_money}\n🔹 Kriptovalyuta: {crypto}\n⏳ Kunlik foiz: {percent}"
    await message.answer(text=text)
