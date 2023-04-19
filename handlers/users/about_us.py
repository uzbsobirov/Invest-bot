from aiogram.types import MediaGroup

from loader import dp, bot

from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="📰 Bot haqida", state='*')
async def about_us_func(message: types.Message, state: FSMContext):

    media1 = MediaGroup()
    media2 = MediaGroup()
    media3 = MediaGroup()

    text1 = "<b>METAGO BOT NIMA ❓ - NEGA BIZGA PUL TO'LAYDI</b> 💰❓\n\n" \
            "- MetaGo 2017 yil AQSH da tashkil etildi va o'zining MAG Kriptovalyutasiga ega ✅\n" \
            "- Joriy Yilda MetaGo arbitraj loyihasi keng ommaga taqdim etildi ✅\n" \
            "- MetaGo Kriptovalyuta oldi sottisi bilan shug'ullanadi va foydani " \
            "darajalarga asoslab ikkiga bo'ladi :\n\n" \
            " 🟢 PREMIUM / yani bunda kunlik foyda siz kiritgan summaning " \
            "3.4% ni tashkil qiladi.500$ bilan boshlanadi.\n\n🔵 STANDARD  /  " \
            "yani bunda kunlik foyda siz kiritgan summaning 2.3% ni tashkil qiladi. " \
            "50$ bilan boshlanadi.\n\n🟡 MINIMUM   /  yani bunda kunlik foyda siz " \
            "kiritgan summaning 1.8% ni tashkil qiladi. 30 $ bilan boshlanadi.\n\n" \
            "💰Eng kam yechib olish 10 $\n💰Eng ko'p yechib olish 10000 $ - bir martalik zayavkada\n" \
            "🏛️Hisobingizga 72 soat davomida tushadi✅"

    text2 = "METAGO – dunyodagi yetakchi aqlli moliyaviy boshqaruv platformasi " \
            "hisoblanib, kompaniya shtab-kvartirasi Koloradoda, Gʻarbiy AQShda " \
            "joylashgan. METAGO AQSH Moliya byurosi tomonidan tartibga solinadi, " \
            "siz bizning kompaniyamizning barcha malakalari, sertifikatlari, biznesi, " \
            "litsenziyalari va hokazolarni tekshirishingiz mumkin. Google play doʻkonida " \
            "ham yuklab olish mumkin. METAGO bosh ofisi 2017 yilda tashkil etilgan. METAGO " \
            "dunyodagi eng professional miqdoriy platforma boʻlib, yaxshi miqdoriy platforma " \
            "boʻlish uchun barcha masʼuliyatni oʻz zimmasiga oladi✅️"

    text3 = "🇺🇿 MetaGo Bot - O'zbekiston davlatida ham o'z filiallariga ega bo'lib , " \
            "hozirda ko'plab foydalanuvchilardan tashkil topgan jamoalariga ega va " \
            "yuqori darajada daromad olishayotganligi sababli hayriya tadbirlarini ham " \
            "o'tkazib  kelmoqda.\n\n🤑MetaGo Bot - nafaqat dunyo aholisini hattoki musulmon " \
            "davlatlar xalqi tomonidan ham o'zining ishonchli, tezkor daromad manbai sababli " \
            "iliqlik bilan kutib olindi va hozirda ko'plab davlatlar MetaGo Bot orqali o'z " \
            "orzulariga erishib, farovon hayot kechirmoqda✅️"


    # First media
    with open(file='media/video1.mp4', mode='rb') as video1:
        media1.attach_video(video=video1, caption=text1)
    video1.close()


    # # Second description
    # with open(file='media/photo2.jpg', mode='rb') as photo2_1:
    #     media2.attach_photo(photo=photo2_1)
    # photo2_1.close()
    #
    # with open(file='media/photo2_2.jpg', mode='rb') as photo2_2:
    #     media2.attach_photo(photo=photo2_2)
    # photo2_2.close()
    #
    # with open(file='media/photo2_3.jpg', mode='rb') as photo2_3:
    #     media2.attach_photo(photo=photo2_3)
    # photo2_3.close()
    #
    # with open(file='media/photo2_4.jpg', mode='rb') as photo2_4:
    #     media2.attach_photo(photo=photo2_4)
    # photo2_4.close()
    #
    # with open(file='media/photo2_5.jpg', mode='rb') as photo2_5:
    #     media2.attach_photo(photo=photo2_5)
    # photo2_5.close()
    #
    # with open(file='media/photo2_6.jpg', mode='rb') as photo2_6:
    #     media2.attach_photo(photo=photo2_6)
    # photo2_6.close()
    #
    # with open(file='media/photo2_7.jpg', mode='rb') as photo2_7:
    #     media2.attach_photo(photo=photo2_7)
    # photo2_7.close()
    #
    #
    # # Third medias
    # with open(file='media/photo3.jpg', mode='rb') as photo3:
    #     media2.attach_photo(photo=photo3)
    # photo3.close()
    #
    # with open(file='media/photo3_2.jpg', mode='rb') as photo3_2:
    #     media2.attach_photo(photo=photo3_2)
    # photo3_2.close()
    #
    # with open(file='media/photo3_3.jpg', mode='rb') as photo3_3:
    #     media2.attach_photo(photo=photo3_3)
    # photo3_3.close()
    #
    # with open(file='media/photo3_4.mp4', mode='rb') as photo3_4:
    #     media2.attach_photo(photo=photo3_4)
    # photo3_4.close()
    #
    # with open(file='media/photo3_5.jpg', mode='rb') as photo3_5:
    #     media2.attach_photo(photo=photo3_5)
    # photo3_5.close()
    #
    # with open(file='media/video3.mp4', mode='rb') as video_3:
    #     media2.attach_photo(photo=video_3)
    # video_3.close()
    #
    # with open(file='media/video3_2.mp4', mode='rb') as video3_2:
    #     media2.attach_photo(photo=video3_2)
    # video3_2.close()
    #
    # with open(file='media/video3_3.mp4', mode='rb') as video3_3:
    #     media2.attach_photo(photo=video3_3)
    # video3_3.close()




    await message.answer_media_group(media=media1)
    await message.answer(text=text1)

    # await message.answer_media_group(media=media2)
    # await message.answer(text=text2)
    #
    # await message.answer_media_group(media=media3)
    # await message.answer(text=text3)
