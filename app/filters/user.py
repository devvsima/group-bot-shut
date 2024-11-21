from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from data.config import ADMINS
from datetime import datetime, timedelta

from utils.coin import check_coutdown

class Farm(BoundFilter):
    async def check(self, message: Message):
        return check_coutdown(message.from_user.id)
    
class ShuraChances(BoundFilter):
    async def check(self, message: Message):
        text = message.text.lower()
        return bool(text.startswith(('шура інфа', 'шура инфа', 'шура шансы', 'шура шанс', 'шура шанси')))
    
class ShuraInfo(BoundFilter):
    async def check(self, message: Message):
        text = message.text.lower()
        return bool(text.startswith(('шура мнение', 'шура думка')))
        
class ShuraWho(BoundFilter):
    async def check(self, message: Message):
        text = message.text.lower()
        return bool(text.startswith(('шура кто', 'шура хто')))
                                
class ShuraShip(BoundFilter):
    async def check(self, message: Message):
        text = message.text.lower()
        return bool(text in ['шип'])

class ShuraZov(BoundFilter):
    async def check(self, message: Message):
        text = message.text.lower()
        return bool(text in ['заклик гоев', 'заклик гоїв'])