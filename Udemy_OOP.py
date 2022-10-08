"""
Задача 1
Реализуйте методы класса Line (линия), который принимает на вход координаты в виде двух
 кортежей, и возвращает угол наклона (slope) и длину (distance) этой линии.

Длину отрезка рассчитаю по теореме Пифагора: АВ = ((X[b] - X[a])**2 + (Y[b] - Y[a])**2))**0.5
Для расчета угла формула: угол = (у2-у1) / (х2-х1)
# Пример
coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)
li.distance()
9.433981132056603
li.slope()
1.6
"""


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2-y1)/(x2-x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())

"""
Задача 2

Реализуйте методы класса.

c = Cylinder(2, 3)
c.volume()
56.52
c.surface_area()
94.2
"""


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * 3.14 * self.radius ** 2

    def surface_area(self):
        top = 3.14 * self.radius ** 2
        return (2 * top) + (2 * 3.14 * self.radius * self.height)


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())
