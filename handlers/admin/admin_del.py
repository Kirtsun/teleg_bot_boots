import json

from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.utils.media_group import MediaGroupBuilder
from loader import admins
from buttons import DelCallbackFactory, get_buttons_del
from Data_base.database import get_size, del_boots
from aiogram.utils.keyboard import InlineKeyboardBuilder


admin_del_router = Router()


@admin_del_router.message(Command('adm_menu'), F.from_user.id.in_(admins))
async def admin_menu(message: types.Message):
    await message.answer(text='Выбери размер, в котором хочешь провести удаления.', reply_markup=get_buttons_del())


@admin_del_router.callback_query(DelCallbackFactory.filter())
async def del_info(
        callback: types.CallbackQuery,
        callback_data: DelCallbackFactory):
    builder = InlineKeyboardBuilder()
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
            builder.add(types.InlineKeyboardButton(
                text='Удалить.',
                callback_data=f'del {row[0]}'
            ))
            await callback.message.answer_media_group(media=media.build())
            await callback.message.answer(text='⬆️⬆️⬆️', reply_markup=builder.as_markup())
            await callback.answer()
        await callback.message.answer(text=f'Что бы снова получить возможность просмотреть все размеры, необходимо'
                                           f'выполнить команду: \n /adm_menu')
    else:
        await callback.message.answer(text='К сожалению, данного размера пока нет в наличии.')
        await callback.answer()
        await callback.message.answer(text=f'Что бы снова получить возможность просмотреть все размеры, необходимо'
                                           f'выполнить команду: \n /adm_menu')


@admin_del_router.callback_query(F.data.startswith('del '))
async def del_data(callback: types.CallbackQuery):
    pk = callback.data.replace('del ', '')
    res = await del_boots(pk)
    if res:
        await callback.message.bot.delete_message(chat_id=callback.message.chat.id,
                                                  message_id=callback.message.message_id)
    else:
        await callback.message.answer(text='Что-то пошло не так с удалением!')



