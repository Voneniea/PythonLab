from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, id):
        self.__id = id

    @abstractmethod
    def move(self, dx, dy):
        pass

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def __str__(self):
        return f"Фигура(ID: {self.__id})"


class Rectangle(Shape):
    def __init__(self, id, x1, y1, x2, y2):
        super().__init__(id)
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def move(self, dx, dy):
        self.__x1 += dx
        self.__y1 += dy
        self.__x2 += dx
        self.__y2 += dy

    def is_include(self, other):
        if isinstance(other, Pentagon):
            for x, y in other.get_vertices():
                if not (self.__x1 <= x <= self.__x2 and self.__y1 <= y <= self.__y2):
                    return False
            return True
        else:
            raise ValueError("Неподдерживаемый тип для проверки включения")

    def get_coordinates(self):
        return (self.__x1, self.__y1, self.__x2, self.__y2)

    def set_coordinates(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def __str__(self):
        return f"Прямоугольник(ID: {self.get_id()}, Координаты: ({self.__x1}, {self.__y1}), ({self.__x2}, {self.__y2}))"


class Pentagon(Shape):
    def __init__(self, id, vertices):
        super().__init__(id)
        self.__vertices = vertices

    def move(self, dx, dy):
        self.__vertices = [(x + dx, y + dy) for x, y in self.__vertices]

    def get_vertices(self):
        return self.__vertices

    def set_vertices(self, vertices):
        self.__vertices = vertices

    def __str__(self):
        return f"Пятиугольник(ID: {self.get_id()}, Вершины: {self.__vertices})"


# Пример использования
try:
    rect = Rectangle("R1", 0, 0, 4, 4)
    pentagon = Pentagon("P1", [(1, 1), (2, 2), (3, 1), (2.5, 0.5), (1.5, 0.5)])

    print(rect)
    print(pentagon)

    if rect.is_include(pentagon):
        print("Пятиугольник включен в прямоугольник")
    else:
        print("Пятиугольник не включен в прямоугольник")

    rect.move(2, 2)
    pentagon.move(1, 1)

    print("После перемещения:")
    print(rect)
    print(pentagon)

    if rect.is_include(pentagon):
        print("Пятиугольник включен в прямоугольник")
    else:
        print("Пятиугольник не включен в прямоугольник")

except ValueError as e:
    print(f"Ошибка: {e}")