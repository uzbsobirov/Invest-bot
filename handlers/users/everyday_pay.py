import schedule

from loader import dp, db
from states.buycrypto import EveryDay
from .detectors import detect_percent

from aiogram.dispatcher import FSMContext
from aiogram import types


def pay_time_schedule(user_id, current_money, crypto):

    percent = (current_money * detect_percent(crypto=crypto)) / 100

    changed_money = current_money + percent

    return "Kunlik foiz hisobingizga o'tkazildi✅", changed_money


async def main(user_id):
    schedule.every(5).seconds.do(pay_time_schedule(user_id=user_id))

    while True:
        schedule.run_pending()

# if __name__ == '__main__':
#     await main(user_id)