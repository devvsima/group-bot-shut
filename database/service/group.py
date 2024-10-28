from ..models.users import Users
from ..models.group import Groups, UserGroup
from utils.logging import logger


def add_user_to_group(user_id, username, group_id, group_title):
    # Получаем или создаем пользователя
    user, created = Users.get_or_create(id=user_id, defaults={'username': username})

    # Получаем или создаем группу
    group, created = Groups.get_or_create(group_id=group_id, defaults={'title': group_title})

    # Добавляем пользователя в группу
    UserGroup.get_or_create(user=user, group=group)


def get_group_members(group_id):
    # Получаем группу по group_id
    group = Groups.get(Groups.group_id == group_id)
    
    # Получаем участников группы через связь UserGroup
    members = (
        Users
        .select()
        .join(UserGroup)
        .where(UserGroup.group == group)
    )
    
    # Собираем имена пользователей в список
    member_usernames = [user.username for user in members]
    return member_usernames