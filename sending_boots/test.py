from aiogram import types, Router, F
from aiogram.filters import Command
from loader import bot

test_router = Router()


@test_router.message(Command('test'))
async def test(message: types.Message):
    print(str(message.from_user))




