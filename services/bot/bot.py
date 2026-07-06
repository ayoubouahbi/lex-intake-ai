import os
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv("../api/.env")

bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
dp = Dispatcher()
users = {}

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Bonjour 👋\n\nBienvenue au cabinet.\n\nAvant de commencer, quel est votre nom et prénom ?"
    )


@dp.message()
async def receive_name(message: Message):
    user_id = message.from_user.id

    if user_id not in users:
        users[user_id] = {
            "step": "name"
        }

    if users[user_id]["step"] == "name":
        users[user_id]["name"] = message.text
        users[user_id]["step"] = "phone"

        await message.answer(
            f"Merci {message.text}.\n\nQuel est votre numéro de téléphone ?"
        )

    elif users[user_id]["step"] == "phone":
        users[user_id]["phone"] = message.text

        await message.answer(
            "Merci. Votre demande a bien été enregistrée."
        )

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
