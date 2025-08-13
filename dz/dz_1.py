# a = 7
# b = 15
#
# print("a:", a)
# print("b:", b)
# c = a
# a = b
# b = c
# print("a", a)
# print("b", b)

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# num4 = int(input("Введите четвертое число: "))
# num5 = int(input("Введите пятое число: "))
#
# sum1 = num1 * num2 * num3 * num4 * num5
# sum2 = num1 + num2 + num3 + num4 + num5
# sum3 = sum2 / 5
# print("Введите пятизначное число:", num1 * 10000 + num2 * 1000 + num3 * 100 + num4 * 10 + num5)
# print("Произведение цифр числа:", sum1)
# print("Среднее арифметическое:", sum3)
#

# a = int(input("Введите число копеек от до до 99: "))
# kop = a
# if 11 <= kop <= 14:
#     print(a, "копеек")
# elif 1 <= a <= 10 or 15 <= a <= 99:
#     kop = kop % 10
#     if kop == 1:
#         print(a, "копейка")
#     elif 2 <= kop <= 4:
#         print(a, "копейки")
#     else:
#         print(a, "копеек")
# else:
#     print("Значения должны быть от 1 по 99")


# n = int(input("Количество символов: "))
# symbol = input("Тип символа: ")
# orient = int(input("0 - горизонтальная\n1 - вертикальная\nориентация линии: "))
#
# i = 0
# while i < n:
#     if orient == 1:
#         print(symbol)
#     else:
#         print(symbol, end=" ")
#     i += 1


# a = [int(input("-> ")) for i in range(int(input("n =")))]
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
#         print("Сумма отрицательных элементов", s)


# lst = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# new_lst = []
# i = 0
# for element in lst:
#     k = element
#     for q in lst:
#         if k == q:
#             i += 1
#     if i == 1:
#         new_lst.append(k)
#     i = 0
# print(new_lst)

# import random
#
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# mas1 = mas.copy()
# mas1.sort()
# print(mas1)
# min1 = mas1[0]
# print("min =", min1)
# ind = mas.index(min1)
# print("Min index =", ind)
# del mas[:ind]
# print(mas)

# import math
#
# tr = int(input("Выбор фигуры: \n1-Треугольник\n2-Прямоугольник\n3-Круг\n"))
# s = None
# if tr == 1:
#     a = int(input("Введите сторону "))
#     b = int(input("Введите сторону "))
#     c = int(input("Введите сторону "))
#     p = (a + b + c) / 2
#     s = math.sqrt(p * (p - a) * (p - b) * (p - c))
# elif tr == 2:
#     a = int(input("Введите сторону "))
#     b = int(input("Введите сторону "))
#     s = a * b
# elif tr == 3:
#     radius = int(input("Введите радиус "))
#     s = math.pi * radius ** 2
# else:
#     print("Такой фигуры не существует")
# print(round(s, 2))


# def prikol(count=20, symbol="-"):
#     print(count * symbol)
#
#
# prikol(10, "+")
# prikol(5, "*")
# prikol(15, "#")
# prikol(7)
# prikol()


# from random import randint
#
#
# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl1 = ran(0,5)
# print(tpl1)
# tpl2 = ran(-5,0)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print("0 = ", tpl3.count(0))
#


# s1 = "Python"
# s2 = "Programming language"
#
# a = set(s1) - set(s2)
# # print(a)
# for i in a:
#     print(i, end=" ")


# dict_sales = {'John': {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#               'Tom': {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#               'Anne': {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#               'Fionna': {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
#
# for x, y in dict_sales.items():
#     print(x)
#     for i, j in y.items():
#         print("\t", i, ": ", j, sep="")
#
# person = input("Имя: ")
# region = input("Регион ")
# print(dict_sales[person][region])
# new_date = int(input("Новое значение: "))
# dict_sales[person][region] = new_date
# print(dict_sales[person])


# student = {}
#
# n = int(input("Кол-во студентов "))
# s = 0
# for i in range(1, n + 1):  # 0 1 2
#     name = input(str(i) + "-й студент: ")
#     point = int(input("Балл: "))
#     student[name] = point
#     s += point
# average = s / n
# print(student)
# print("Средний балл:", round(average), "Студенты с баллом выше среднего: " ,sep="")
#
#
# for i in student:
#     if student[i] > average:
#         print(i)

# !!!
# s = 0
#
# def outer(a, b, c):
#     def inner(i, j):
#         return i + j
#
#     global s
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#
#
# outer(2, 4, 6)
# print(s)
# outer(5, 8, 2)
# print(s)
# outer(1, 6, 8)
# print(s)

