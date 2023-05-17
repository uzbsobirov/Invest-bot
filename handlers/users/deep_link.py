from loader import dp, db, bot
from keyboards.inline.deeplink import deep_link_share

from aiogram import types
from aiogram.dispatcher import FSMContext

from language import i18n

_ = i18n.gettext


@dp.message_handler(text=_("🔗 Referal"), state='*')
async def start_deep_link(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    get_me = await bot.get_me()
    bot_username = get_me.username

    selection = await db.select_one_user(user_id=user_id)
    count = selection[0][10]
    deeplink = selection[0][8]

    caption = _(f"Sizning referalingiz: {count} ta\n\n"
                f"🎁Metago Botdan Sizga har bir taklif qilgan dòstingiz uchun 5$ "
                f"gacha bonus beriladi va ular balansini har gal to'ldirganida sizga 1% "
                f"oyda taqdim etiladi!✅️\n\nSizning link: <code>{deeplink}</code>")

    with open(file='media/referal.jpg', mode='rb') as photo:
        await message.answer_photo(photo=photo, caption=caption,
                                   reply_markup=deep_link_share(user_id=user_id, bot_username=bot_username))
