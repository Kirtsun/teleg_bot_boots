from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import Optional
from aiogram.filters.callback_data import CallbackData


class SizesCallbackFactory(CallbackData, prefix="sizenum"):
    value_size: int
    value_sm: float


def get_buttons_size():
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Размер 39(24,5 см)', callback_data=SizesCallbackFactory(value_size=39, value_sm=24.5)
    )
    builder.button(
        text='Размер 40(25 см)', callback_data=SizesCallbackFactory(value_size=40, value_sm=25)
    )
    builder.button(
        text='Размер 40,5(25,5 см)', callback_data=SizesCallbackFactory(value_size=40, value_sm=25.5)
    )
    builder.button(
        text='Размер 41(26 см)', callback_data=SizesCallbackFactory(value_size=41, value_sm=26)
    )
    builder.button(
        text='Размер 42(26,5 см)', callback_data=SizesCallbackFactory(value_size=42, value_sm=26.5)
    )
    builder.button(
        text='Размер 42(27 см)', callback_data=SizesCallbackFactory(value_size=42, value_sm=27)
    )
    builder.button(
        text='Размер 43(27,5 см)', callback_data=SizesCallbackFactory(value_size=43, value_sm=25.5)
    )
    builder.button(
        text='Размер 44(28 см)', callback_data=SizesCallbackFactory(value_size=44, value_sm=28)
    )
    builder.button(
        text='Размер 44(28,5 см)', callback_data=SizesCallbackFactory(value_size=44, value_sm=28.5)
    )
    builder.button(
        text='Размер 45(29 см)', callback_data=SizesCallbackFactory(value_size=45, value_sm=29)
    )
    builder.button(
        text='Размер 46(29,5 см)', callback_data=SizesCallbackFactory(value_size=46, value_sm=29.5)
    )
    builder.button(
        text='Размер 46(30 см)', callback_data=SizesCallbackFactory(value_size=46, value_sm=30)
    )
    builder.button(
        text='Размер 47(30,5 см)', callback_data=SizesCallbackFactory(value_size=47, value_sm=30.5)
    )
    builder.button(
        text='Размер 48(31 см)', callback_data=SizesCallbackFactory(value_size=48, value_sm=31)
    )
    builder.button(
        text='Размер 48(31,5 см)', callback_data=SizesCallbackFactory(value_size=46, value_sm=31.5)
    )
    builder.adjust(2)
    return builder.as_markup()
