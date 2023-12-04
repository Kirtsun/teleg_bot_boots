from aiogram import types, Router, F
from aiogram.filters import Command
from Data_base.database import save_post
from loader import admins
from state.state_save_photo import SavePhoto
from aiogram.fsm.context import FSMContext
from helping_func_for_admin import check_right_sm

admin_save_router = Router()


@admin_save_router.message(Command('load'), F.from_user.id.in_(admins))
async def save_photo(message: types.Message, state: FSMContext):
    await state.set_state()
    await message.answer(text='Отправь мне первое фото.\n'
                              'Если хочешь остановить загрузку - /cancel')
    await state.set_state(SavePhoto.photo1)


@admin_save_router.message(Command('cancel'))
@admin_save_router.message(F.text.casefold() == 'cancel')
async def cancel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer('Загрузка фото остановлена!')


@admin_save_router.message(SavePhoto.photo1)
async def photo1(message: types.Message, state: FSMContext):
    if message.photo:
        data = await state.update_data(photo1=message.photo[0].file_id)
    else:
        data = await state.update_data(video1=message.video.file_id)
    await state.set_state(SavePhoto.photo2)
    await message.answer(text='Отправь фото 2.\n'
                              'Если хочешь остановить загрузку - /cancel')


@admin_save_router.message(SavePhoto.photo2)
async def photo2(message: types.Message, state: FSMContext):
    if message.photo:
        data = await state.update_data(photo2=message.photo[0].file_id)
    else:
        data = await state.update_data(video2=message.video.file_id)
    await state.set_state(SavePhoto.photo3)
    await message.answer(text='Отправь фото 3.\n'
                              'Если хочешь остановить загрузку - /cancel')


@admin_save_router.message(SavePhoto.photo3)
async def photo3(message: types.Message, state: FSMContext):
    if message.photo:
        data = await state.update_data(photo3=message.photo[0].file_id)
    else:
        data = await state.update_data(video3=message.video.file_id)
    await state.set_state(SavePhoto.photo4)
    await message.answer(text='Отправь фото 4.\n'
                              'Если хочешь остановить загрузку - /cancel')


@admin_save_router.message(SavePhoto.photo4)
async def photo4(message: types.Message, state: FSMContext):
    if message.photo:
        data = await state.update_data(photo4=message.photo[0].file_id)
    else:
        data = await state.update_data(video4=message.video.file_id)
    await state.set_state(SavePhoto.photo5)
    await message.answer(text='Отправь фото 5.\n'
                              'Если хочешь остановить загрузку - /cancel')


@admin_save_router.message(SavePhoto.photo5)
async def photo5(message: types.Message, state: FSMContext):
    if message.photo:
        data = await state.update_data(photo5=message.photo[0].file_id)
    else:
        data = await state.update_data(video5=message.video.file_id)
    await state.set_state(SavePhoto.photo6)
    await message.answer(text='Отправь фото 6.\n'
                              'Если хочешь остановить загрузку - /cancel')


@admin_save_router.message(SavePhoto.photo6)
async def photo6(message: types.Message, state: FSMContext):
    if message.photo:
        data = await state.update_data(photo6=message.photo[0].file_id)
    else:
        data = await state.update_data(video6=message.video.file_id)
    await state.set_state(SavePhoto.photo7)
    await message.answer(text='Отправь фото 7.\n'
                              'Если хочешь остановить загрузку - /cancel')


@admin_save_router.message(SavePhoto.photo7)
async def photo7(message: types.Message, state: FSMContext):
    if message.photo:
        data = await state.update_data(photo7=message.photo[0].file_id)
    else:
        data = await state.update_data(video7=message.video.file_id)
    await state.set_state(SavePhoto.name)
    await message.answer(text='Отправь название красовок.\n'
                              'Если хочешь остановить загрузку - /cancel')


@admin_save_router.message(SavePhoto.name)
async def boots_name(message: types.Message, state: FSMContext):
    if message.photo or message.video:
        await message.answer('Место для фото уже закончилось! Отправь название кросовок.')
    else:
        data = await state.update_data(name=message.text)
        await state.set_state(SavePhoto.size)
        await message.answer(text='Отправь размер, просто цифры.\n'
                              'Если хочешь остановить загрузку - /cancel')


@admin_save_router.message(SavePhoto.size)
async def size(message: types.Message, state: FSMContext):
    if int(message.text) > 48 or int(message.text) < 39:
        await message.answer(text='Размеры могут быть только от 39 до 48! По другому инфо не будет сохранено в базу!\n'
                                  'Отправь коректный размер снова.')
    else:
        data = await state.update_data(size=int(message.text))
        await state.set_state(SavePhoto.sm)
        await message.answer(text='Сейчас нужно отправить размер стельки, нужно указать только цифры.\n'
                              'Если хочешь остановить загрузку - /cancel')


@admin_save_router.message(SavePhoto.sm)
async def sm(message: types.Message, state: FSMContext):
    data = await state.update_data()
    if await check_right_sm(sm=message.text, size=data['size']):
        data = await state.update_data(sm=float(message.text))
        await state.set_state(SavePhoto.condition)
        await message.answer(text='Укажи состояние обуви, нужна цифра от 1 до 10.\n'
                              'Если хочешь остановить загрузку - /cancel')
    else:
        await message.answer('Указан не верный размер стельки или у этого размера нет такой стельки!\n'
                             'Отпрявь заново стельку!')


@admin_save_router.message(SavePhoto.condition)
async def condition(message: types.Message, state: FSMContext):
    if int(message.text) > 10:
        await message.answer('Состояние не может быть больше 10! Отправь заново.')
    else:
        data = await state.update_data(condition=int(message.text))
        await state.set_state(SavePhoto.price)
        await message.answer(text='И последнее, напиши цену!\n'
                                  'Если хочешь остановить загрузку - /cancel')


@admin_save_router.message(SavePhoto.price)
async def price(message: types.Message, state: FSMContext):
    data = await state.update_data(price=float(message.text))
    if await save_post(data):
        await message.answer('Информация сохранена :)\n'
                             '/load\n\n'
                             '/amd_menu')
    else:
        await message.answer('Что то пошло не так :(')
    await state.clear()




