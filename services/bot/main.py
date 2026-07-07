import asyncio
import os
from handlers.start import router as start_router
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers.intake import router as intake_router

from config.settings import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)


dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(intake_router)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
