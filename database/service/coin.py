from ..models.users import Users
from utils.logging import logger


def add_coin(id, coins):
    Users.update(coins=Users.coins + coins).where(Users.id == id).execute()

