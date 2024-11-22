from aiogram import types
from aiogram.dispatcher.filters import Text, Command

from loader import dp, bot, _

from app.filters.user import Farm, Wallet
from utils.coin import get_countdown, coin_count
from database.service.coin import add_coin
from app.keyboards.inline.economic import wallet_ikb, market_ikb
from app.handlers.msg_text import msg_text

from utils.coin import check_coutdown


@dp.message_handler(Farm())
async def _farm(message: types.Message):
    if check_coutdown(message.from_user.id):
        coins = coin_count(message.from_user.id) 
        add_coin(message.from_user.id, coins)
        await message.reply(msg_text.FARM.format(coins))
    else:
        hours, minutes, seconds = get_countdown(message.from_user.id)
        await message.reply(msg_text.FARM_COOLDOWN.format(hours, minutes, seconds))
        

@dp.message_handler(Wallet())
async def money(message: types.Message, user):
    await message.reply(msg_text.WALLET.format(user.coins), reply_markup=wallet_ikb())
    
    
# @dp.callback_query_handler(Text('market'))
# async def money(callback: types.CallbackQuery):
#     await callback.message.edit_text(f"Товар:", reply_markup=market_ikb())


@dp.callback_query_handler(Text('add_command'))
async def money(callback: types.CallbackQuery):
    text="""
Стоимость добавления команды: 250$ 🐽

Чтобы добавить новую команду, используйте формат: `/add (слово):(ответ)`

Пример команды:
`/add да:ваш ответ`"""
    await callback.message.edit_text(text)

# @dp.message_handler(Command("add"))
# async def money(message: types.Message):
#     parts = message.get_args().split(':')
#     from utils.json_utils import add_command_to_group
#     add_command_to_group(message.chat.id, parts[0], parts[1])
#     await message.answer("Команда добавленна")


@dp.callback_query_handler(Text('del_command'))
async def money(callback: types.CallbackQuery, user):
    await callback.message.edit_text(f"Пока нит удаления", reply_markup=market_ikb())



# @dp.callback_query_handler(Text('add_command'))
# async def money(callback: types.CallbackQuery, user):
#     await bot.send_message(chat_id=callback.from_user.id, 
#                         text="""
# Стоимость добавления команды: 250$ 🐽

# Чтобы добавить новую команду, используйте формат: `/add (слово):(ответ)`

# Пример команды:
# `/add да:ваш ответ`""", 
#                         reply_markup=market_ikb())

@dp.callback_query_handler(Text('del_command'))
async def money(callback: types.CallbackQuery, user):
    await callback.message.edit_text(f"Товар:", reply_markup=market_ikb())
