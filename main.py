import asyncio
import logging
from aiogram import Dispatcher
from aiogram import Bot

from dotenv import load_dotenv
import os
load_dotenv()

from aiogram_dialog import setup_dialogs

from quiz_dialogue import router_basic

# Initialize bot here
bot = Bot(token=os.getenv('API_TOKEN'), parse_mode="HTML")

async def main_loop():

    dp = Dispatcher()
    setup_dialogs(dp)
    dp.include_routers(router_basic)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main_loop())