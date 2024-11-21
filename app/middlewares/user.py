from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery, InlineQuery

from database.service.users import get_or_create_user
from database.service.group import add_user_to_group


class UsersMiddleware(BaseMiddleware):
    @staticmethod
    async def on_process_message(message: Message, data: dict):

        if message.chat.type == 'channel':
            raise CancelHandler()

        # await message.answer_chat_action('typing')

        user = message.from_user
        
        data['user'] = get_or_create_user(user.id, user.username, user.language_code)
        if message.chat.title:
            add_user_to_group(user.id, user.username, message.chat.id, message.chat.title)
        
    @staticmethod
    async def on_process_callback_query(callback_query: CallbackQuery, data: dict):
        user = callback_query.from_user
        language_code = user.language_code or "en"
        
        data['user'] = get_or_create_user(user.id, user.username, language_code)

    @staticmethod
    async def on_process_inline_query(inline_query: InlineQuery, data: dict):
        user = inline_query.from_user
        language_code = user.language_code or "en"
        
        data['user'] = get_or_create_user(user.id, user.username, language_code)