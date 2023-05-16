from aiogram.types import MediaGroup

from loader import dp, bot

from aiogram import types
from aiogram.dispatcher import FSMContext

from language import i18n

_ = i18n.gettext


@dp.message_handler(text=_("📰 Bot haqida"), state='*')
async def about_us_func(message: types.Message, state: FSMContext):
    media1 = MediaGroup()
    media2 = MediaGroup()
    media3 = MediaGroup()

    text1 = _("<b>METAGO BOT NIMA ❓ - NEGA BIZGA PUL TO'LAYDI</b> 💰❓\n\n"
              "- MetaGo 2017 yil AQSH da tashkil etildi va o'zining MAG Kriptovalyutasiga ega ✅\n"
              "- Joriy Yilda MetaGo arbitraj loyihasi keng ommaga taqdim etildi ✅\n"
              "- MetaGo Kriptovalyuta oldi sottisi bilan shug'ullanadi va foydani "
              "darajalarga asoslab ikkiga bo'ladi :\n\n 🟢 PREMIUM / yani bunda "
              "kunlik foyda siz kiritgan summaning 3.4% ni tashkil qiladi.500$ bilan boshlanadi.\n\n"
              "🔵 STANDARD  /  yani bunda kunlik foyda siz kiritgan summaning 2.3% ni tashkil qiladi. "
              "50$ bilan boshlanadi.\n\n🟡 MINIMUM   /  yani bunda kunlik foyda siz "
              "kiritgan summaning 1.8% ni tashkil qiladi. 30 $ bilan boshlanadi.\n\n"
              "💰Eng kam yechib olish 10 $\n💰Eng ko'p yechib olish 10000 $ - bir martalik zayavkada\n🏛"
              "️Hisobingizga 72 soat davomida tushadi✅")

    text2 = _("METAGO – dunyodagi yetakchi aqlli moliyaviy boshqaruv platformasi hisoblanib, "
              "kompaniya shtab-kvartirasi Koloradoda, Gʻarbiy AQShda joylashgan. METAGO AQSH "
              "Moliya byurosi tomonidan tartibga solinadi, siz bizning kompaniyamizning barcha "
              "malakalari, sertifikatlari, biznesi, litsenziyalari va hokazolarni "
              "tekshirishingiz mumkin. Google play doʻkonida ham yuklab olish mumkin. "
              "METAGO bosh ofisi 2017 yilda tashkil etilgan. METAGO dunyodagi eng professional "
              "miqdoriy platforma boʻlib, yaxshi miqdoriy platforma boʻlish uchun barcha masʼuliyatni "
              "oʻz zimmasiga oladi✅️")

    text3 = _("🇺🇿 MetaGo Bot - O'zbekiston davlatida ham o'z filiallariga ega bo'lib , "
              "hozirda ko'plab foydalanuvchilardan tashkil topgan jamoalariga ega va yuqori "
              "darajada daromad olishayotganligi sababli hayriya tadbirlarini ham o'tkazib  "
              "kelmoqda.\n\n🤑MetaGo Bot - nafaqat dunyo aholisini hattoki musulmon davlatlar "
              "xalqi tomonidan ham o'zining ishonchli, tezkor daromad manbai sababli iliqlik bilan "
              "kutib olindi va hozirda ko'plab davlatlar MetaGo Bot orqali o'z orzulariga erishib, "
              "farovon hayot kechirmoqda✅️")

    # First media
    media1.attach_video(video="https://t.me/metago_medias/15", caption=text1)

    # Second media
    media2.attach_photo(photo="https://t.me/metago_medias/2", caption=text2)
    media2.attach_photo(photo="https://t.me/metago_medias/3")
    media2.attach_photo(photo="https://t.me/metago_medias/4")
    media2.attach_photo(photo="https://t.me/metago_medias/5")
    media2.attach_photo(photo="https://t.me/metago_medias/6")
    media2.attach_photo(photo="https://t.me/metago_medias/7")

    # Third media
    media3.attach_photo(photo="https://t.me/metago_medias/8", caption=text3)
    media3.attach_video(video="https://t.me/metago_medias/12")
    media3.attach_photo(photo="https://t.me/metago_medias/9")
    media3.attach_video(video="https://t.me/metago_medias/16")
    media3.attach_photo(photo="https://t.me/metago_medias/10")
    media3.attach_video(video="https://t.me/metago_medias/17")
    media3.attach_photo(photo="https://t.me/metago_medias/11")
    media3.attach_video(video="https://t.me/metago_medias/18")
    media3.attach_photo(photo="https://t.me/metago_medias/13")

    await message.answer_media_group(media=media1)

    await message.answer_media_group(media=media2)

    await message.answer_media_group(media=media3)
