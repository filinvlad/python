a = input("Введите список: ")  # Просим ввести данные
a = list(a)  # присваиваем тип данных(список)
a[:-1:2], a[1::2] = a[1::2], a[:-1:2]  # определяем границы списка и шаг замены элементов,меняем
print(''.join(a))  # выводим на экран
