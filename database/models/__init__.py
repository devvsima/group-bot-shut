from .users import Users
from .group import Groups, UserGroup
from ..connect import db


db.create_tables([Users, Groups, UserGroup])