"""
Вам поручили написать простой парсер для значений, которые вы получаете из внешнего API.
На вход вы получаете список строк, в которых нечетные слова - это ключи, а четные слова - это их значения.
Ключи, значения которых вы должны учитывать - id, name, last_name, age, salary, position. Остальные ключи и их значения
не должны попасть в итоговый набор данных.
Ключ age и id должен быть представлен в формате int.
Ключ salary должен быть представлен в формате Decimal.

Ограничения:
1) На вход подается информация по сотрудникам, где всегда четное количество слов
2) Там, где нужны числовые значения, числа могут быть преобразованы к int или Decimal без ошибок.

После парсинга вы должны получить структуру данных, описанную ниже  list[dict[str, int | str]]:
[
    {'id': 1, 'name': 'Ivan', 'last_name': 'Ivanov', 'age': 29, 'position': developer, 'salary': Decimal('10000')},
    ...
]

для тестирования запустить pytest 1_task/test.py
"""

import os
from decimal import Decimal
from types import MappingProxyType

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '\n'


def read_file(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_employees_info() -> list[str]:
    """Внешнее апи, которое возвращает вам список строк с данными по сотрудникам."""
    return read_file(os.path.join(
        BASE_DIR, '1_task', 'input_data.txt',
    )).split(SPLIT_SYMBOL)


def get_parsed_employees_info() -> list[dict[str, int | str]]:
    employees_info = get_employees_info()
    parsed_employees_info = []
    dictionary_sample = {
        'id': int,
        'age': int,
        'name': str,
        'salary': Decimal,
        'position': str,
        'last_name': str
    }
    dictionary_sample = MappingProxyType(dictionary_sample)
    for employees in employees_info:
        employees = employees.split(" ")
        employees_dict = {}
        for words_number in range(0, len(employees) // 2):
            key = employees[2 * words_number]
            value = employees[2 * words_number + 1]
            my_type = dictionary_sample.get(key)
            if my_type:
                value = my_type(value)
                employees_dict[key] = value
        parsed_employees_info.append(employees_dict)
    return parsed_employees_info


print(get_parsed_employees_info())
