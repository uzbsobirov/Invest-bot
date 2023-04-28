from data.config import ADMINS
from keyboards.inline.admin import admin
from keyboards.inline.cards import cards
from loader import dp
from states.admin import Panel
from states.buycrypto import Buy
from states.viprates import Rate
from keyboards.inline.viprates import rates
from keyboards.default.start import start, start_admin
from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text="back_to_main", state='*')
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()

    start_text = "<b>Assalomu aleykum hurmatli mijoz! Siz bu bot orqali kriptovalyutalarga investitsiya " \
                 "kiritib olishingiz mumkin</b>"
    await call.message.answer(text=start_text, reply_markup=start)
    await state.finish()

@dp.callback_query_handler(text="back", state=Rate.rates)
async def back_to_rates(call: types.CallbackQuery, state: FSMContext):

    text = "O'zingizga kerakli bo'lgan tarifni tanlang👇"
    await call.message.edit_text(text=text, reply_markup=rates)
    await Rate.rates.set()

@dp.callback_query_handler(text="back_to_rates", state=Buy.crypto)
async def back_to_rates(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()

    text = "O'zingizga kerakli bo'lgan tarifni tanlang👇"
    await call.message.answer(text=text, reply_markup=rates)
    await Rate.rates.set()

@dp.callback_query_handler(text="back_to_cards", state=Buy.photo)
async def back_to_rates(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()

    text = "<b>📋Quyidagi to'lov turlaridan birini tanlang:</b>"
    await call.message.answer(text=text, reply_markup=cards)
    await Buy.crypto.set()

@dp.callback_query_handler(text="back", state=Panel.statics)
async def back_to_admin_menu(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="<b>Admin panelga xush kelibsiz</b>", reply_markup=admin)
    await Panel.admin_menu.set()

@dp.callback_query_handler(text="back", state=Panel.admin_menu)
async def back_to_main_menu(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    try:
        await call.message.delete()
    except:
        pass

    if int(user_id) != int(ADMINS[0]):
        await call.message.answer(text="<b>Asosiy menu</b>", reply_markup=start)

    else:
        await call.message.answer(text="<b>Asosiy menu</b>", reply_markup=start_admin)

    await state.finish()

@dp.callback_query_handler(text="back_to_admin_menu", state=Panel.sponsor)
async def back_to_admin_menu(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="<b>Admin panelga xush kelibsiz</b>", reply_markup=admin)
    await Panel.admin_menu.set()

@dp.callback_query_handler(text="back_sponsor", state=Panel.get_id)
async def back_to_admin_menu(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="<b>Admin panelga xush kelibsiz</b>", reply_markup=admin)
    await Panel.admin_menu.set()