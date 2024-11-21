from aiogram import types
from aiogram.dispatcher.filters import CommandStart, Text

from loader import dp, bot, _
from app.handlers.msg_text import msg_text
@dp.message_handler(CommandStart())
async def _start_command(message: types.Message):
    await message.answer(msg_text.WELCOME.format(message.from_user.id, message.from_user.full_name))



