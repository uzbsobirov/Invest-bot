from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from keyboards.inline.help import help

from language import i18n

_ = i18n.gettext


@dp.message_handler(CommandHelp(), state='*')
async def bot_help(message: types.Message):
    text = _("<b>Agar sizda biror bitta muammo bo'lsa yoki taklifingiz bo'lsa adminga murojaat qiling!</b>")

    await message.answer(text=text, reply_markup=help)
