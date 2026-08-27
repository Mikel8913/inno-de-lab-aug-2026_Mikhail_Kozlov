celsius = float(input("Введите температуру в градусах Цельсия: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius:g}°C это {fahrenheit:.1f}°F".replace(".", ","))