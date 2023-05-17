from aiogram import executor

from loader import dp, db, bot
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers.users.admin_panel.pay_to_user import scheduler


async def on_startup(dispatcher):
    await db.create()
    await db.create_table_users()
    await db.create_table_user_lang()

    # Birlamchi komandalar (/start va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if __name__ == "__main__":
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
