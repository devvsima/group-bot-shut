from peewee import CharField, BigIntegerField, DateTimeField, ForeignKeyField, TextField
import json
from playhouse.db_url import connect

from datetime import datetime
from ..connect import db, BaseModel

from .users import Users

class Groups(BaseModel):
   group_id = BigIntegerField(primary_key=True)  # Используем BigIntegerField для идентификатора группы
   title = CharField()
   data = TextField(null=True)  # Поле для хранения JSON-данных в виде строки

   def set_data(self, dictionary):
      """Устанавливаем данные в поле data в формате JSON."""
      self.data = json.dumps(dictionary)

   def get_data(self):
      """Получаем данные из поля data как словарь."""
      return json.loads(self.data)
class UserGroup(BaseModel):
   user = ForeignKeyField(Users, backref='groups')  # Связь с пользователем
   group = ForeignKeyField(Groups, backref='members')  # Связь с группой

