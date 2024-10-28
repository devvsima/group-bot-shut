from peewee import CharField, BigIntegerField, DateTimeField, ForeignKeyField
from datetime import datetime
from ..connect import db, BaseModel

from .users import Users

class Groups(BaseModel):
   group_id = BigIntegerField(primary_key=True)  # Используем BigIntegerField для идентификатора группы
   title = CharField()

class UserGroup(BaseModel):
   user = ForeignKeyField(Users, backref='groups')  # Связь с пользователем
   group = ForeignKeyField(Groups, backref='members')  # Связь с группой

