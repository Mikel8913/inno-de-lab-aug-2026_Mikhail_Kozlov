from typing import Any

# Константа
DEFAULT_RETURN_INDEX_BASE = 10.0


def calculate_overdue_fine(
        movie_title: str,
        days_overdue: Any,
        fine_rate: float
) -> tuple[float, float] | None:
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

        print(f"Фильм: '{movie_title}' | Итоговый штраф: {total_fine}$ | Индекс: {return_index}")
        return total_fine, return_index

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


print("=== ПРОВЕРКА ВОЗВРАТОВ ===")

calculate_overdue_fine("Matrix", 5, 1.5)
calculate_overdue_fine("Inception", "пять", 2.0)
calculate_overdue_fine("Avatar", 0, 2.5)
calculate_overdue_fine("Interstellar", [3], 3.0)
