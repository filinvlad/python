t = int(input("Введите время в секундах:"))  # просим пользователя ввести время в секундах

h = t // 3600  # вычисляем количество часов в введенном числе
m = ((t % 3600) // 60)  # вычисляем количество минут в остатке от часов
s = (t - h * 3600 - m * 60)  # вычисляем оставшиеся секунды

print(f"{h:02d}ч:{m:02d}м:{s:02d}с")  # выводим на экран данные в формате чч:мм:сс