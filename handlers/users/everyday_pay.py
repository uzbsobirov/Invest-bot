import asyncio

import schedule
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from loader import dp, db
from .detectors import detect_percent, detect_crypto_money
from data.config import ADMINS

from aiogram import types


async def pay_time_schedule(user_id: int):
    # user_id = update['from']['id']



    # for _ in range(1, 31):
    get_datas = await db.select_one_user(user_id=user_id)

    current_money = get_datas[0][5]
    crypto = get_datas[0][4]
    date = get_datas[0][12]

    if date > 0:
        if current_money > detect_crypto_money(crypto=crypto):

            percent = (current_money * detect_percent(crypto=crypto)) / 100

            changed_money = current_money + percent

            await db.update_user_new_money(money=changed_money, user_id=user_id)

            await db.update_user_date(user_id=user_id)






