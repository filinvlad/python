def my_func(x, y):
    try:
        y = y * (-1)
        s = x ** y
        s = 1 / s
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return s

print(my_func(2, -3))