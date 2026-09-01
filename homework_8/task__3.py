from typing import Any, Tuple, Optional

# Константа
DEFAULT_RETURN_INDEX_BASE = 10.0


def calculate_overdue_fine(
        movie_title: str,
        days_overdue: Any,
        fine_rate: float
) -> Optional[Tuple[float, float]]:
    """
    Безопасно рассчитывает штраф за просрочку и индекс оборачиваемости.

    Args:
        movie_title (str): Название фильма.
        days_overdue (Any): Количество дней просрочки(могут быть разные типы данных)
        fine_rate (float): Штраф за один день просрочки

    Returns:
        Optional[Tuple[float, float]]: Кортеж (total_fine, return_index) или None при ошибке

    Обрабатываемые ошибки:
        - TypeError: Некорректный тип данных для days_overdue
        - ValueError: Некорректное строковое значение
        - ZeroDivisionError: days_overdue равен 0
    """
    try:
        # преобразовать дни в число
        numeric_days = float(days_overdue)

        # рассчитываем штраф
        total_fine = numeric_days * fine_rate

        # индекс оборачиваемости
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

    except TypeError as error:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{movie_title}': {error}")
        return None

    except ValueError as error:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для '{movie_title}': {error}")
        return None

    except ZeroDivisionError as error:
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{movie_title}': {error}")
        return None

    finally:
        print("--- Проверка транзакции возврата завершена ---")

    return total_fine, return_index


print("=== ПРОВЕРКА ВОЗВРАТОВ ===")

# расчет
result = calculate_overdue_fine("Matrix", 5, 1.5)
if result is not None:
    total_fine, return_index = result
    print(f"Фильм: 'Matrix' | Итоговый штраф: {total_fine}$ | Индекс: {return_index}")

# ошибка значения (ValueError)
result = calculate_overdue_fine("Inception", "пять", 2.0)

# деление на ноль (ZeroDivisionError)
result = calculate_overdue_fine("Avatar", 0, 2.5)

# ошибка типа (TypeError)
result = calculate_overdue_fine("Interstellar", [3], 3.0)
