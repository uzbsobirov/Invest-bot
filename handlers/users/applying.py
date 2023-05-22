from data.config import ADMINS
from keyboards.inline.apply import apply
from loader import dp, bot
from states.apply import Apply

from aiogram import types
from aiogram.dispatcher import FSMContext

from language import i18n

_ = i18n.gettext


@dp.message_handler(text=[_("☎️ Murojaat uchun"), "☎️ Для ознакомления"], state='*')
async def apply_to_admin(message: types.Message, state: FSMContext):

    text = _("<b>Murojaatingizni yozib qoldiring👇</b>")
    await message.answer(text=text)
    await Apply.message.set()


@dp.message_handler(state=Apply.message)
async def get_user_message(message: types.Message, state: FSMContext):
    full_name = message.from_user.full_name
    user_mention = message.from_user.get_mention(name=full_name)
    text = message.text

    await bot.send_message(chat_id=ADMINS[0], text="{} -- dan yangi xabar📌\n\n<i>{}</i>".format(user_mention, text))
    await bot.send_message(chat_id=message.chat.id, text='Xabaringiz adminga yuborildi')