from handlers.detectors import detect_crypto
from keyboards.inline.cards import cards
from loader import dp, bot
from keyboards.inline.buying import buying

from aiogram import types
from aiogram.dispatcher import FSMContext

from states.viprates import Rate
from states.buycrypto import Buy

from language import i18n

_ = i18n.gettext

@dp.callback_query_handler(state=Rate.rates)
async def any_state(call: types.CallbackQuery, state: FSMContext):

    text = _("<b>📋Quyidagi to'lov turlaridan birini tanlang:</b>")
    await call.message.edit_text(text=text, reply_markup=cards)
    await Buy.crypto.set()

@dp.callback_query_handler(text="payeer", state=Buy.crypto)
async def buy_anything(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    data = await state.get_data()
    current = data.get('current_crypto')

    if current == 'maximumltc':
        text = _("<b>🔹 Kriptovalyuta: Maximum LTC\n📋To'lov tizimi: Payeer\n\n💳 Hamyon: <code>P1092553472</code>\n📝 Izoh: <code>{}</code>, LTC\n\n❗️Qo'shimcha: Diqqat! izoh kiritishni unutsangiz yoki noto'g'ri kiritsangiz hisobingizga pul tushmaydi! Bu kabi holatlarda, biz bilan bog'lanishingiz mumkin.\n\n🔊To'lov haqidagi chekni shu yerga yuboring</b>".format(user_id))

        await call.message.delete()
        await call.message.answer_photo(photo="https://t.me/metago_medias/23", caption=text, reply_markup=buying)

    elif current == 'standarteth':
        text = _("<b>🔹 Kriptovalyuta: Standart ETH\n📋To'lov tizimi: Payeer\n\n💳 Hamyon: <code>P1092553472</code>\n📝 Izoh: <code>{}</code>, ETH\n\n❗️Qo'shimcha: Diqqat! izoh kiritishni unutsangiz yoki noto'g'ri kiritsangiz hisobingizga pul tushmaydi! Bu kabi holatlarda, biz bilan bog'lanishingiz mumkin.\n\n🔊To'lov haqidagi chekni shu yerga yuboring</b>".format(user_id))

        await call.message.delete()
        await call.message.answer_photo(photo="https://t.me/metago_medias/23", caption=text, reply_markup=buying)

    else:
        text = _("<b>🔹 Kriptovalyuta: Premium BTC\n📋To'lov tizimi: Payeer\n\n💳 Hamyon: <code>P1092553472</code>\n📝 Izoh: <code>{}</code>, BTC\n\n❗️Qo'shimcha: Diqqat! izoh kiritishni unutsangiz yoki noto'g'ri kiritsangiz hisobingizga pul tushmaydi! Bu kabi holatlarda, biz bilan bog'lanishingiz mumkin.\n\n🔊To'lov haqidagi chekni shu yerga yuboring</b>".format(user_id))
        await call.message.delete()
        await call.message.answer_photo(photo="https://t.me/metago_medias/23", caption=text, reply_markup=buying)

    await Buy.photo.set()

@dp.callback_query_handler(text="qiwi", state=Buy.crypto)
async def buy_anything(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    data = await state.get_data()
    current = data.get('current_crypto')

    if current == 'maximumltc':
        text = _("<b>🔹 Kriptovalyuta: Maximum LTC\n📋To'lov tizimi: Qiwi\n\n💳 Hamyon: <code>79955910342</code>\n📝 Izoh: <code>{}</code>, LTC\n\n❗️Qo'shimcha: Diqqat! izoh kiritishni unutsangiz yoki noto'g'ri kiritsangiz hisobingizga pul tushmaydi! Bu kabi holatlarda, biz bilan bog'lanishingiz mumkin.\n\n🔊To'lov haqidagi chekni shu yerga yuboring</b>".format(user_id))

        await call.message.delete()
        await call.message.answer_photo(photo="https://t.me/metago_medias/24", caption=text, reply_markup=buying)

    elif current == 'standarteth':
        text = _("<b>🔹 Kriptovalyuta: Standart ETH\n📋To'lov tizimi: Qiwi\n\n💳 Hamyon: <code>79955910342</code>\n📝 Izoh: <code>{}</code>, ETH\n\n❗️Qo'shimcha: Diqqat! izoh kiritishni unutsangiz yoki noto'g'ri kiritsangiz hisobingizga pul tushmaydi! Bu kabi holatlarda, biz bilan bog'lanishingiz mumkin.\n\n🔊To'lov haqidagi chekni shu yerga yuboring</b>".format(user_id))

        await call.message.delete()
        await call.message.answer_photo(photo="https://t.me/metago_medias/24", caption=text, reply_markup=buying)

    else:
        text = _("<b>🔹 Kriptovalyuta: Premium BTC\n📋To'lov tizimi: Qiwi\n\n💳 Hamyon: <code>79955910342</code>\n📝 Izoh: <code>{}</code>, BTC\n\n❗️Qo'shimcha: Diqqat! izoh kiritishni unutsangiz yoki noto'g'ri kiritsangiz hisobingizga pul tushmaydi! Bu kabi holatlarda, biz bilan bog'lanishingiz mumkin. To'lovni tasdiqlash uchun chek yuborish shart!\n\n🔊To'lov haqidagi chekni shu yerga yuboring</b>".format(user_id))

        await call.message.delete()
        await call.message.answer_photo(photo="https://t.me/metago_medias/24", caption=text, reply_markup=buying)

    await Buy.photo.set()


@dp.callback_query_handler(text="binance", state=Buy.crypto)
async def buy_anything(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    data = await state.get_data()
    current = data.get('current_crypto')

    if current == 'maximumltc':
        text = _("<b>🔹 Kriptovalyuta: Maximum LTC\n📋To'lov tizimi: Binance\n\n💳 Hamyon: <code>P1092553472</code>\n📝 Izoh: <code>{}</code>, LTC\n\n❗️Qo'shimcha: Diqqat! izoh kiritishni unutsangiz yoki noto'g'ri kiritsangiz hisobingizga pul tushmaydi! Bu kabi holatlarda, biz bilan bog'lanishingiz mumkin.\n\n🔊To'lov haqidagi chekni shu yerga yuboring</b>".format(user_id))

        await call.message.delete()
        await call.message.answer_photo(photo="https://t.me/metago_medias/26", caption=text, reply_markup=buying)

    elif current == 'standarteth':
        text = _("<b>🔹 Kriptovalyuta: Standart ETH\n📋To'lov tizimi: Binance\n\n💳 Hamyon: <code>P1092553472</code>\n📝 Izoh: <code>{}</code>, ETH\n\n❗️Qo'shimcha: Diqqat! izoh kiritishni unutsangiz yoki noto'g'ri kiritsangiz hisobingizga pul tushmaydi! Bu kabi holatlarda, biz bilan bog'lanishingiz mumkin.\n\n🔊To'lov haqidagi chekni shu yerga yuboring</b>".format(user_id))

        await call.message.delete()
        await call.message.answer_photo(photo="https://t.me/metago_medias/26", caption=text, reply_markup=buying)

    else:
        text = _("<b>🔹 Kriptovalyuta: Premium BTC\n📋To'lov tizimi: Binance\n\n💳 Hamyon: <code>P1092553472</code>\n📝 Izoh: <code>{}</code>, BTC\n\n❗️Qo'shimcha: Diqqat! izoh kiritishni unutsangiz yoki noto'g'ri kiritsangiz hisobingizga pul tushmaydi! Bu kabi holatlarda, biz bilan bog'lanishingiz mumkin.\n\n🔊To'lov haqidagi chekni shu yerga yuboring</b>".format(user_id))

        await call.message.delete()
        await call.message.answer_photo(photo="https://t.me/metago_medias/26", caption=text, reply_markup=buying)

    await Buy.photo.set()

@dp.message_handler(state=Buy.photo, content_types=types.ContentType.PHOTO)
async def confirm_photo(message: types.Message, state: FSMContext):
    data = await state.get_data()
    current = data.get('current_crypto')

    photo_id = message.photo[-1].file_id
    user_id = message.from_user.id
    chat_id = -1001749997672
    full_name = message.from_user.full_name
    user_mention = message.from_user.get_mention(name=full_name)

    await state.update_data(
        {'user_id': user_id}
    )

    caption = f"🆔 -> <code>{user_id}</code>\n👤 -> {user_mention}\n💎 -> {detect_crypto(crypto=current)}"

    await bot.send_photo(chat_id=chat_id, photo=photo_id, caption=caption)

    await bot.send_message(chat_id=message.chat.id, text=_("Chek adminlarga yuborildi. "
                                                           "Admin tez orada chekni tekshirib "
                                                           "xisobingizni to'ldirishadi"))



