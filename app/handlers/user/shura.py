from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot, _

from database.service.group import get_group_members
from random import randint

from app.handlers.msg_text import msg_text

from app.filters.user import ShuraInfo, ShuraShip, ShuraChances, ShuraWho, ShuraZov

@dp.message_handler(ShuraShip())
async def _start_command(message: types.Message):
    list = get_group_members(message.chat.id)

    user1 = list[randint(1, len(list)-1)]
    user2 = list[randint(1, len(list)-1)]
    
    await message.reply(msg_text.SHIP.format(user1, user2))
    
    
@dp.message_handler(ShuraWho())
async def _start_command(message: types.Message):
    words_to_remove = ["шура" , "кто", "хто"]
    list = get_group_members(message.chat.id)
    user = list[randint(1, len(list)-1)]

    # Убираем слова, которых нет в списке `words_to_remove`
    filtered_text = ' '.join(word for word in message.text.split() if word not in words_to_remove)
    
    await message.reply(msg_text.WHO.format(user, filtered_text))

    
@dp.message_handler(ShuraInfo())
async def _start_command(message: types.Message):
    num = randint(1, 4)
    info = {1: _("Да"), 2: _("Нет"), 3: _("В душе не ебу"),}
    await message.reply(info[num])
    
@dp.message_handler(ShuraChances())
async def _start_command(message: types.Message):
    change = randint(1, 100)
    await message.reply(msg_text.CHANCES.format(change))
    
    
@dp.message_handler(ShuraZov())
async def _start_command(message: types.Message):
    list = get_group_members(message.chat.id)
    
    for i in range(0, len(list), 5):
        chunk = list[i:i + 5]  # Извлекаем подсписок длиной до 5 элементов
        chunk_with_at = [f"@{name}" for name in chunk]
        text = ", ".join(chunk_with_at)
    await message.answer(text)