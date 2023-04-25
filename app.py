from aiogram import executor

from loader import dp, db, scheduler
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
# from handlers.users.everyday_pay import schedule_jobs



async def on_startup(dispatcher):
    await db.create()
    await db.create_table_users()
    await db.create_table_sponsor()
    # await schedule_jobs()

    # Birlamchi komandalar (/start va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if __name__ == "__main__":
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)

