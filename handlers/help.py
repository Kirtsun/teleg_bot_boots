from aiogram import types, Router, F
from aiogram.filters import Command
from loader import admins

help_router = Router()


@help_router.message(Command('help'))
@help_router.message(F.text.casefold() == 'cancel')
async def help_comm(message: types.Message):
    if message.from_user.id in admins:
        await message.answer(text='Ну что хозяин, без помощи ни как?))\n'
                                  'Вот команды администратора, которые тебе могут пригодиться:\n\n'
                                  '/adm_menu - эта команда выведет тебя меню размеров. С помощью этого меню,'
                                  ' ты можешь выбрать бутсы, которые хочешь удалить.\n\n'
                                  '/load - это команда запускает процес загрузки фото и информации в базу данных.\n\n'
                                  '/cancel - останавливает процес загрузки фото.\n\n'
                                  '/menu - команда выводит меню с доступными размерами обуви.\n\n'
                                  '/help - виводит иформацию о доступных командах в этом боте.\n\n'
                                  'Если все еще остались вопросы или что-то не работает напиши мне -> @Kyrtsun')
    else:
        await message.answer(text='Вот команды, которые помогут разобраться в этом боте:\n'
                                  '/menu - команда выводит меню с доступными размерами обуви.\n\n'
                                  '/help - виводит иформацию о доступных командах в этом боте.\n\n'
                                  'Если все еще остались вопросы или что-то не работает напиши -> @Yaroslav_2500')
