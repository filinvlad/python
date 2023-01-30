class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def mass(self):
        length = self._length
        width = self._width
        weight = self.weight
        depth = self.depth
        a = length * width * weight * depth / 1000
        print(f"Масса асфальта: {length} м * {width} м * {weight} кг * {depth} см = ", a, "т")


r = Road(14, 3000, 25, 6)
r.mass()