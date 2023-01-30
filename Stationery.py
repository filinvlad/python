class Stationery:
    title = "Канцелярские принадлежности"

    def draw(self):
        print()

class Pen(Stationery):
    def draw(self):

        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):

        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):

        print("Запуск отрисовки маркером")


s = Stationery()
print(s.title)
s.draw()

p_1 = Pen()
p_1.draw()

p_2 = Pencil()
p_2.draw()

h = Handle()
h.draw()