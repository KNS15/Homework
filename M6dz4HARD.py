import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = []
        self.set_color(*color)
        self.filled = False
        self._create_sides(*sides)

    def _create_sides(self, *sides):
        if len(sides) != self.__class__.sides_count:
            self.set_sides(*[1] * self.__class__.sides_count)
        else:
            self.set_sides(*sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, codes):
        if not isinstance(codes, tuple or list) or not len(codes) == 3:
            return False
        elif not all(isinstance(code, int) for code in codes) or any(isinstance(code, bool) for code in codes):
            return False
        elif not all(0 <= ele < 256 for ele in codes):
            return False
        else:
            self.filled = True
            return True

    def set_color(self, *codes):
        if self.__is_valid_color(codes):
            self.__color = list(codes)

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = list(sides)

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, sides):
        if not isinstance(sides, tuple or list):
            return False
        elif not all(isinstance(side, int) for side in sides) or any(isinstance(side, bool) for side in sides):
            return False
        elif not len(sides) == self.__class__.sides_count or not sides:
            return False
        elif not all(side > 0 for side in sides):
            return False
        else:
            return True

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = len(self) / (2 * 3.14)

    def get_square(self):
        return "3.14 * {} ** 2", format(self.__radius)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = self.get_sides()
        self.base = max(self.__sides)
        self.__height = 2 * self.get_square() / self.base

    def get_square(self):
        x = len(self) / 2
        return math.sqrt(x * (x - self.__sides[0]) * (x - self.__sides[1]) * (x - self.__sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def _create_sides(self, *sides):
        if len(sides) != 1:
            self.set_sides(*[1] * self.__class__.sides_count)
        else:
            self.set_sides(*[*sides] * self.__class__.sides_count)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
