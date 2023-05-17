from loader import db
from .detectors import detect_percent, detect_crypto_money


async def pay_time_schedule(user_id: int):

    get_datas = await db.select_one_user(user_id=int(user_id))

    current_money = get_datas[0][5]
    crypto = get_datas[0][4]
    date = get_datas[0][12]

    if date > 0:
        if current_money > detect_crypto_money(crypto=crypto):

            percent = (current_money * detect_percent(crypto=crypto)) / 100

            changed_money = current_money + percent

            await db.update_user_new_money(money=changed_money, user_id=user_id)

            await db.update_user_date(user_id=user_id)






