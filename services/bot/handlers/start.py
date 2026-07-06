from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Bonjour 👋\n\nBienvenue au cabinet.\n\nAvant de commencer, quel est votre nom et prénom ?"
    )
