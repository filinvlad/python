my_list = [7, 5, 3, 3, 2]

a = False
while not a:
    b = int(input('Введите новое значение рейтинга: '))
    if b < 0:
        print('Должно быть положительное число')
        continue
    for el in my_list:
        my_list.append(b)
        my_list.sort(reverse=True)
        a = True
        break
print(f'Измененный рейтинг: {my_list}')
