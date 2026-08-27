

raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

# Разбить строку на элементы и получаем список c помощью .split()
data_user = raw_user_record.split(";")
#print(data_user)

# Удалить пробелы в начале и конце элемента с помощью .strip()
user_id = data_user[0].strip()
last_name = data_user[1].strip()
city = data_user[2].strip()
status = data_user[3].strip()
# withou_spaces = user_id,last_name,city,status
# print(withou_spaces)

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