class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_salary(self):
        return self._income['wage'] + self._income['bonus']


a = Position('Иван', 'Иванов', 'мастер', 80000, 30000)
print(f'Полные данные сотрудника: {a.name}, {a.surname}, {a.position}, {a.get_full_salary()}')
