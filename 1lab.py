print("Замена чисел в списке")
print("Положительные числа заменяются на 1")
print("Отрицательные числа заменяются на -1")
print("Ноль остается без изменений")
print()

# Ввод количества чисел
while True:
    try:
        n = int(input("Введите количество чисел: "))
        if n > 0:
            break
        else:
            print("Количество должно быть больше нуля.")
    except ValueError:
        print("Ошибка ввода. Нужно ввести целое число.")

result = []

# Ввод и обработка чисел
for i in range(n):
    while True:
        try:
            value = int(input(f"Введите число № {i + 1}: " ))
            break
        except ValueError:
            print("Ошибка ввода. Нужно ввести целое число.")

    result.append(1 if value > 0 else (-1 if value < 0 else 0))

print()
print("Полученный список:")
print(result)

input("Нажмите Enter для завершения программы...")