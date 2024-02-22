"""
<Назначение модуля>
"""

# TODO(Vlad): В названиях файлов только маленькие буквы. Посмотри PEP 8.

import collections 


def digit_sum(num: int) -> int:
    """
    Возвращаем сумму цифр числа, преобразованного в строку

    :param num: исходное число для преобразования
    :return: сумма цифр числа, преобразованного в строку
    """
    digits = [int(char) for char in str(num)]
    return sum(digits)


def is_valid(x: int, y: int, max_limit: int = 25) -> bool:
    """
    Проверяем, что сумма цифр координат X и Y не превышает заданный предел

    :param blabla
    :return blabla
    """
    coord_sum = digit_sum(x) + digit_sum(y)
    return coord_sum <= 25  

def count_visited_cells(start_x, start_y):
    visited = set()  # Множество для хранения посещенных клеток
    cells = collections.deque([(start_x, start_y)])  # Очередь для обхода клеток
    count = 0  # Счетчик посещенных клеток

    while cells:  # Пока очередь не пуста
        x, y = cells.popleft()  # Извлекаем клетку из очереди
        if (x, y) not in visited and is_valid(x, y):  # Если клетка еще не посещалась и доступна
            visited.add((x, y))  # Добавляем клетку в посещенные
            count += 1  # Увеличиваем счетчик посещенных клеток
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Возможные направления движения
            for dx, dy in directions:  # Перебираем направления
                new_x, new_y = x + dx, y + dy  # Вычисляем новые координаты
                if is_valid(new_x, new_y):  # Если клетка доступна
                    cells.append((new_x, new_y))  # Добавляем новую клетку в очередь
    return count

start_x, start_y = 1000, 1000
print("Количество посещенных клеток:", count_visited_cells(start_x, start_y))
