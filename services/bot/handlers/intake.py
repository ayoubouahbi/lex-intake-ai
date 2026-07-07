from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states import IntakeForm

router = Router()


@router.message(IntakeForm.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(IntakeForm.phone)

    await message.answer("Quel est votre numéro de téléphone ?")
