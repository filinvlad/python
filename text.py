my_file = open('test.txt', 'w', encoding='utf-8')
line = input('Введите текст \n')
while line:
    my_file.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break
