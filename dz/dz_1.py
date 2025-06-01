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
from math import sqrt


class Area:
    __count = 0

    @staticmethod
    def triangle_area(a, b, c):
        p = (a + b + c) / 2
        Area.__count += 1
        return sqrt(p * (p - a) * (p - b) * (p - c))

    @staticmethod
    def triangle_area_2(a, h):
        Area.__count += 1
        return 0.5 * a * h

    @staticmethod
    def square_area(a):
        Area.__count += 1
        return a ** 2

    @staticmethod
    def rectangle_area(a, b):
        Area.__count += 1
        return a * b

    @staticmethod
    def get_count():
        return Area.__count


print("Площадь треугольника по формуле Герона (3,4,5):", Area.triangle_area(3, 4, 5))
print("Площадь треугольника по формуле Герона(13,14,15:", Area.triangle_area(13, 14, 15))
print("Площадь треугольника через основание и высоту(6,7:", Area.triangle_area_2(6, 7))
print("Площадь квадрата:", Area.square_area(7))
print("Площадь квадрата:", Area.square_area(8))
print("Площадь квадрата:", Area.square_area(9))
print("Площадь прямоугольника:", Area.rectangle_area(2, 6))
print("Количество подсчетов площади:", Area.get_count())


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
