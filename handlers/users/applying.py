from keyboards.inline.apply import apply
from loader import dp

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="🆘 Murojaat uchun admin_panel", state='*')
async def apply_to_admin(message: types.Message, state: FSMContext):

    text = "<b>Murojaat uchun admin_panel👇</b>"
    await message.answer(text=text, reply_markup=apply)
    await state.finish()