from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot, _


@dp.message_handler(Text('ферма'))
async def _settings_command(message: types.Message):
    await message.answer(
        text=_(""),
    )
