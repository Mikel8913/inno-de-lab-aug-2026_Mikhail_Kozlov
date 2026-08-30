raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10", "SUCCESS:0", "SUCCESS:250", "ERROR:200"]

#
transactions = [
    int(transaction.split(":")[1])  # разбиваем строку по : и преобразум вторую часть в целое число
    for transaction in raw_transactions  # перебираем каждую транзакцию
    if transaction.startswith("SUCCESS:")  # оставляем транзакции SUCCESS
       and int(transaction.split(":")[1]) > 0  # проверка, что сумма > 0
]

print(f"Очищенные транзакции: {transactions}")
