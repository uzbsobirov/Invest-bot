from keyboards.inline.cards import cards
from loader import dp
from keyboards.inline.buying import buying

from aiogram import types
from aiogram.dispatcher import FSMContext

from states.viprates import Rate
from states.buycrypto import Buy


@dp.callback_query_handler(state=Rate.rates)
async def any_state(call: types.CallbackQuery, state: FSMContext):

    text = "<b>📋Quyidagi to'lov turlaridan birini tanlang:</b>"
    await call.message.edit_text(text=text, reply_markup=cards)
    await Buy.crypto.set()

@dp.callback_query_handler(text="payeer", state=Buy.crypto)
async def buy_anything(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    data = await state.get_data()
    current = data.get('current_crypto')

    if current == 'maximumltc':
        text = "<b>🔹 Kriptovalyuta: Maximum LTC\n" \
               "📋To'lov tizimi: Payeer\n\n" \
               "💳 Hamyon ( yoki karta ): qiwi karta here\n" \
               f"📝 Izoh: <code>{user_id}</code>, LTC\n\n" \
               "❗️Qo'shimcha: Diqqat! izoh kiritishni unutsangiz yoki " \
               "noto'g'ri kiritsangiz hisobingizga pul tushmaydi! " \
               "Bu kabi holatlarda, biz bilan bog'lanishingiz mumkin.</b>"
        await call.message.edit_text(text=text, reply_markup=buying)

    elif current == 'standarteth':
        text = "<b>🔹 Kriptovalyuta: Standart ETH\n" \
               "📋To'lov tizimi: Payeer\n\n" \
               "💳 Hamyon ( yoki karta ): qiwi karta here\n" \
               f"📝 Izoh: <code>{user_id}</code>, ETH\n\n" \
               "❗️Qo'shimcha: Diqqat! izoh kiritishni unutsangiz yoki " \
               "noto'g'ri kiritsangiz hisobingizga pul tushmaydi! " \
               "Bu kabi holatlarda, biz bilan bog'lanishingiz mumkin.</b>"
        await call.message.edit_text(text=text, reply_markup=buying)

    else:
        text = "<b>🔹 Kriptovalyuta: Premium BTC\n" \
               "📋To'lov tizimi: Payeer\n\n" \
               "💳 Hamyon ( yoki karta ): qiwi karta here\n" \
               f"📝 Izoh: <code>{user_id}</code>, BTC\n\n" \
               "❗️Qo'shimcha: Diqqat! izoh kiritishni unutsangiz yoki " \
               "noto'g'ri kiritsangiz hisobingizga pul tushmaydi! " \
               "Bu kabi holatlarda, biz bilan bog'lanishingiz mumkin.</b>"
        await call.message.edit_text(text=text, reply_markup=buying)

@dp.callback_query_handler(text="qiwi", state=Buy.crypto)
async def buy_anything(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    data = await state.get_data()
    current = data.get('current_crypto')

    if current == 'maximumltc':
        text = "<b>🔹 Kriptovalyuta: Maximum LTC\n" \
               "📋To'lov tizimi: Qiwi\n\n" \
               "💳 Hamyon ( yoki karta ): qiwi karta here\n" \
               f"📝 Izoh: <code>{user_id}</code>, LTC\n\n" \
               "❗️Qo'shimcha: Diqqat! izoh kiritishni unutsangiz yoki " \
               "noto'g'ri kiritsangiz hisobingizga pul tushmaydi! " \
               "Bu kabi holatlarda, biz bilan bog'lanishingiz mumkin.</b>"
        await call.message.edit_text(text=text, reply_markup=buying)

    elif current == 'standarteth':
        text = "<b>🔹 Kriptovalyuta: Standart ETH\n" \
               "📋To'lov tizimi: Qiwi\n\n" \
               "💳 Hamyon ( yoki karta ): qiwi karta here\n" \
               f"📝 Izoh: <code>{user_id}</code>, ETH\n\n" \
               "❗️Qo'shimcha: Diqqat! izoh kiritishni unutsangiz yoki " \
               "noto'g'ri kiritsangiz hisobingizga pul tushmaydi! " \
               "Bu kabi holatlarda, biz bilan bog'lanishingiz mumkin.</b>"
        await call.message.edit_text(text=text, reply_markup=buying)

    else:
        text = "<b>🔹 Kriptovalyuta: Premium BTC\n" \
               "📋To'lov tizimi: Qiwi\n\n" \
               "💳 Hamyon ( yoki karta ): qiwi karta here\n" \
               f"📝 Izoh: <code>{user_id}</code>, BTC\n\n" \
               "❗️Qo'shimcha: Diqqat! izoh kiritishni unutsangiz yoki " \
               "noto'g'ri kiritsangiz hisobingizga pul tushmaydi! " \
               "Bu kabi holatlarda, biz bilan bog'lanishingiz mumkin.</b>"
        await call.message.edit_text(text=text, reply_markup=buying)