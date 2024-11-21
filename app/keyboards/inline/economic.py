from aiogram.types import (
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from loader import _


def wallet_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Магазин 🏪", callback_data="market"),
            ],
        ],
    )
    return ikb

def market_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Добавить команду", callback_data="add_command"),
                InlineKeyboardButton(text="Убрать команду", callback_data="del_command"),
            ],
        ],
    )
    return ikb

def group_list_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Добавить команду", callback_data="add_command"),
                InlineKeyboardButton(text="Убрать команду", callback_data="del_command"),
            ],
        ],
    )
    return ikb

