# Расчет стоимости оптовой аренды фильмов
MAX_RENTAL_BATCH_LIMIT = 150.0


def calculate_rental_batch(
        quantity: int,
        rental_rate: float,
        discount: float = 0.0
) -> tuple[float, bool]:
    '''
        Рассчет стоимости партии дисков с учетом жанровой скидки.
        Args:
            quantity (int): Количевство дисков в партии.
            rental_rate (float): Цена аренды одного диска.
            discount (float): Скидка в процентах (0.0 по умолчанию).

        Returns:
            tuple[float, bool]: Кортеж из двух элементов.
    '''
    # итоговая стоимость партии со скидкой
    final_sum = round(
        quantity * rental_rate * (1 - discount), 2
    )
    # лимит стоимости превышен или нет
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT
    # возврат сумму и результата проверки лимита
    return final_sum, is_limit_exceeded


input_data = [
    ("Academy Dinosaur", 30, 2.99, 0.0),
    ("Affair Prejudice", 40, 4.99, 0.1),
    ("Agent Truman", 10, 1.99, 0.0),
    ("African Egg", 50, 3.50, 0.2),
]
print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")

# пример с позиционными аргументами
for i, (title_input, quantity_input, price_input, discount_input) in enumerate(input_data, start=1):
    final_sum, is_limit_exceeded = calculate_rental_batch(quantity_input, price_input, discount_input)
    print(f"Партия {i} ({title_input}): Сумма {final_sum}$. Превышение лимита: {is_limit_exceeded}")

# пример с именованными аргументами
final_sum, is_limit_exceeded = calculate_rental_batch(
    quantity=30,
    rental_rate=2.99,
    discount=0.0
)
print(f"Партия Academy Dinosaur (именованные аргументы): Сумма {final_sum}$. Превышение лимита: {is_limit_exceeded}")
