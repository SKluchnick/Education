#1. Модифицируйте класс Point следующим образом:
# обеспечьте проверку значений координат (только числа),
# добавьте метод, который бы позволял сравнивать точки (если координаты точек совпадают - точки равны)
class Point:
    _x = 0
    _y = 0

    def __init__(self, x, y):
        if not isinstance(x, int) and isinstance(y, int):
            print("Mistake only int")
            return
        self._x, self._y = x, y

    @property
    def x(self):
        return self._x

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return f'Point with x is {self._x} and y is {self._y}'

    @staticmethod
    def check_eq_coord(v1, v2):
        return v1 == v2

    def __eq__(self, other):
        return  self._x == other



p1 = Point(5, 5)
p2 = Point(5, 5)
print(p1.check_eq_coord(5,5))

print(p1 == p2)

#2. Модифицируйте класс Line следующим образом:
# обеспечьте проверку точек начала и конца при создании линии в __init__ (точки начала и конца отрезка не должны совпадать)
# модифицируйте метод __str__ так чтобы он отдавал информацию в формате \
#     ("Line with points [информация о точке начала] [информация о точке конца] and length [длина]")

class Line:
    _start_point = Point(0, 0)
    _finish_point = Point(0, 0)

    def __init__(self, first_point, second_point):
        if not isinstance(first_point, Point) or \
                not isinstance(second_point, Point) or \
                not self._check_points_coord(first_point, second_point):
            raise Exception
        if  first_point == second_point:
            raise Exception
        self._start_point = first_point
        self._finish_point = second_point

    def length(self):
        return ((self._start_point.x - self._finish_point.x) ** 2 + (
                self._start_point.y - self._finish_point.y) ** 2) ** 0.5

    # позволяет делать метод без self
    @staticmethod
    def _check_points_coord(p1, p2):
        return not (p1.x == p2.x and p1.y == p2.y)



line1 = Line(p1, p2)
