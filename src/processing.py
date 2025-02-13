from datetime import datetime
from typing import List


def sort_dates(data: List[dict], order: str = 'descending') -> List[dict]:
    """
    Сортирует список словарей по дате.

    Args:
    - data: Список словарей с ключом 'date'.
    - order: Порядок сортировки ('descending' или 'ascending').

    Returns:
    - Отсортированный список.
    """
    if order == 'descending':
        return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=True)
    else:
        return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=False)


# Пример использования
data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

sorted_data = sort_dates(data, 'descending')
print(sorted_data)


def filter_state(data: List[dict], state: str = 'EXECUTED') -> List[dict]:
    """
    Фильтрует список словарей по состоянию.

    Args:
    - data: Список словарей с ключом 'state'.
    - state: Состояние для фильтрации.

    Returns:
    - Отфильтрованный список.
    """
    result = []
    for item in data:
        if item['state'] == state:
            result.append(item)
    return result


# Пример использования
data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

filtered_data = filter_state(data, 'EXECUTED')
print(filtered_data)
