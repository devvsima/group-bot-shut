import json
import os
# Функция для загрузки всех команд из файла
def load_commands(filename='commands.json'):
    if not os.path.exists(filename):
        return {}  # Если файл не найден, возвращаем пустой словарь

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            if os.path.getsize(filename) == 0:  # Проверяем, пуст ли файл
                return {}  # Если файл пустой, возвращаем пустой словарь
            return json.load(f)  # Загружаем и возвращаем весь словарь команд
    except json.JSONDecodeError:
        print("Ошибка: файл содержит недопустимый JSON.")
        return {}  # Если ошибка декодирования, возвращаем пустой словарь

# Функция для сохранения всех команд в файл
def save_commands(commands, filename='commands.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(commands, f, ensure_ascii=False, indent=4)

# Функция для добавления команды в определённую группу
def add_command_to_group(group_id, command, response, filename='commands.json'):
    # Загружаем все команды
    commands = load_commands(filename)

    # Проверяем, существует ли группа
    if group_id not in commands:
        commands[group_id] = {}  # Если нет, создаем новую группу

    # Добавляем или обновляем команду в группе
    commands[group_id][command] = response

    # Сохраняем обновленный словарь в файл
    save_commands(commands, filename)