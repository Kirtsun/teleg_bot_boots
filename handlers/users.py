from aiogram import types, Router
from buttons.button_for_size import SizesCallbackFactory, get_buttons_size
from Data_base.database import get_size
import json
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.filters import Command

user_router = Router()


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
        for row in res:
            photo = json.loads(row[1])
            videos = json.loads(row[2])
            media = MediaGroupBuilder(
                caption=f'{row[3]}\n'
                        f'🔛Size: {row[4]}({row[5]} см)\n'
                        f'🔝Condition: {row[6]}/10\n'
                        f'💰Price: {row[7]} UAN\n'
                        f'Питання та замовлення у приват -> @Yaroslav_2500'
            )
            if photo:
                for i in photo:
                    media.add_photo(i)
            if videos:
                for i in videos:
                    media.add_video(i)
            await callback.message.answer_media_group(media=media.build())
            await callback.answer()
        await callback.message.answer(text=f'Что бы снова получить возможность просмотреть все размеры, необходимо'
                                           f'выполнить команду: \n /menu')
    else:
        await callback.message.answer(text='К сожалению, данного размера пока нет в наличии.')
        await callback.answer()
        await callback.message.answer(text=f'Что бы снова получить возможность просмотреть все размеры, необходимо'
                                           f'выполнить команду: \n /menu')
