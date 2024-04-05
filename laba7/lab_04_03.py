import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1) 
import math

# Определение базового класса Geometric
class Geometric:
    # Метод для вычисления площади
    def calculateArea(self):
        print("Calculating area")

# Определение класса Square, унаследованного от Geometric
class Square(Geometric):
    # Конструктор класса Square
    def __init__(self, a):
        self.side = a  # Длина стороны квадрата
        
    # Метод для вычисления периметра квадрата (приватный)
    def _perimeter(self):
        print("Perimeter of Square {}: {}\n".format(self.side, self.side*4))
    
    # Переопределенный метод для вычисления площади квадрата
    def calculateArea(self):
        print("Area of Square {}: {}\n".format(self.side, pow(self.side, 2)))

# Определение класса Circle, унаследованного от Geometric
class Circle(Geometric):
    # Конструктор класса Circle
    def __init__(self, radius):
        self.__radius = radius  # Приватный радиус окружности
    
    # Переопределенный метод для вычисления площади окружности
    def calculateArea(self):
        area = math.pi * (self.__radius ** 2)  # Формула для вычисления площади окружности: Pi * r^2
        print("Площадь окружности {}: {:.2f}\n".format(self.__radius, area))

# Создание объекта базового класса Geometric
geom = Geometric()
geom.calculateArea()

# Создание объекта класса Square и вызов методов для вычисления площади и периметра квадрата
sq = Square(5)
sq.calculateArea()
sq._perimeter()

# Создание объекта класса Circle и вызов метода для вычисления площади окружности
cir = Circle(3)
cir.calculateArea()

# Проверка наследования и экземпляров
print("Check subclass Square: ", issubclass(Square, Geometric))
print("Check subclass Circle: ", issubclass(Circle, Geometric))
print("Check instance sq -> Square: ", isinstance(sq, Square))
print("Check instance sq -> Geometric: ", isinstance(sq, Geometric))
print("Check instance sq -> dict: ", isinstance(sq, dict))

# Вывод базовых классов для каждого класса
print("Geometric.__bases__: ", Geometric.__bases__)
print("Square.__bases__: ", Square.__bases__)
print("Circle.__bases__: ", Circle.__bases__)
