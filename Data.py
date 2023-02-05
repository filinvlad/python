class Data:

    day_month_year = "06 - 2 - 2023"

    @classmethod
    def extract(cls):
        my_date = [int(el) for el in cls.day_month_year.split() if el != '-']
        cls.day, cls.month, cls.year = my_date
        print(*my_date)

    @staticmethod
    def valid():

        if 1 <= Data.day <= 31:
            if 1 <= Data.month <= 12:
                if 2023 >= Data.year >= 0:
                    return f"Все в порядке"
                else:
                    return f"Неправильный год"
            else:
                return f"Неправильный месяц"
        else:
            return f"Неправильный день"


Data.extract()
print(Data.valid())