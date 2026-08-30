raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

# разбиваем строку, убираем пробелы у каждого элемента
data_user = [item.strip() for item in raw_user_record.split(";")]
# print(data_user)

# раскладываем элементы списка по отдельным переменным
user_id, last_name, city, status = data_user

# Префикс "UID-" добавил
user_id = f"UID-{user_id}"

# "_" заменить на пробел и заглавные буквы  привезти к правильному регистру
last_name = last_name.replace("_", " ").title()
# print(last_name)

# к верхнему регистру приводим
city = city.replace("_", " ").upper()
# print(city)

# к нижнему регистру приводим
status = status.lower()
# print(status)
# собираем через разделитель "|"
processed_elements = " | ".join([user_id, last_name, city, status])

print(f"Нормализованная запись: {processed_elements}")
