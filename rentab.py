a = int(input("Введите выручку предприятия: "))  # просим ввести выручку
b = int(input("Введите издержки предприятия: "))  # просим ввести издержки

if a - b > 0:  # если есть прибыль, выводим на экран
    print(f"Прибыль предприятия: {a - b}")
    print(f"Рентабельность предприятия:{(((a - b) / a) * 100):.2f}%")
    c = int(input("Введите численность работников предприятия: "))
    print(f"Прибыль на работника:{((a - b) / c):.2f}")
elif a - b < 0:  # иначе убыток, выводим на экран
    print(f"Убыток предприятия: {b - a}")
else:
    print("Выручка равна издержкам")
