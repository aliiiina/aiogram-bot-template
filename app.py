from aiogram import executor
import filters, handlers
from loader import dp

from utils.notify_admins import on_startup_notify

async def on_startup(dispatcher):
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
