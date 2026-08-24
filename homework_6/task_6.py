number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число: "))
math_operator = input("Выберите оператор (+, -, *, /): ")

if math_operator == "+":
    result = number_1 + number_2
    print(f"Результат: {number_1} + {number_2} = {result}")

elif math_operator == "-":
    result = number_1 - number_2
    print(f"Результат: {number_1} - {number_2} = {result}")

elif math_operator == "*":
    result = number_1 * number_2
    print(f"Результат: {number_1} * {number_2} = {result}")

elif math_operator == "/":
    if number_2 == 0:
        print("Ошибка, делить на ноль нельзя!")
    else:
        result = number_1 / number_2
        print(f"Результат: {number_1} / {number_2} = {result}")

else:
    print("Ошибка, неизвестный оператор! Используйте +, -, *, /")