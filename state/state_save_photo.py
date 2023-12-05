from aiogram.fsm.state import State, StatesGroup


class SavePhoto(StatesGroup):
    photo1 = State()
    photo2 = State()
    photo3 = State()
    photo4 = State()
    photo5 = State()
    photo6 = State()
    photo7 = State()
    name = State()
    size = State()
    sm = State()
    condition = State()
    price = State()
