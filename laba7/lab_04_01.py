import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

import time
# Создание класса
class Ticket: 
    def __init__(self, date, name,deadline): # конструктор класса
        self.createDate = date
        self.owner = name
        self.deadline = deadline

    # деструктор класса для удаления объекта
    def __del__(self):
        print("Delete ticket:",time.asctime(self.createDate))

    # метод для отображения информации о тикете
    def display(self):
        print("Ticket:")
        print(" createDate:",time.asctime(self.createDate))
        print(" owner: ",self.owner)
        print(" deadline:",time.asctime(self.deadline))

# создание объекта класа
ticket1 = Ticket(time.localtime(),"Ivan Ivanov", time.strptime("17.12.2017", "%d.%m.%Y"))

# вызов метода
ticket1.display()


print("Owner: ", ticket1.owner)
print("Owner(getattr): ", getattr(ticket1,"owner")) # получение значения атрибута
print("hasattr: ", hasattr(ticket1,"owner"))# проверка наличия атрибута
setattr(ticket1,"owner","Alexei Petrov") # установка значение атрибута
print("Owner(setattr): ", ticket1.owner)

# Задание 2
delattr(ticket1,"owner") # удаление значения атрибута
# print("delattr: ", ticket1.owner)
# Возникает ошибка AttributeError, потому что нельзя обратиться к несуществующему атрибуту

print("delattr: ", getattr(ticket1, "owner", "Атрибут не найден")) # Исправленный вариант

# Задание 3
del ticket1 # удаление объекта

# print(ticket1)
# Возникает ошибка NameError, потому что нельзя обратиться к несуществующему объекту

# Задание 4
# Вывод времени компьютера в определенном формате
print(time.strftime("%d %b %Y %H:%M:%S", time.localtime()))

# Задание 5
# Создаем объект по строке
time_string = "17.07.2017 10:53:00"
time_object = time.strptime(time_string, "%d.%m.%Y %H:%M:%S")
print(time_object)