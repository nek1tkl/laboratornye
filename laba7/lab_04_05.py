import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1) 

# Базовый класс Person
class Person:
    # Инициализация объекта
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    # Метод для отображения информации о человеке
    def display(self):
        print(f"Имя: {self.firstname}")
        print(f"Фамилия: {self.lastname}")
        print(f"Возраст: {self.age}")

# Класс Student, наследуется от Person
class Student(Person):
    # Консткрутор с дополнительными атрибутами
    def __init__(self, firstname, lastname, age, student_id, record_book):
        super().__init__(firstname, lastname, age)  # Вызов конструктора родительского класса
        self.student_id = student_id # Идентификатор студента
        self.record_book = record_book  # Оценки

    # Переопределение метода display для вывода информации о студенте
    def display(self):
        super().display()  # Вызов метода display из родительского класса
        print(f"ID студента: {self.student_id}")
        print("Оценки:")
        print(f"Пятерки: {self.record_book[0]}")
        print(f"Четверки: {self.record_book[1]}")
        print(f"Тройки: {self.record_book[2]}")
        print(f"Двойки: {self.record_book[3]}")

# Создаем объекты класса Student
student1 = Student("Иван", "Иванов", 20, "1", [5, 4, 3, 2])
student2 = Student("Петр", "Петров", 22, "2", [4, 4, 4, 3])
student3 = Student("Алексей", "Сидоров", 21, "3", [5, 5, 5, 5])

# Вывод информации о студентах на экран
print("Информация о студенте 1:")
student1.display()
print("\nИнформация о студенте 2:")
student2.display()
print("\nИнформация о студенте 3:")
student3.display()

# Класс Professor, также наследуется от Person
class Professor(Person):
    # Конструктор с дополнительными атрибутами
    def __init__(self, firstname, lastname, age, professor_id, degree):
        super().__init__(firstname, lastname, age)  # Вызов конструктора родительского класса
        self.professor_id = professor_id
        self.degree = degree
    
    # Переопределение метода display для вывода информации о профессоре
    def display(self):
        super().display()  # Вызов метода display из родительского класса
        print("ID профессора:", self.professor_id)
        print("Научная степень:", self.degree)

# Создаем объекты класса Professor для проверки работы методов
professor1 = Professor("Ольга", "Иванова", 45, "1", "Доктор наук")
professor2 = Professor("Марина", "Петрова", 50, "2", "Кандидат наук")
professor3 = Professor("Мария", "Сидорова", 55, "3", "Профессор")

# Выводим информацию о профессорах на экран
print("Информация о профессоре 1:")
professor1.display()
print("\nИнформация о профессоре 2:")
professor2.display()
print("\nИнформация о профессоре 3:")
professor3.display()
