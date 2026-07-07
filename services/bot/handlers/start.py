from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states import IntakeForm

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(IntakeForm.name)

    await message.answer(
        "Bonjour 👋\n\nBienvenue au cabinet.\n\nQuel est votre nom et prénom ?"
    )