# локальная

# def outer(a, b, c):
#     s = 0
#
#     def inner(i, j):
#         nonlocal s
#         s += i * j
#
#     inner(a, b)
#     inner(a, c)
#     inner(b, c)
#     return 2 * s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))


# from math import pi
#
# area = {
#     'Circle': lambda x: pi * x * x,
#     'Rectangle': lambda x, y: x * y,
#     'Trapezoid': lambda a, b, h: (a + b) * h / 2
# }
#
# print(area['Circle'](2))
# print(area['Rectangle'](10, 13))
# print(area['Trapezoid'](7, 5, 3))


# def avg(fn):
#     def wrap(*args):
#         print("Среднее арифметическое", *args, "=", fn(*args) / len(args))
#
#     return wrap
#
#
# @avg
# def summa(*args):
#     print("Сумма чисел:", *args, "=", sum(args))
#     return sum(args)
#
#
# summa(2, 3, 3, 4)


# s = "I am learning Python. hello, WORLD!"
# print(s.rfind('h') + 1)
# a = s[:s.find('h')]
# b = s[s.find('h'):s.rfind('h') + 1]
# c = s[s.rfind("h") + 1:]
# print(a + b[::-1] + c)


# 20.03.2025

# def negative_number(n):
#     if not n:
#         return 0
#     count = 0
#     if n[0] < 0:
#         count += 1
#     return count + negative_number(n[1:])
#
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(negative_number(lst))
#
#
#

# print("Я сделал это домашнее задание")


# f = open("test3.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# f.close()
#
# f = open("test3.txt", "r")
# read_line = f.readlines()
# print(read_line)
# f.close()
#
# pos1 = int(input("Pos1 = "))
# pos2 = int(input("Pos2 = "))
# if 0 <= pos1 < len(read_line) and 0 <= pos2 < len(read_line):
#     read_line[pos1], read_line[pos2] = read_line[pos2], read_line[pos1]
# else:
#     print("Такой строки нет")
#
# print(read_line)
#
# f = open("test3.txt", "w")
# f.writelines(read_line)
# f.close()


# 03.04.2025
# import os
# file_path = r"C:\Users\User\Desktop\Python\dz\test3.txt"
#
# if os.path.exists(file_path):
#     directory, name = os.path.split(file_path)
#     atime = os.path.getatime(file_path)
#     print(f"{name} ({directory})- время последнего доступа к файлу {atime} секунд ")
# else:
#     print(f"Файл {file_path} не существует")

# 08.04.2025
# from math import sqrt
#
#
# class Area:
#     __count = 0
#
#     @staticmethod
#     def triangle_area(a, b, c):
#         p = (a + b + c) / 2
#         Area.__count += 1
#         return sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def triangle_area_2(a, h):
#         Area.__count += 1
#         return 0.5 * a * h
#
#     @staticmethod
#     def square_area(a):
#         Area.__count += 1
#         return a ** 2
#
#     @staticmethod
#     def rectangle_area(a, b):
#         Area.__count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Area.__count
#
#
# print("Площадь треугольника по формуле Герона (3,4,5):", Area.triangle_area(3, 4, 5))
# print("Площадь треугольника по формуле Герона(13,14,15:", Area.triangle_area(13, 14, 15))
# print("Площадь треугольника через основание и высоту(6,7:", Area.triangle_area_2(6, 7))
# print("Площадь квадрата:", Area.square_area(7))
# print("Площадь квадрата:", Area.square_area(8))
# print("Площадь квадрата:", Area.square_area(9))
# print("Площадь прямоугольника:", Area.rectangle_area(2, 6))
# print("Количество подсчетов площади:", Area.get_count())
#

# 15.04.2025


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# # class RectBorder(Rect):
# #     ...
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# # shape2 = RectBorder(600,300,"1px","red")
# # shape2.show_rect()

# 17.04.2025

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, thin, typed, color):
#         super().__init__(width, height)
#         self.thin = thin
#         self.typed = typed
#         self.color = color
#
#     def show_rect(self):
#         super().show_rect()
#         print("Толщина", self.thin)
#         print("Тип рамки", self.typed)
#         print("Цвет рамки", self.color)
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px","solid","red")
# shape2.show_rect()

# 22.04.2022


