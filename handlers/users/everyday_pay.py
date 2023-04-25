import schedule

from loader import dp, db
from states.buycrypto import EveryDay
from .detectors import detect_percent

from aiogram.dispatcher import FSMContext
from aiogram import types

# from data.config import ADMINS
# from loader import scheduler, bot
# from aiogram import Dispatcher
#
# async def send_message_to_admin():
#     await bot.send_message(chat_id=ADMINS[0], text='siuuu')
#
# async def schedule_jobs():
#     scheduler.add_job(await send_message_to_admin(), 'interval', seconds=5)
#
#
#
#
#
#





# def pay_time_schedule(user_id, current_money, crypto):
#
#     percent = (current_money * detect_percent(crypto=crypto)) / 100
#
#     changed_money = current_money + percent
#
#     return "Kunlik foiz hisobingizga o'tkazildi✅", changed_money
#
#
# async def main(user_id):
#     schedule.every(5).seconds.do(pay_time_schedule(user_id=user_id))
#
#     while True:
#         schedule.run_pending()
#
# # if __name__ == '__main__':
# #     await main(user_id)