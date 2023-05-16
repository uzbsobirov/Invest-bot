from keyboards.inline.apply import apply
from loader import dp

from aiogram import types
from aiogram.dispatcher import FSMContext

from language import i18n

_ = i18n.gettext


@dp.message_handler(text=_("☎️ Murojaat uchun"), state='*')
async def apply_to_admin(message: types.Message, state: FSMContext):

    text = _("<b>Murojaat uchun admin_panel👇</b>")
    await message.answer(text=text, reply_markup=apply)
    await state.finish()