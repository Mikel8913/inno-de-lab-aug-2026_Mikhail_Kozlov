db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}
#  Извлекаем значения host и port
connection = db_config["connection"]
host = connection["host"]
port = connection["port"]

# Проверка наличие ключа ssl_settings и ssl_mode, .get() с дефолтным значением verify-full
ssl_mode = connection.get("ssl_settings", {}).get("ssl_mode", "verify-full")

# замена  user на admin
connection["user"] = "admin"

#  новый параметр max_connections
connection["max_connections"] = 100

#  SSL Mode
print(f"SSL Mode: {ssl_mode}")

#  содержимое connection через .items()
print("Параметры соединения:")
for key, value in connection.items():
    print(f"* {key}: {value}")
