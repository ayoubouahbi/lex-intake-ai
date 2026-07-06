import asyncio
import os
from handlers.start import router as start_router
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from config.settings import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)


dp = Dispatcher()
dp.include_router(start_router)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
