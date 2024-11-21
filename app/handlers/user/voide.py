from aiogram import types
from loader import dp
from utils.logging import logger
@dp.message_handler()
async def _start_command(message: types.Message):
    logger.info(f"User ID: {message.from_user.id}, Message: {message.text}")