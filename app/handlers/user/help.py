from aiogram import types
from aiogram.dispatcher.filters import CommandHelp, Command

from loader import dp, bot, _

from app.handlers.msg_text import msg_text
@dp.message_handler(Command("Help 🆘"))
@dp.message_handler(CommandHelp())
async def _help_command(message: types.Message):
    await message.answer(
        text=msg_text.HELP,
    )
