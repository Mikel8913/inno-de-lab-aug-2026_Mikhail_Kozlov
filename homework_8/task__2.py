import time
from typing import Callable, Any

PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8


def performance_logger(func: Callable) -> Callable:
    """
    Декоратор для замера времени выполнения функции
    Args:
        func (Callable): Целевая функция, время которой
            нужно замерить и залогировать.
    Returns:
        Callable: Обёртка, которая выполняет func с переданными
            аргументами, замеряет время его работы, логирует результат
            и возвращает то же значение, что вернула func.
    """

    # внутренняя функцию-обёртку, которая принимает любые аргументы
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # время начала выполнения функции
        start = time.perf_counter()

        # функция с переданными аргументами
        result = func(*args, **kwargs)

        # затраченное время
        elapsed = time.perf_counter() - start

        print(f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' выполнена за {elapsed:.{TIME_DECIMALS}f} сек.")

        # возвращает результат оригинальной функции
        return result

    # возвращает функцию-обёртку
    return wrapper


@performance_logger
def get_sorted_report(sales_data: list[dict[str, str | float]]) -> list[dict[str, str | float]]:
    """Сортировка списка по убыванию total_sales.

    Args:
        sales_data (list[dict[str, str | float]]): Список словарей,каждый словарь содержит ключи "category"
            (str) и "total_sales" (float).

    Returns:
        list[dict[str, str | float]]: Отсортированный по убыванию
            "total_sales" список словарей.
    """
    # сортируем список по ключу "total_sales" в порядке убывания
    # Lambda-функция извлекает значение total_sales из каждого словаря
    return sorted(sales_data, key=lambda x: x["total_sales"], reverse=True)


# тестовый набор данных
test_sets = [
    [
        {"category": "Action", "total_sales": 4311.85},
        {"category": "Animation", "total_sales": 4656.30},
        {"category": "Children", "total_sales": 3655.55}
    ],
    [
        {"category": "Classics", "total_sales": 1200.10},
        {"category": "Comedy", "total_sales": 4000.00},
        {"category": "Documentary", "total_sales": 4000.00}
    ],
    [
        {"category": "Drama", "total_sales": 500.00}
    ]
]

print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")

# проходим по каждому тестовому набору
for i, data in enumerate(test_sets, 1):
    print(f"\n--- ТЕСТ {i} ---")

    # отсортированный список
    result = get_sorted_report(data)

    print("Топ категорий по выручке:")

    # проходим по отсортированному списку и выводим категории с нумерацией
    for j, item in enumerate(result, 1):
        print(f"{j}. {item['category']}: {item['total_sales']}")
