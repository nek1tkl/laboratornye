# Определение класса Worker
class Worker:
    'doc class Worker'
    count = 0  # Переменная класса для подсчета количества созданных объектов

    # Конструктор класса
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Worker.count += 1  # Увеличиваем счетчик при создании нового объекта

    # Метод для отображения информации о рабочем
    def display(self):
        print("Worker:")
        print("{} {}".format(self.name, self.surname))

w1 = Worker("Ivan", "Ivanov")# Создание объекта Worker с именем "Ivan" и фамилией "Ivanov"
print("w1.count: ", w1.count)# Вывод количества созданных объектов Worker
w2 = Worker("Alexei", "Petrov")# Создание объекта Worker с именем "Alexei" и фамилией "Petrov"
print("w2.count: ", w2.count)# Вывод количества созданных объектов Worker
print("w1.count: ", w1.count)# Вывод количества созданных объектов Worker через объект w1
print("Worker.count: {0}\n".format(Worker.count))# Вывод количества созданных объектов Worker через класс Worker
print("Worker.__name__: ", Worker.__name__)# Вывод свойства __name__ класса Worker
print("Worker.__dict__: ", Worker.__dict__)# Вывод словаря __dict__ класса Worker
print("Worker.__doc__: ", Worker.__doc__)# Вывод документации __doc__ класса Worker
print("Worker.__bases__: ", Worker.__bases__)# Вывод кортежа __bases__ класса Worker

# Определение класса Animal
class Animal:
    'doc class Animal'
    count = 0  # Переменная класса для подсчета количества созданных объектов

    # Конструктор класса
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.count += 1  # Увеличиваем счетчик при создании нового объекта
        self.id = Animal.count  # Присваиваем объекту уникальный идентификатор

    # Метод для отображения информации о животном
    def display(self):
        print("Animal count: {}".format(self.id))
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))

# Создание объектов класса Animal
animal1 = Animal("Кот белый", 1)
animal2 = Animal("Кот серый", 2)
animal3 = Animal("Кот черный", 3)

# Вывод информации о созданных объектах Animal
animal1.display()
animal2.display()
animal3.display()
