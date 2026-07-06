from aiogram.fsm.state import State, StatesGroup


class IntakeForm(StatesGroup):
    name = State()
    phone = State()
    city = State()
    legal_area = State()
    description = State()