# class Student:
#     def __init__(self,name):
#         self.name = name
#         self.note = self.Notebook()
#
#     def show(self):
#         print(self.name, end="")
#         self.note.show()
#         print(self.note.brand)
#
#     class Notebook:
#         def __init__(self):
#             self.brand = "HP"
#             self.cpu = "i7"
#             self.ram = 16
#
#         def show(self):
#             print(f"=> {self.brand}, {self.cpu}, {self.ram}")
#
# s1 = Student("Roman")
# s2 = Student("Vladimir")
# s1.show()
# s2.show()

# 24.04.2025

# Доработать занятие 29

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#
# c1 = Clock(1135)
# c2 = Clock(11351)
# # c4 = Clock(300)
# # c3 = c1 + c2
# # c1 += c2
# print(c1.get_format_time())
# print(c2.get_format_time())
# # print(c4.get_format_time())
# # print(c3.get_format_time())
# if c1 != c2:
#     print("Время равно")
# else:
#     print("Время разное")


# 29.05.2025 (дз 30) истек 4.05

# import math
# from abc import ABC, abstractmethod
#
#
# class Shape:
#     def __init__(self, color):
#         self.color = color
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def draw(self):
#         pass
#
#     @abstractmethod
#     def info(self):
#         pass
#
#
# class Square(Shape):
#     def __init__(self, side, color):
#         super().__init__(color)
#         self.side = side
#
#     def get_perimeter(self):
#         return self.side * 4
#
#     def get_area(self):
#         return self.side * self.side
#
#     def draw(self):
#         return ("*  " * self.side + "\n") * self.side
#
#     def info(self):
#         print(f"=== Квадрат ===\nСторона: {self.side}\nЦвет: {self.color}"
#               f"\nПлощадь: {self.get_area()}\nПериметр: {self.get_perimeter()}\n{self.draw()}\n")
#
#
# class Rectangle(Shape):
#     def __init__(self, length, width, color):
#         super().__init__(color)
#         self.length = length
#         self.width = width
#
#     def get_perimeter(self):
#         return (self.length + self.width) * 2
#
#     def get_area(self):
#         return self.length * self.width
#
#     def draw(self):
#         return ("*  " * self.width + "\n") * self.length
#
#     def info(self):
#         print(f"=== Прямоугольник ===\nДлина: {self.length}\nШирина: {self.width}\nЦвет: {self.color}"
#               f"\nПлощадь: {self.get_area()}\nПериметр: {self.get_perimeter()}\n{self.draw()}\n")
#
#
# class Triangle(Shape):
#     def __init__(self, side_1, side_2, side_3, color):
#         super().__init__(color)
#         self.side_1 = side_1
#         self.side_2 = side_2
#         self.side_3 = side_3
#
#     def get_perimeter(self):
#         return self.side_1 + self.side_2 + self.side_3
#
#     def get_area(self):
#         p = self.get_perimeter() / 2
#         return round(math.sqrt(p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3)), 2)
#
#     def draw(self):
#         # return ("*  " * self.width + "\n") * self.length
#         rows = []
#         for n in range(self.side_2):  # 6, n = 2
#             rows.append(" " * n + "*" * (self.side_1 - 2 * n))  # ['***********', ' *********', '  *******']
#         rows.reverse()
#         # return "\n".join(reversed(rows))
#         return "\n".join(rows)
#
#     def info(self):
#         print(f"=== Треугольник ===\nСторона 1: {self.side_1}\nСторона 2: {self.side_2}\nСторона 3: {self.side_3}"
#               f"\nЦвет: {self.color}\nПлощадь: {self.get_area()}\nПериметр: {self.get_perimeter()}\n{self.draw()}\n")
#
#
# # sq = Square(3, "red")
# # sq.info()
# # rect = Rectangle(3, 7, "green")
# # rect.info()
# # tr = Triangle(11, 6, 6, "yellow")
# # tr.info()
#
# fig = [Square(3, "red"), Rectangle(3, 7, "green"), Triangle(11, 6, 6, "yellow")]
#
# for g in fig:
#     g.info()


# дз 31
# from car.electrocar import ElectroCar
#
#
# e_car = ElectroCar("Tesla","T",2018,9000,100)
# e_car.show_car()
# e_car.descript_battery()

#dz 32

import json
from random import choice


def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)
    # print(name)

    while len(tel) != 10:
        tel += choice(nums)
    # print(tel)

    person = {
        'name': name,
        'tel': tel
    }

    return person, tel


def write_json(person_dict,num):  # {'name': ..., 'tel': ...}
    try:
        data = json.load(open("persons.json"))
    except FileNotFoundError:
        data = {}

    data[num] = person_dict

    with open("persons.json", "w") as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person()[0], gen_person()[1])
