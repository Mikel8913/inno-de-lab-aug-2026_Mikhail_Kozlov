import random


unknown_number = random.randint(1, 20)
attempts = 5
print("Я загадал число от 1 до 20. У тебя 5 попыток!")
while attempts > 0:
    guess_number = int(input(f"Попытка {6 - attempts}. Введите число: "))
    if guess_number == unknown_number:
        print("Ты угадал! Отличная работа.")
        break
    elif guess_number < unknown_number:
        print("Слишком мало!")
    else:
        print("Слишком много!")
    attempts -= 1
    if attempts > 0:
        print(f"Осталось попыток: {attempts}")
    else:
        print(f"Игра окончена! Загаданное число было: {unknown_number}")