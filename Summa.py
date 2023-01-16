def my_sum(my_list):
    a = 0
    for i in my_list:
        try:
            a += int(i)
        except ValueError:
            continue
    return a

n_sum = 0
while True:
    b = input("Введите строку чисел, разделенных пробелом: ").split()
    n_sum += my_sum(b)
    if n_sum != 0:
        print(f"Для завершения введите '!'\nСумма введенных чисел равна: {n_sum}")
    if b.count('!') > 0:
        break
