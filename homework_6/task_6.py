number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число: "))
math_operator = input("Выберите оператор (+, -, *, /): ")

is_valid = True

if math_operator == "+":
    result = number_1 + number_2
elif math_operator == "-":
    result = number_1 - number_2
elif math_operator == "*":
    result = number_1 * number_2
elif math_operator == "/":
    if number_2 == 0:
        print("Ошибка: деление на ноль невозможно!")
        is_valid = False
    else:
        result = number_1 / number_2
else:
    print("Ошибка: неизвестный оператор! Используйте +, -, *, /")
    is_valid = False

if is_valid:
    print(f"Результат: {number_1} {math_operator} {number_2} = {result}")