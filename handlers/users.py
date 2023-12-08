import asyncio

import json

from Data_base.database import get_size

from aiogram import Router, exceptions, types
from aiogram.filters import Command
from aiogram.utils.media_group import MediaGroupBuilder

from buttons.button_for_size import SizesCallbackFactory, get_buttons_size

from logger import get_logger


user_router = Router()
logger = get_logger('users')


@user_router.message(Command('menu'))
async def menu(message: types.Message):
    await message.answer(text='Выберите размер, который Вас интересует.', reply_markup=get_buttons_size())


@user_router.callback_query(SizesCallbackFactory.filter())
async def send_all_products(
        callback: types.CallbackQuery,
        callback_data: SizesCallbackFactory):
    res = await get_size(callback_data.value_size, callback_data.value_sm)
    await callback.message.delete()
    if res:
        await callback.answer()
        for row in res:
            photo = json.loads(row[1])
            videos = json.loads(row[2])
            media = MediaGroupBuilder(
                caption=f'{row[3]}\n'
                        f'🔛Size: {row[4]}({row[5]} см)\n'
                        f'🔝Condition: {row[6]}/10\n'
                        f'💰Price: {row[7]} UAN\n'
                        f'Вопросы и заказы -> @Yaroslav_2500'
            )
            if photo:
                for i in photo:
                    media.add_photo(i)
            if videos:
                for i in videos:
                    media.add_video(i)
            try:
                await callback.message.answer_media_group(media=media.build())
            except Exception or exceptions.TelegramAPIError as e:
                logger.critical(f'Не удалось отправить все посты для пользователя! {e}')
                await callback.message.answer(text='К сожалению, что то пошло не так, обратитесь к админу'
                                                   ' -> @Yaroslav_2500')
            await asyncio.sleep(delay=2)
        await callback.message.answer(text='Что бы снова получить возможность просмотреть все размеры, необходимо'
                                           'выполнить команду: \n /menu')
    else:
        await callback.message.answer(text='К сожалению, данного размера пока нет в наличии.')
        await callback.answer()
        await callback.message.answer(text='Что бы снова получить возможность просмотреть все размеры, необходимо'
                                           'выполнить команду: \n /menu')
