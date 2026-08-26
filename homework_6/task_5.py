import random

min_number = 1
max_number = 20
max_Attempts = 3

unknown_number = random.randint(min_number, max_number)
attempts = max_Attempts

print(f"Я загадал число от {min_number} до {max_number}. У тебя {max_Attempts} попыток!")

while attempts > 0:
    guess = int(input(f"Попытка {max_Attempts - attempts + 1}. Введите число: "))

    if guess == unknown_number:
        print("Ты угадал! Отличная работа.")
        break
    elif guess < unknown_number:
        print("Слишком мало!")
    else:
        print("Слишком много!")

    attempts -= 1

    if attempts > 0:
        print(f"Осталось попыток: {attempts}")
    else:
        print(f"Игра окончена! Загаданное число было: {unknown_number}")