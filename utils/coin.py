from datetime import datetime, timedelta

last_usage = {}
cooldown = timedelta(hours=6)

def check_coutdown(user_id):
    current_time = datetime.now()
    if user_id in last_usage:
        time_since_last_use = current_time - last_usage[user_id]
    
        # Если прошло меньше 6 часов, выводим сообщение об ожидании
        if time_since_last_use < cooldown:
            return False
            
    last_usage[user_id] = current_time
    return True


def get_countdown(user_id):
    current_time = datetime.now()
    time_since_last_use = current_time - last_usage[user_id]

    remaining_time = cooldown - time_since_last_use
    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60) 
    return hours, minutes, seconds

def coin_count(user_id):
    from random import randint
    current_time = datetime.now()
    time_since_last_use = current_time - last_usage[user_id]
    hours_since_last_use = time_since_last_use.total_seconds() / 3600
    multiplier = 1 + (hours_since_last_use - 6) * 0.1  # Начинаем рост после 6 часов
    multiplier = 1
    return randint(1, 51) * multiplier
