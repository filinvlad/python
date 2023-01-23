
with open('5.txt', 'w') as file_obj:
    line = input('Введите цифры через пробел: ')
    file_obj.writelines(line)
    a = line.split()
    print(sum(map(int, a)))
