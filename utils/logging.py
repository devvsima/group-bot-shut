from logging import getLogger
from data.config import DIR
from loguru import logger


logger.add(
    f"{DIR}/logs/logs.log", 
    format='[{time}] [{level}] [{file.name}:{line}]  {message}', 
    level='DEBUG', 
    rotation='1 week',
    compression='zip')

getLogger('aiogram').addFilter(lambda r: r.getMessage().find('Field \'database_user\' doesn\'t exist in') == -1)

# import re
# from datetime import datetime, timedelta

# # Путь к лог-файлу
# log_file = "./logs/logs.log"

# # ID пользователя, для которого нужно подсчитать сообщения
# user_id = "743347029"

# # Дата начала и конца периода
# now = datetime.now()
# start_date = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
# end_date = now

# # Регулярное выражение для поиска данных в логе
# log_pattern = re.compile(r"\[(.*?)\] \[.*?\] \[.*?:.*?\]  User ID: (\d+), Message: .*")

# # Подсчёт сообщений
# message_count = 0
# with open(log_file, "r", encoding="utf-8") as file:
#     for line in file:
#         match = log_pattern.match(line)
#         if match:
#             log_time = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S")
#             log_user_id = match.group(2)
#             if start_date <= log_time <= end_date and log_user_id == user_id:
#                 message_count += 1

# print(f"Количество сообщений от пользователя {user_id} за месяц: {message_count}")
