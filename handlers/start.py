from aiogram import types, Router
from aiogram.filters import Command
from Data_base.database import save_user_info


start_router = Router()


@start_router.message(Command('start'))
async def start(message: types.Message):
    await save_user_info(message.from_user.full_name, message.from_user.id)
    await message.answer(f'Добрий день, {message.from_user.full_name}!\n'
                         f'Вы находитесь в телеграм боте, который поможет Вам выбрать спортивную обувь.\n'
                         f'Тут все очень легко, что бы начать работу, необходимо выполнить команду /menu,\n'
                         f'Бот покажет выбор размеров, нажимайте на интересующий, бот покажет что есть в наличии.\n\n'
                         f'Если есть вопросы, Вы всегда можете обратиться к администратору -> @Yaroslav_2500\n\n'
                         f'Что бы получить каталог размеров, выполните команду /menu.\n\n'
                         f'/help - если что-то не получаеться.'
                         )
