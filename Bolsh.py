def my_func(a, b, c):
    l = [a, b, c]
    l.sort(reverse=True)
    print(f"Аргументы: {l}")
    for i in range(len(l)):
        return(f"Сумма наибольших двух аргументов: {l[0] + l[1]}")

print(my_func(9, 3, 8))