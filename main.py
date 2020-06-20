import asyncio


from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handlers import dp, send_to_admin

    executor.start_polling(dp, on_startup=send_to_admin)