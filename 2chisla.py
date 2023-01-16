def my_rez():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        c = a / b
    except ValueError:
        return 'Ошибка значения'
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return c
    if b != 0:
        return (c)


print(f"Ответ: {my_rez()}")
