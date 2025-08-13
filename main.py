# name = "admin"  # переменная
# # print("Hello, " + name + "!")
# age = 20
# # print(name + str(age))
# print(age)
# age = 15.5
# print(age)
# print(type(name))
# print(type(age))
import math

# a = 4
# b = 5
# print(id(a))
# print(id(b))
# a = b  # 5
# print(a)
# print(b)
# print(id(a))
# print(id(b))

# a = b = c = 1
# print(a)
# print(b)
# print(c)

# a, b, c = 5, "Hello", 9.2
#
# print(a)
# print(b)
# print(c)

# _first_name = "admin"
# print(_first_name)

# PI = 3.14
# print(PI)

# name = "Никита"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.")


# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# # первый способ
# # c = a  # 1
# # a = b  # 2
# # b = c  # 1
# # второй способ
# # a, b = b, a
# # третий способ
# a = a + b  # 1 + 2 = 3
# b = a - b  # 3 - 2 = 1
# a = a - b  # 3 - 1 = 2
# print("a:", a)
# print("b:", b)

# print("строка \
# символов")
# print('строка \nсимволов')
# print("\tДокумент \"file.txt\"      находится     по пути: \rD\\folder\\file.txt")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + "___"
# print(s3 * 3)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(7 / 2)
# print(7 // 2)
# print(7 ** 2)
# print(7 % 2)

# a = 5
# b = 7
# c = 3
# res = a + b + c
# print("Сумма:", res)
# print("Произведение:", a * b * c)
# print("Среднее арифметическое:", res / 3)

# print(6 / 4 * 5 ** 2 + 7)  # 113
# print((6 + 4) * (5 ** 2 + 7))  # 320

# num = 10
# num += 5  # num = num + 5 = 15
# print(num)
#
# num -= 3  #  num = num - 3 = 12
# print(num)
#
# num **= 2  # num = num ** 2  144
# print(num)

# num = 4321
# print("Исходное число:", num)
# a = num % 10
# print("a:", a)
# num = num // 10
# # print(num)
# b = num % 10
# print("b:", b)
# num = num // 10
# # print(num)
# c = num % 10
# print("c:", c)
# num = num // 10
# # print(num)
# d = num % 10
# print("d:", d)
# print("Обратное число:", a * 1000 + b * 100 + c * 10 + d)


# num = 9753
# print("Исходное число:", num)
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print("Обратное число:", res)

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# # res = num1 + str(num2)
# print(res)

# print(int(3.8))
# print(round(3.8))
# print(type(round(3.8)))
# print(round(3.895, 2))
# print(type(round(3.899, 2)))

# a = '5.2'
# b = 10
# c = float(a) + b
# print(c)

# name = "Виктор"
# age = 28
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="", end=" ")
# print("Новая строка")

# name = input("Введите имя: ")
# print("Ваше имя:", name)

# num = input("Введите число: ")
# power = input("Введите степень: ")
# num = int(num)
# power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# num1 = int(input("Введите число 1: "))
# num2 = int(input("Введите число 2: "))
# num3 = int(input("Введите число 3: "))
# num4 = int(input("Введите число 4: "))
# sum1 = num1 + num2
# sum2 = num3 + num4
# res = sum1 / sum2
# print(round(res, 2))

# b1 = True
# b2 = False
# print(type(b1))
# print(b1 + 5)
# print(b2 + 5)

# print(bool("python"))
# print(bool(""))
# print(bool(" "))
# print(bool(5))
# print(bool(0))
# print(bool(0.1))
# print(bool(0.0))
# print(bool(False))
# print(bool(None))
#
# a = None
# print(a)
# print(type(a))

# print(7 == 7)
# print(2 + 5 == 7 / 3)
# print(2 + 5 != 7 / 3)
# print(8 > 5)
# print(8 > 8)
# print(8 >= 8)
# print(9 > 9)
# print(9 >= 9)
# print("python" > "Python")  # 112 > 80

# print(2 < 4 < 9)  # True && True => True
# print(2 * 5 > 7 >= 4 + 3)  # 10 > 7 >= 7  True && True => True
# print(3 * 3 <= 7 >= 2)  # 9 <= 7 >= 2  False && True =>
#
# a = "10"
# b = 10
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)  # True and True => True
# print(5 - 3 == 2 and 1 + 3 < 4)  # True and False => False
#
# print(5 - 3 == 2 or 1 + 3 == 4)  # True or True => True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True or False => True
#
# print(not 9 - 5)
# print(not 7 - 7)
#
# adfsdf = 5
# print("a:", adfsdf)

# print("строка текста строка текста строка текста строка текста строка текста строка текста строка текста строка
# текста "
#       "строка текста строка текста строка текста строка текста строка текста ")

# cnt = 5
# if cnt < 10:
#     # cnt = cnt + 1
#     cnt += 1
#     print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 15
# b = 25
# if a > b:
#     print("a > b")
# elif a == b:
#     print("a == b")
# else:
#     print("b > a")

# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
# c = input("Введите третью строку: ")
#
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or b == c or a == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")


# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")


# a = int(input("Введите номер месяца:"))
# if a == 12 or a == 1 or a == 2:
#     print("Зима")
# elif a == 3 or a == 4 or a == 5:
#     print("Весна")
# elif a == 6 or a == 7 or a == 8:
#     print("Лето")
# elif a == 9 or a == 10 or a == 11:
#     print("Ocень")
# else:
#     print("Нету таких месяцев")

# month = int(input("Введите номер месяца цифрой: "))
# if 1 <= month <= 2 or month == 12:
#     print("Время года - Зима")
# elif 3 <= month <= 5:
#     print("Время года - Весна")
# elif 6 <= month <= 8:
#     print("Время года - Лето")
# elif 9 <= month <= 11:
#     print("Время года - Осень")
# else:
#     print("Некорректное значение")

# season = int(input("Введите номер месяца: "))
# if 1 <= season <= 12:
#     print("Время года: ", end="")
#     if 1 <= season <= 2 or season == 12:
#         print("Зима")
#     if 3 <= season <= 5:
#         print("Весна")
#     if 6 <= season <= 8:
#         print("Лето")
#     if 9 <= season <= 11:
#         print("Осень")
# else:
#     print("Такого месяца нет")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ", end="")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if 5 <= n <= 9 or n == 0:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ворон", end="")
#     if n == 1:
#         print("а", n)
#     elif 2 <= n <= 4:
#         print("ы", n)
#     else:
#         print("", n)
# else:
#     print("Ошибка ввода")


# match выражение:
#     case шаблон_1:
#         действие_1
#     case шаблон_2:
#         действие_2
#     case _:
#         значение_по_умолчанию

# password = "user"
#
# match password:
#     case "admin":
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#     case _:
#         print("Пароль неверен")

# day = 'понедельник'
# time = 15
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 12 or 14 <= time <= 17:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")

# Тернарное выражение

# a, b = 30, 20
# print(a if a < b else b)

# a, b = 30, 20
# print("На 0 делить нельзя" if b == 0 else a / b)


# a = int(input("Введите число от 1 до 99: "))
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

# a = int(input("Введите число от 1 до 99: "))  # 53
# kop = a
# if 11 <= kop <= 14:
#     print(a, "копеек")
# elif 1 <= a <= 99:
#     kop = kop % 10
#     if kop == 1:
#         print(a, "копейка")
#     elif 2 <= kop <= 4:
#         print(a, "копейки")
#     else:
#         print(a, "копеек")
# else:
#     print("Значения должны быть от 1 по 99")

# Исключения

# a = 5
# b = 0
# print(a / b)

# try:  # попытаться
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")
#
# print("Код далее")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на 0")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или нельзя делить на 0")
# else:  # когда в блоку try не возникло исключение
#     print("Все нормально. Вы ввели", n, "и", m)
# finally:  # выполнится в любом случае
#     print("Конец программы")

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(str(n) + " " + str(m))

# Циклы

# while уловие:
#     блок_кода

# итерация - один шаг цикла

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1
#
# print()
#
# j = 2
# while j <= 20:
#     print(j, end=" ")
#     j += 2

# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Укажите количество символов: "))
# # print("*" * n)
# while n > 0:
#     print("*", end="")
#     n -= 1

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     if a % 2:  # 1 3 5
#         print(a)
#         res += a
#     a += 1
# print("Сумма нечетных чисел:", res)

# n = input("Введите целое число: ")
#
# while type(n) is not int: # is not не равно \ не является
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# res = 1
# while True:
#     n = int(input("введите  число: "))
#     if n == 0:
#         break
#     res *= n
# print(res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# print("Цикл окончен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# n = int(input("Количество символов: "))
# symbol = input("Тип символа: ")
# orient = int(input("0 - горизонтальная\n1 - вертикальная\nориентация линии: "))
#
# # while orient != "0" and orient != "1":
# #     orient = input("Укажите Ваш выбор числом 0 или 1: ")
# i = 0
# while i < n:
#     if orient == 1:
#         print(symbol)
#     else:
#         print(symbol, end=" ")
#     i += 1


# for element in collection:
#     print(element)

# for i in "Hello":
#     print(i)
#
# for i in "Hello", "World":
#     print(i)

# range(start=0, stop, step=1)

# for i in range(10):  # i = 0, i < 10; i += 1
#     print(i, end=" ")
#
# print()
# j = 10
# while j > 0:
#     print(j, end=" ")
#     j -= 2


# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(11, 100, 11):
#     print(i, end=" ")
#
# print()
#
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     # if i == 1:
#     #     break
# else:
#     print("Конец цикла")


# for i in range(3):  # for(let i = 0; i < 3; i++)  # i = 3
#     print("+++")
#     for j in range(2):  # for(let j = 0; j < 2; j++) # j = 2
#         print("-----")


# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):  # 3
#     for j in range(w):  # 1
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

# string = [letter * 2 for letter in "Python"]
# print(string)
#
# for letter in "Python":
#     print(letter * 2, end="\t")

# num = [i for i in range(30) if i % 2 == 0]
# print(num)
#
# for i in range(30):
#     if i % 2 == 0:
#         print(i, end="\t")


# Список (list)
# nums = [8, 3, 9, 4, 1]
# print(nums)
# print(type(nums))
#
# num1 = list()
# print(num1)
# print(type(num1))

# nums = [8, 3, 9, 4, 1, "one", True]
# print(nums)
# print(nums[0])
# print(nums[-5])
# print(nums[4])
# print(nums[-1])
# print(nums[-2])

# nums = [8, 3, 9, 4, 1]
# print(nums)
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)

# nums = [8, 3, 9, 4, 1]
# print(nums, id(nums))
# print(nums[0], id(nums[0]))
# print(nums[1], id(nums[1]))
# nums[1] = 256
# print(nums[1], id(nums[1]))
# print(nums, id(nums))
# print("Длина списка:", len(nums))

# nums = [8, 3, 9, 4, 1]
# nums2 = [11, 12, 13]
# n = nums + nums2
# print(n)
# print(n * 3)

# print(list("Hello"))
#
# print(range(10))
# print(list(range(10)))
# print(list(range(2, 10)))
# print(list(range(10, 2, -2)))

# [выражение for переменная in последовательность]

# a = [0 for i in range(1, 5)]  # 0 1 2
# print(a)  # [0, 0, 0, 0, 0]

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)  # [1, 4, 9, 16]


# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]  # range(0, -1)
# print(a)

# a = list(range(10, 100, 10))
# print(a)
#
# for i in range(len(a)):  # 0 1 2 3 4 5 6 7 8
#     print(a[i] + 2, end=" ")
# print()
#
# for i in a:
#     print(i + 2, end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print("Сумма отрицательных элементов:", s)

# for i in a:
#     if i < 0:
#         s += i
# print("Сумма отрицательных элементов:", s)


# i = 0
# while i < len(a):
#     if a[i] < 0:
#         s += a[i]
#     i += 1
# print("Сумма отрицательных элементов:", s)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
#
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")
# print()
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# n = list(range(21, 26))
# print(n)
# k = s = 0
# # for i in range(len(n)):
# # if n[i] % 2 == 0:
# #     k += 1
# # else:
# #     s += n[i]
#
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
#
# print("Количество четных элементов:", k)
# print("Сумма нечетных элементов:", s)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# sum1 = kol = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         kol += 1
#         sum1 += a[i]
# print("среднее арифметическое", sum1 / kol)

# lst = [7, 9, 2, 1, 17]
# print(lst)
# lst[0], lst[1] = lst[1], lst[0]
# print(lst)

# Срез
# список[start:stop:step]

# s = [9, 7, 2, 1, 17, 8]
# print(s)
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[::2])
# print(s[:])
# print(s[0:-1])
# print(s[-1:0:-1])
# print(s[10:20])

# lst = list(range(1, 8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[::-7])
# print(lst[-1:])
# print(lst[3:4])
# print(lst[4:7])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])

# st = "123456"
# print(st[1:3])
# num = st[::-1]
# print(num)
# print(type(num))
# num = int(num)
# print(num)
# print(type(num))

# lst = list(range(1, 8))
# print(lst)
# lst[1:3] = [0, 0, 0, 0]
# print(lst)
# lst[1:2] = [20]
# lst[3] = [40, 50]
# print(lst)
# lst[15:16] = [100]
# print(lst)

# print(len(lst))

# Методы списков

# lst = list(range(1, 8))
# print(lst)
# lst.append(99)  # добавляет один элемент в конец списка
# print(lst)
# lst.extend([1, 2, 3])   # добавляет список элемент в конец списка
# print(lst)
# lst.insert(1, 100)  # добавляет элемент (второй параметр) по заданному индексу (первый параметр)
# print(lst)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)  # [5,6,7,8,9]
# print(s)

# a = [5, 9, 2, 1, 4, 3, 4, 2]
# b = [4, 2, 1, 3, 7, 2]
# c = []  # [2]
# # 1 вариант
# # for i in a:
# #     for j in b:
# #         if i in c:
# #             continue
# #         if i == j:  # 1 == 1
# #             c.append(i)
# #             break
#
# for element in a:
#     if element in b and element not in c:  # [2, 1, 4, 3, 4, 2]
#         c.append(element)
#
# print(c)
#

# 04.02.2025

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# b = []
#
# for i in range(len(a)):
#     if a[i] not in b:
#         b.append(a[i])
# print(b)


# lst = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# new_lst = []
# i= 0
# for element in lst:
#     k = element
#     for element in lst:
#         if k == element:
#             i += 1
#         if i == 1:
#             print(k, end=" ")
#         new_lst.append(k)
#         i = 0


# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# b = []
#
# for i in range(len(a)):
#     if a[i] not in b:
#         b.append(a[i])
# print(b)


# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# num = a.count(6) # показывает количество одинаковых чисел в списке
# print(num)


# # второй вариант решения дз
# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# b = []
# for i in range(len(a)):
#     if a.count(a[i]) == 1:
#         b.append(a[i])
# print(b)
#


# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(a)
# for i in a:  # 3
#     if a.count(i) == 1:  # 1 == 1
#         print(i, end=" ")  # 3 5


# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(a)
# for i in a:  # 1, 3, 5, 6, 2, 4, 6, 1, 2, 7
#     print(i, end=" ")
#     # if a.count(i) == 1:
#     #     print(i, end=" ")
#
#
# print()
# for i in range(len(a)): # 0,1,2,3,4,5,6,7,8,9
#     print(a[i], end=" ") # без индекса перечисление списка от 0 до конца длины
# #     if a.count(a[i]) == 1:
# #         b.append(a[i])
#


# a = [1, 2, 3]
# b = [11, 22, 33, 4, 2]
# c = []
# вариант когда длина второго  списка длиннее
# for i in range(len(a)):  # 0 1 2
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
#
# print(c)

# вариант когда 1 список больше
# a = [1, 2, 3, 5, 6]
# b = [11, 22, 33, ]
# c = []
# for i in range(len(b)):  # 0 1 2
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(b), len(a)):
#     c.append(a[i])
#
# print(c)

# 3 вариант универсальный вариант
# a = [1, 2, 3, 4, 2]
# b = [11, 22, 33, 55, 66]
# c = []
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
#
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
#
# print(c)


# a = [1, 2, 3, 4, 2]
# b = [11, 22, 33, 55, 66]
# c = []
# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
# for i in range(len(a), len(b)):
#         c.append(b[i])
# print(c)

# запомнить методы
# lst = [11, 1, 22, 3, 33, 3, 55, 66]
#
# lst[5:] = []
# print(lst)
# # 2
# lst = [11, 1, 22, 3, 33, 3, 55, 66]
#
# lst[3:5] = []
# print(lst)
# # 3
# lst = [11, 1, 22, 3, 33, 3, 55, 66]
#
# del lst[2]
# print(lst)
#
# # 4
# lst = [11, 1, 22, 3, 33, 3, 55, 66]
#
# del lst[:]
# print(lst)
#
# # 5
# lst = [11, 1, 22, 3, 33, 3, 55, 66]
#
# lst.remove(22)  # удаляет элемент из списка по значению(первое вхождение)
# print(lst)


# 6
# lst = [11, 1, 22, 3, 33, 3, 55, 66]
# last = lst.pop() # удаляет последний элемент из списка и возвращает его
# print(last)
# print(lst)
#
#
# lst = [11, 1, 22, 3, 33, 3, 55, 66]
# second = lst.pop(5) # удаляет элемент из списка и возвращает его
# print(second)
# print(lst)
#
# lst.clear() # удалил все значения из списка
# print(lst)


# задача
# print("Введите элементы списка")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print("Введите индекс: ")
# k = int(input("k = "))
# a.pop(k)
# print(a)
#


# lst = [11, 1, 22, 3, 33, 3, 55, 66]
# value = 100
# if value in lst:
#     ind = lst.index(value, ) #start stop  # возвращает индекс первого вхождения искомого элемента, можно указать
#    диапозон от какого до какого индекса м производим поиск, может выбрасывать  исключение ValueError - если элемент не найден
#     print(ind)
# print(lst)


# lst = [11, 1, 22, 3, 33, 3, 55, 66]
# a = lst.copy() # создает копию списка по другому адресу
# print(lst, id(lst))
# print(a,id(a))
#
# a.append(100)
# print(lst)
# print(a)
#
# lst[0] = 256
# print(lst)
# print(a)


# print(dir(list)) # важко!!!

# lst = [11, 1, 22, 3, 33, 3, 55, 66]
# lst.reverse()  # развернул элементы в противоложную сторону
# print(lst)


# lst = [11, 1, 22, 3, 33, 3, 55, 66]
# lst.sort()  # расставил по возрастанию цифры
# print(lst)
#
# lst = [11, 1, 22, 3, 33, 3, 55, 66]
# lst.sort(reverse=True)  # расставил по убыванию цифры
# print(lst)

# st = "Hello"
# new_lst = sorted(st, reverse=True)
# print(new_lst)
# print(st)

# # s = ['Виталий', 'Сергей', 'Александр', 'Анна']
# # s.sort(key=len)  # от меньшего к большому по буквам имена расставляет
# # print(s)


# Генерация случайных данных

# import random

# print(random.random())
# print(random.randint(5,10))
# print(random.randrange(5,10))
#
#
# print(random.uniform(5.5,10.3))

# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# s = [55, 66, 77, 88, 99, 5, 7, 9, 1, 2, 4, 3, 8]
# print(random.choice(city_list))
# print(random.choice(s))
# print(random.choices(city_list, k=3)) #k= добавляет количество элементов
# print(random.choices(s, k=3))


# random.shuffle(city_list) # может перемешать элементы  в списке
# random.shuffle(s)
# print(city_list)
# print(s)


# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)

# 06.02.2025


# import random
#
# mas1 = [random.randint(0, 100) for i in range(10)]
# print(mas1)
# mas = mas1.copy()
# mas.sort()
# print(mas)
# min_ = mas[0]
# print("Min =", min_)
# ind = mas1.index(min_)
# print(ind)
# del mas1[:ind]
# print(mas1)
#
#

# import random

# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# print(len(mas))  # длина списка
# print(min(mas))  # минимальный элемент из списка
# print(max(mas))  # максимальный элемент из списка
# print(sum(mas))  # сумма элементов списка

# заполнить массив из 10 элеиментов случайными числами.
# Найти максимальный элемент массива и переместить его вначала массива

# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# maximum = max(mas)
# print("Max =", maximum)
# mas.remove(maximum)  # удаляет элемент с максимального значения
# mas.insert(0, maximum)
# print(mas)


# mas = [random.randint(0, 10) for i in range(10)]
# print(mas)
# print(2 not in mas)


# lst = [4,2]
# if len(lst) == 0:
#     print("Список пустой")
#
# print(bool(lst))
#
# if not lst:
#     print("Список пустой")
# else:
#     print("В списке есть элементы")

# print(len(m))
# print(m[1][2])  # получили 1 индекс / второе индекс вложенного индекса

# m = [
#     [1, 2, 5, 7],  # 0
#     [4, 6, 7, 8],  # 1
#     [5, 5, 6, 7, ]  # 2
# ]
# print(m)
# print("Вариант 1")
# for row in range(len(m)):  # row = 0 # 0 1 2
#     # print(m[row])
#     for col in range(len(m[row])):  # col = 0 # 0 1 2 3
#         print(m[row][col], end="\t")
#     print()
#
# print("Вариант 2")
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()


# Модули

# import math

# print(math.sqrt(4))  # корень
# print(math.ceil(4.2))  # округление в верхнюю сторону
# print(math.floor(4.2))  # округление в нижнюю сторону

# import math as m # даеот любое название модулю
# print(m.sqrt(4))
# print(m.ceil(4.2))
# print(m.floor(4.2))

# from math import *
#
# print(sqrt(4))
# print(ceil(4.2)) # округление верх
# print(floor(4.2)) #округление вниз


# from math import sqrt, ceil, floor  # самый производительный метод
#
# print(sqrt(4))
# print(ceil(4.2))
# print(floor(4.2))


# import math
# print(dir(math))

# from math import pi
# # print(pi)
#
# radius = int(input("Введите радиус окружности "))
# print("Длина окружности", round(2 * pi * radius,2))


# import time
# import locale

# print(time.time())
# print(time.ctime())
# print(time.localtime())
# res = time.localtime()
# # print(res.tm_year, "-", res.tm_mom, "-0", res.tm_mday, sep="")
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))
#
# locale.setlocale(locale.LC_ALL, "ru")
# print(time.strftime("Сегодня: %B/%d/%Y,%A"))


# start = time.monotonic()
# # start = time.time()
# pause = 5
# print("Программа запущена")
# time.sleep(pause)
# result = time.monotonic() - start
# print("Программа выполнена за", result, "секунд")

# обратный таймер
# a = 500
# for i in range(a, -1, -1):
#     time.sleep(1)
#     print(i)


# 11.02.2025

# import math
#
# shape = int(input("Выбор фигуры:\n1-треугольник\n2-пряумогольник\n3-круг\n: "))
# s = None
# if shape == 1:
#     a = int(input("Введите сторону a = "))
#     b = int(input("Введите сторону b = "))
#     c = int(input("Введите сторону c = "))
#     p = (a + b + c) / 2
#     s = math.sqrt(p * (p - a) * (p - b) * (p - c))
#
# elif shape == 2:
#     a = int(input("Введите сторону a = "))
#     b = int(input("Введите сторону b = "))
#     s = a * b
# elif shape == 3:
#     radius = int(input("Введите радиус = "))
#     s = math.pi * radius ** 2
# else:
#     print("Такой фигуры не существует")
#
# print(round(s, 2))


# ФУНКЦИИ


# def hello(name, age):
#     print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
#
#
# hello("Irina", 28)
# hello("Ivan", 15)


# def get_sum(a, b):
#     print(a + b)
#
#
# get_sum(2, 5)
# get_sum("abc", "dry")


# def print_line(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# print_line(9, "+", "-")
# print_line(7, "X", "0")


# def get_sum(a, b):
#     print("Hello")
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)


# def max_value(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(max_value(9, 6))
# print(max_value(9, 61))
#
#

# Написать функцию, нахождения разности,если a > b или сумму, если a < b
# a  и b - вводятся с клавиатуры


# def add(x, y):
#     if x > y:
#         return x - y
#     else:
#         return x + y
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# print(add(a, b))

# обменяли значения местами


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# 2 вариант

# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def is_first_big(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_first_big(10, 5))
# print(is_first_big(5, 10))
#
# a = int(input("Введите первое число "))
# b = int(input("Введите второе число "))
# if is_first_big(a,b):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше первого")


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5, 2, d=2))
# print(get_sum(1, 5, d=2))
#
#
# # 2 вариант как можно еще
# def get_sum(a, b=2, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(5))


# def display_info(name, age):
#     print("Name", name, "\nAge", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
#

# 13.02.2025

# def set_param(count=20, symbol="-"):
#     print(count * symbol)
#
#
# set_param(10,"+")
# set_param(5,"*")
# set_param(10,"#")
# set_param(7)
# set_param()


# def func(a, b):
#     return a + b
#
#
# print(func(2, 5))
# print(func(b=2, a=5))
# print(func(2))


# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)
# print(lst1 is lst2)
#
# a = "Hello"
# b = "Hello"
# print(a, id(a))
# print(b, id(b))
# print(a == b)
# print(a is b)


# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))
# lst1.pop(1)
# print(lst1, id(lst1))


# a = "Hello"
# print(a, id(a))
# a = a + "!"
# print(a, id(a))


# a = 5
# print(a, id(a))
# a = a + 3
# print(a, id(a))


# TUPLE - КОРТЕЖ ()

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
#
# print(lst[1])
# print(tpl[1])
# lst[1] = 50
# print(lst[1])
#
# tpl[1] = 50
# print(tpl[1])


# a = 1, 2, 3, 4, 5
# print(a, type(a))


# a = tuple("Hello")
# print(a, type(a))


# a = 1, 2, 3, 4, 5
# print(a[2])
# print(a[1:3])


# from random import randint
#
# print(tuple(i for i in range(10)))

# print(tuple(input("-> ") for i in range(5)))

# print(tuple(randint(50, 100) for i in range(10)))


# t1 = tuple("Hello")
# t2 = tuple("World")
# t3 = t1 + t2
# print(t3)
# # print(len(t3))  # считает длину списка
#
# print(t3.count('l')) # показывает количество таких букв в списке
#
# # print(t3.index('l',3))
#
# print(t3.count('a'))
# if 'a' in t3:
#     print(t3.index("a"))
# else:
#     print("Такого элемента нет")


# for i in t3:
#     print(i, end=" ")


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) == 1:
#             return tpl[tpl.index(el):]
#         else:
#             first = tpl.index(el)  # 1
#             second = tpl.index(el, first + 1)  # 4
#             print("first", first)
#             print("second", second)
#             return tpl[first:second]  # tpl[1:4+1]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# t = (True, 11, "Python", [4, 5, 6], ["Hello", "world"])
# print(t, id(t))
# t[4][0] = 'new'
# print(t, id(t))
# t[4].append("hi")
# print(t, id(t))


# РАСПАКОВКА КОРТЕЖА

# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# x, y, z = t  # x, z, y = 1, 2 , 3 аналог
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])
# first_name, year, married = user


# first_name, year, married = get_user()
# print(first_name)
# print(year)
# print(married)


# можно преобразовать список в кортеж и наоборот
# lst = [1, 2, 3, 4, 5]
# print(lst, type(lst))
# tpl = tuple(lst)
# print(tpl, type(tpl))
# lst2 = list(tpl)
# print(lst2, type(lst2))
# lst2.append(6)
# tpl2 = tuple(lst2)
# print(tpl2, type(tpl2))


# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
#
# # print(countries)
# for country in countries:
#     country_name, country_population,cities = country
#     print("\nСтрана ", country_name, " население = ", country_population,cities, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ",city_name," население = ",city_population, sep="" )


# tpl = tuple(input("Введите строку: "))
# print(tpl)
# lst = []
# for i in range(len(tpl)):
#     if tpl[i] not in lst:
#         lst.append(tpl[i])
#         print(lst)
#         for i in range(len(lst)):
#             print("Количество", lst[i], "=", tpl.count(lst[i]))


# 18.02.2025

# from random import randint
#
#
# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl1 = ran(0, 5)
# print(tpl1)
# tpl2 = ran(-5, 0)
# print(tpl2)
#
# tpl3 = tpl1 + tpl2
# print(tpl3)
#
# print("0 =", tpl3.count(0))


# Множество (set)
# к объекту set  нельзя обратиться по индексу

# s = {"red", "yellow", "green"}
# print(s)
# print(type(s))


# a = set("hello")
# print(a, type(a))

# a = set() # пустой сет можно создавать толлько так
# print(a, type(a))


# s = [i for i in range(10)]
# print(s)

# lst = [10, 2, 2, 2, 2, 3, 3, 8, 8, 9, 9, 10]
# # st = {i for i in lst if i % 2 == 0}
# st = set(lst)
# print(st)
# lst2 = list(st)
# print(lst2)

# t = {"red", "yellow", "green"}
# print("green" in t) # так можем проверить на наличие какие то элементы в множестве
# print("blue" in t)

# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# print([i for i in lst if "a" in i])
# print(tuple("A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst))
# print(["A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == "c"])
#
# lst2 = []
# for i in lst:
#     if i[0] == "c":
#         if i[0] == "a":
#             lst.append("A" + i[1:])
#         else:
#             lst2.append("B" + i[1:])
#
# print(lst2)


# print(dir(set))  # dir показывает набор функций

# a = {'red', 'yellow', 'green'}
# print(a)
# a.add('black')  # добавление элементов рандомно
# print(a)
#
# # a.remove('yellow') # удаляет элемент по значению
# # print(a)
# #
# # # a.remove('blue') #KeyError
# # # print(a)
# #
# # el = "blue"
# # if el in a:
# #     a.remove(el)
# #
# # print(a)
#
#
# a.discard("yellow")  # удаляет элемент по значению,но выбрасывает исключения если в списке нету
# print(a)
# a.pop()  # удаляет первый элемент из множества
# print(a)
#
# a.clear()  # очистили множество
# print(a)


# a = {0, 1, 2, 3}
# b = {4, 2, 3, 1}
# # c = a.union(b)  # {0, 1, 2, 3 , 4 }
# # c = a | b
# # print(c)
#
# # a |= b  # аналог += -= метод называется update
# # print(a)
# #
# # c = a & b
# # print(c)
#
# # a = {0, 1, 2, 3}
# # b = {4, 2, 3, 1}
# # c = a - c # оставляет только то, что есть в а но нету в b
#
# # a^= b аналог написания без вложения в переменную
# c = a ^ b  # оставляет уникальное из одного множества и с другого
# print(c)


# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1 | s2 | s3 | s4 | s5 | s6 | s7 # аналог
# s = s1.union(s2,s3,s4,s5,s6,s7)
# print(s)
# print("Кол-во уникальных элеменетов", len(s))
# print("min ", min(s))
# print("max ", max(s))


# s1 = "Hello"
# s2 = "How are you"
#
# # a = set(s1) & set(s2)
# # print(a)
#
# s1 = set(s1)
# print(s1)
# s2 = set(s2)
# print(s2)
# a = s1 & s2
#
# for i in a:
#     print(i, end=" ")

# a не является подножеством b потому что a больше
# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# c = a <= b
# print(c)


# frozenset (замороженное множество)

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
#
# a = frozenset({"hello", "world"})
# print(a)


# Словарь (dict) {}

# lst = ["one", "two"]
# d = {"furst": "one", "second": "two"}
#
# print(lst[1])
# lst[1] = "ten"
# print(lst)
#
#
# d["second"] = "ten"
# print(d)


# d = {}
# print(d)
# print(type(d))


# d = dict(a="Hello", b="World")
# print(d)
# print(type(d))
#
# d1 = {"a": "Hello", "b": "World"}
# print(d1)
#

# d = {0: "text", "one": 45, (1, 2):"Кортеж", 42: [9, 8], True: 1, False: 0, "a": "Кортеж"}
# print(d)
#

# user = [
#     ["a", 1],
#     ["b", 2],
#     ["c", 3],
# ]
# print(user)
# new_dict = dict(user)
# print(new_dict)


# 20.02.2025

# d = {i: i ** 2 for i in range(1,8)}
# print(d)
#
# # print(3 in d)  # проверяет наличие ключа в словаре
# # print(25 in d)
#
# # del d[3]
# # print(d)
#
# # key = 4
# # if key in d: # проверяет на наличие ключа в словаре, чтобы удалить после
# #     del d[key]
# #     print(d)
#
# key = 9
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключем", key, "нет в словаре")
#
# print(d)

# Дан словарь с числовыми значениями необходимо их все перемоножить и вывести на экран

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
#
# res = 1
# for key in d:
#     print(key, ":", d[key])
#     res *= d[key]
#
# print(res)


# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# print(d)

# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить "))
# del d[dislike]
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n == "0":  # '0' == 0
#         break
#     else:
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n][1] += count
#                 except ValueError:
#                     print("Значение некорректно. Введите число")
#         else:
#             print("Такого ключа не существует")
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")


# Методы словарей

# d = {"A": 1, "B": 2, "C": 3}
# print(d)
#
# print(d.keys())  # список ключей
# print(d.values())  # список значений
# print(d.items())  # список ключей и значений в виде кортежей
#
# for i, j in d.items():
#     print(i, ":", j)
#


# d = {"A": 1, "B": 2, "C": 3}
# d2 = d.copy() # возвращается копия словаря
# print("D =", d)
# print("D2 =", d2)
# d2["B"] = 5
# print("D =", d)
# print("D2 =", d2)

# d = {"A": 1, "B": 2, "C": 3}
# print(d)
# d.clear() # удалили все элементы из словаря
# item = d.pop("M", "Такого ключа не существует в словаре") # удалили элемент по ключу, вернули значение
# item = d.popitem() # удаляется последний элемент и возвращается кортеж из ключа и значенния
# print(d)
# print(item)

# d = {"A": 1, "B": 2, "C": 3}
# print(d)
# # print(d["W"])
# value = d.get("B", "Такого ключа не сущесвует в словаре") # получает значение по заданному ключу
# print(value)

# d = {"A": 1, "B": 2, "C": 3}
# print(d)
# item = d.setdefault("W", 5)  # по заданному ключу добавляет новый ключ и значение если ключа не существовало
# print(d)
# print(item)

# d = {"A": 1, "B": 2, "C": 3}
# d2 = {"R": 7, "Q": 9}
# print(d)
# print(d2)
# d3 = d | d2 # если 2 одинаковых значения то перезапишет  то что справа
# print(d3)

# 2 вариант

# d = {"A": 1, "B": 2, "C": 3}
# d2 = {"R": 7, "Q": 9, "B": 5}
# d3 = [("T", 7), ("P", 5)]
# print(d)
# print(d2)
# # d3 = d | d2
# d.update(d2)  № объеденяет два словаря в один, если есть одниковые значения,то переписывает то что справа
# d.update(d3)
# print(d)


# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# new_d = dict()
# new_d["name"] = d.pop("name") #d.pop удаляет и возращает в new_d
# new_d["salary"] = d.pop("salary")
# print(d)
# print(new_d)


# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
#
# d['location'] = d.pop("city") # удаляет ключ и перезаписывает
#
# print(d)

# d = {
#     "first": {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "second": {
#         4: "four",
#         5: "five"
#     }
# }
# print(d)
#
# for x in d:
#     print(x)
#     for y in d[x]:
#         print("\t", y, ": ", d[x][y], sep="")


# 2 вариант
# for x, y in d.items():
#     print(x)
#     for i, j in y.items():
#         print("\t", i, ": ", j, sep="")


# 25.02.2025


# dict_sales = {'John': {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#               'Tom': {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#               'Anne': {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#               'Fionna': {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
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
# print(dict_sales[person][region])

# # меняет местами цифру с текстом
# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# print({v: k for k, v in d.items()})


# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# # print({k: v for k, v in d.items()})
# print({k: v for k, v in d.items() if v <= 2})
#

# d = {i: i * 5 for i in [10, 20, 30, 40, 50]}
# print(d)
#
# s = "Hello"
# d1 = {i: i * 3 for i in s}
# print(d1)


# lst = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict() # {"one": []}
# s = None
#
# for i in lst:  # приходит 1,2,3
#     if type(i) is str:  # type(i) == str
#         d[i] = []
#         s = i # s = "one"
#     else:
#         d[s].append(i)
#
# print(d)


# ZIP([], [])

# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
#
# d1 = list(
#     zip([1, 2, 3], ['one', 'two', 'three'], [True, False, True]))  # объеденяет несколько последовательностей в один
# print(d1)

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# d = {k: v for k, v in zip(b, a)}
# print(d)


# a = [1, 2, 3]
# c = list(zip(a))
# print(c)

# one = {"name": "Igor", "surname": "Pavlov", "job": "Consultant"}
# two = {"name": "Irina", "surname": "Vetrova", "job": "Manager"}
#
# for (k1, k2), (v1, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)


# lst = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*lst)
# print(a)
# print(b)

# letter = ['b', 'a', 'd', 'c']
# number = [3, 4, 1, 2]
# d = dict(zip(letter, number))
# print(d)
#
# data = sorted(zip(letter, number))
# print(data)

# data1 = list(zip(letter, number))
# print(data1)
# data1.sort()
# print(data1)
#
# d2 = dict(data1)
# print(d2)
#
# data2 = list(zip(number, letter))
# print(data2)
# data2.sort()
# print(data2)
# d3 = dict(data2)
# d3 = {v: k for k, v in data2}
# print(d3)


# # без звездочки список в списке, с ней распокавали в 1 список
# a = [1, 3, 3]
# b = [*a, 4, 5, 6]
# print(b)

# one = {"один": 1, "два": 2}
# two = {"три": 3, "четыре": 4}
# print({**one, **two})  # {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}

# colors = ["red", "yellow", "green"]
# i = 1
# for color in colors:
#     print(i, ") ", color, sep="")
#     i += 1
# print()
# for j, color in enumerate(colors, 1):
#     print(j, ") ", color, sep="")
#

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
#
# for i, (k, v) in enumerate(d.items()):
#     print(i, ") ", k, ": ", v, sep="")


# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5,2,3))


# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#         return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(7, 8, 9))
#
#


# def average(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#
#     res = []
#     for num in args:
#         if num < sr:
#             res.append(num)
#
#     return res
#
#
# print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(average(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(5))
# print(func(1, 2, 3, 4, 5))

# def scores(student, *score):
#     print("Student Name:", student)
#     for i in score:
#         print(i)
#
#
# scores("Игорь", 5, 5, 4, 3, 4, 5)
# scores("Иван", 5, 5, 4, 3, 4, 5)


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func(a=1, b=2, c=3))


# def info(**data):
#     for k, v in data.items():
#         print(k, ":", v)
#         print()
#
#
# info(name="Irina", surname="Vetrova", age=22)
# info(name="Igor", phone="4643543", age=22, email="igor@mail.ru")
#

# 27.02.2025

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


# def func1(*args):
#     print("args:",args)
#     print(args[0])
#
#
# def func2(**kwargs):
#     print("kwargs:", kwargs)
#     print(kwargs["one"])
#
#
# func1(1, 2, 3, 4, 5, 6)
# func2(one=123, two=456)


#   ОБЛАСТИ ВИДИМОСТИ (scope)


# name = "Tom"  # глобальная переменная
#
#
# def hi():
#     global name   # делает переменную внутри функции глоьальной
#     name = "Sam"
#     surname = "Jonson" # локальная переменная
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()


# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)

# print_ = 5
#
# lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(sum(lst))


# x = 4
#
#
# def func():
#     x = 2  # в функции локальной отдается приоритет
#     print(x + 3)
#
#
# func()


# x = 4
#
#
# def func():
#     x = 2
#
#     def inner():
#         print("x =", x)
#         print(x + 3)
#
#     inner()
#
#
# func()
#
#


# Вложенные функции

# def outer(who):
#     def inner():
#         print("Hello", who)
#
#     inner()
#
#
# outer("World")


# def fun1():
#     a = 6  # 2
#
#     def fun2(b):
#         a = 4 # 5
#         print("Сумма: ", a + b) # 6
#
#     print("a", a)  # 3
#     fun2(3) # 4
#
#
# fun1()  # 1


# x = 25
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a  # делает переменную не локальной, перезаписыввает что выше
#         a = 35
#         print("a", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)


# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#              nonlocal x
#              x = 55
#
#         fn3()
#         print("fn2.x =", x) # 33
#
#     fn2()
#     print("fn1.x =", x) # 25
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))


# dz

# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2,4,6))
# print(outer(5,8,2))
# print(outer(1,6,8))


# ЗАМЫКАНИЕ

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
# func1 = outer(5)
# print(func1(10))

# def func1():
#     a = 1
#     b = "Line"
#     c = [1, 2, 3]
#
#     def func2():
#         c.append(4)
#         a = 5
#         print(a)
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     n = 0
#
#     def inner():
#         nonlocal n
#         n += 1
#         print(city, n)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res1()
# res2 = func("Сочи")
# res2()
# res2()
# res2()


# 04.03.2025

# s = 0
#
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
# outer(2, 4, 6)
# print(s)
# outer(2, 4, 6)
# print(s)


# область видимости не локальной


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
# print(outer(2, 4, 6))
# print(outer(2, 4, 6))


# Анонимные функции ( Lambda - выражения)

# def func(x, y):
#     return x + y
#
#
# print(func(1,2))
#
# print((lambda x, y: x + y)(1,2))
#
# func = lambda x, y: x + y
#
# print(func(1,2))
#
#
# func = (lambda x, y: x + y)(1, 2)
#
# print(func)
#
#
# func = (lambda x, y: x + y)(1, 2)
# print(func)

# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=30: a + b + c)(10, 20))
# print((lambda a, b=20, c=30: a + b + c)(10))
# print((lambda a=10, b=20, c=30: a + b + c)())
#
# print((lambda *args: sum(args))(1, 2, 3, 5))


# tpl = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in tpl:
#     print(t("abc___"))

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = outer(42)
# print(f(3))
#
# # вариант с Lambda
# def outer(n):
#     return lambda x: n + x
#
#
# f = outer(42)
# print(f(3))
#
#
# # 3 вариант
# outer = lambda n: lambda x: n + x
# f = outer(42)
# print(f(3))
#
#
# print((lambda n: lambda x: n + x)(42)(3))
#

# # Задача
# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))


# d = {'b': 10, 'a': 15, 'c': 4}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# print(dict(lst))


# def func(i):
#     return i[1]
#
# d = {'b': 10, 'a': 15, 'c': 4}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=func)
# print(lst)
# print(dict(lst))


# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# res = sorted(players, reverse=True, key=lambda item: item['rating'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'])
# print(res)


# lst = [lambda x, y: x + y,lambda x, y: x - y,lambda x, y: x * y,lambda x, y: x / y,]
# print(lst[3](12,6))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье"),
# }
#
# d[2]()


# print((lambda a, b: a if a > b else b)(5, 3))
# print((lambda lst: [i * 2 for i in lst])([1, 2, 3, 4, 5, 6]))
#
#
# print([i * 2 for i in [1, 2, 3, 4, 5, 6]])


# from random import randint
#
# s = (lambda lst: [randint(10, 20) for i in range(10)])([])
# print(s)  # print([randint(10, 20) for i in range(10)])
# print([i * 2 for i in [1, 2, 3, 4, 5, 6]])


# map(function, iterables), filter(function, iterables)

# def mult(t):
#     return t * 2
#
# lst = [2, 8, 12, -5, -10]
# print(list(map(mult, lst)))
# print(tuple(map(mult, lst)))
#
#


# t = (2.88, -1.75, 100.55)
#
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))
# print(tuple(map(round, t)))


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# print(dict(map(lambda x, y: (x, y), st, num)))
# print(list(map(lambda x, y: (x, y), st, num)))


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# tpl = (True, False, True, False, True)
#
# print(dict(map(lambda x, y: (x, y), st, num)))
# print(list(map(lambda a, b, c: (a, b, c), st, num, tpl)))


# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda a, b: a + b, l1, l2)))

# lst = [input("-> ") for i in range(5)]
# print(lst)
# lst = list(map(int, lst))
# print(lst)


# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
#
# print(tuple(filter(lambda s: len(s) == 3, t)))


# lst = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
#
# lst1 = list(filter(lambda s: s > 75, lst))
# print(lst)
# print(lst1)


# from random import randint
#
# lst = [randint(1,40) for i in range(10)]
# print(lst)
#
# print(list(filter(lambda a: (a >= 10) and a <= 20, lst)))
# print(list(filter(lambda a: 10 <= a <= 20, lst)))


# nums = [45, 55, 60, 37, 100, 105, 220]
# print(list(filter(lambda s: s % 15 == 0, nums)))


# 06.03.2025
# from math import pi
# area = {
#     'Circle': lambda x: pi * x * x,
#     'Rectangle': lambda x, y: x * y,
#     'Trapezoid': lambda a, b, h: (a + b) * h / 2
#
# }
#
# print(area['Circle'](2))
# print(area['Rectangle'](10, 13))
# print(area['Trapezoid'](7, 5, 3))


# Декораторы

# def hello():
#     return "Hello, i im func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return "Hello, i im func 'hello'"
#
#
#
# test = hello
# print(test())


# def my_decorator(func):  # декорурирующая функция
#     def func_wrapper():
#         print("Код до функции")
#         func()
#         print("Код после функции")
#
#     return func_wrapper
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# # test = my_decorator(func_test)
# # test()
#
#
# func_test()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())


# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()


# def outer(fn):
#     def inner(args1, args2):
#         print("Данные:", args1, args2)
#         fn(args1, args2)
#
#     return inner
#
#
# @outer
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Ветрова")


# def outer(fn):
#     def inner(*args1, **kwargs):
#         print("args", args1)
#         print("kwargs", kwargs)
#         fn(*args1, **kwargs)
#
#     return inner
#
#
# @outer
# def print_data(a, b, c, study="python"):
#     print(a, b, c, "изучают", study, end="\n\n")
#
#
# print_data("Борис", "Владимир", "Елизавета", "JavaScript")
# print_data("Борис", "Владимир", "Елизавета")


# def args_dec(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @args_dec("Сумма", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @args_dec("Разность", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def multiply(arg):
#     def my_decorator(func):
#         def wrap(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#
#         return wrap
#     return my_decorator
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print("Результат", return_num(5))


# Строки

# print(bin(18))  # 0b10010 - двоичная система счисления
# print(oct(18))  # 0o22 - восьмипичная система счисления
# print(hex(18))  # 0x12 -шестнадцатеричная система счисления
#
# print(0b10010)
# print(0o22)
# print(0x12 + 0b10010 + 4)


# Unicode


# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
# print("y" in e)


# Задача

# def chang_char_to_str(s, old, new):
#     s2 = ""
#
#     i = 0
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython.Nython очень интересный язык программирования"
# str2 = chang_char_to_str(str1, "N", "P")
# print(str1)
# print(str2)


# Задача
# print(u"Привет")
# print("Привет")


# 11.03.2025

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


# вариант 2

# def avg(fn):
#     def wrap(*args):
#         st = ""
#         for i in args:
#             st += str(i) + ", "
#         print("Среднее арифметическое", st[:-2], "=", fn(*args) / len(args))
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


# print(b"a1b2c2")


# name = "Дмитрий"
# age = 25
# print("Меня зовут ", name, ". Мне", age, " лет.", sep="")
# print("Меня зовут ", name, ". Мне", str(age), " лет.", sep="")
# print(f"Меня зовут {name}. Мне {age} лет")  # обратить внимание


# x = 10
# y = 5
# print(f"{x = }, { y = }")
# # print(" x = ", x, " y = ", y, sep="")
#
# print(f"{x} x {y} / 5 = {round(x * y / 7,2)}")
# print(f"{x} x {y} / 5 = {x * y / 7:.3f}")  # аналог раунда по сокрещения остатка чисел


# num = 74
# print(f"{{num}}")


# dir_name = "folder"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)


# st = ("однострочный текст")
# print(st)
#
# s = """Многострочный
#  текст"""
# print(s)   # переносит на следующую строку
#
#


# def square(n):
#     """Принимает число n, возвращает квадрат числа N"""  # дает краткое описание функции
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)


# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r:положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))


# print(ord('a'))

# while True:
#     n = input("-> ")
#     if n != '-1':
#         print(ord(n))
#     else:
#         break

# Задача

# st = "Test string for me "
# arr = [ord(x) for x in st]
# print("ASCII коды", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое: ", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)


# print(chr(97))
# print(chr(35))
# print(chr(8364))

# a = 122
# b = 97
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
#     else:
#         for i in range(a, b + 1):
#             print(chr(i), end=" ")


# from random import randint
#
#
# SHORTEST = 6
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 123
#
#
# def random_password():
#     rand_len = randint(SHORTEST, LONGEST)
#     result = ""
#     for i in range( rand_len):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
#
# print("Случайный пароль", random_password())


# print(dir(str))

# s = "hello, WORLD! I am learning Python."
# # print(s.capitalize()) #Hello, world! i am learning python. как сделал
# # print(s.lower())  # hello, world! i am learning python.
# # print(s.upper()) # HELLO, WORLD! I AM LEARNING PYTHON.
#
#
# # print(s.count("h",1,-4))
# # print(s.lower().count("i"))
#
# print(s.find("Python"))
# print(s.find("h", 1, -4))
# print(s.find("h"))
# print(s.rfind("h"))
#
# print(s.index("h",1,-4))
# print(s.rindex("h"))

# st = "один два"
# st = input("-> ")
# one = st[:st.find(" ")]  # st[:4]
# two = st[st.find(" ")] # st[4:]
# res = one + " " + two
# print(res)

# st = "один два"
# print(st[st.find(" ") + 1:] + " " + st[:st.find(" ")])


# s = "hello, WORLD! I am learning Python."
# print(s.startswith("hello"))
# print(s.startswith("I am", 14))
# print(s.find("I am"))
#
#
# print(s.endswith("Python."))

# print("abc123".isalnum())  # состоит ли строка из букв и цифр
# print("abc!123".isalnum())
# print("abc".isalnum())
# print("123№".isalnum())

# print("ABCabc".isalpha())  # состоит ли строка из букв
# print("ABC%abc".isalpha())

# print("123".isdigit())  # состоит ли строка из цифр
# print("123".isdigit())

# print("aab".islower()) # находится ли в строке буквы в нижнем регистре,допускается наличие в других символов
# print("123aab!#".islower())
#
# print("ABC".isupper()) # находятся ли в строке буквы в нижнем регистре допускается наличие других символов
# print("123AbBC!!".isupper())
#
# print("py".center(10))
# print("py".center(10,"-"))
# print("py".center(1))

# print("    py".lstrip())
# print("py    ".rstrip())
# print("    py    ".strip())

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(str1.replace("Nython","Python",3)) # меняет слово старое на новое
#


# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))  # обьеденяет строку через заданный символ разделитель
#
# print("..".join(["1", "99"]))

# 13.03.2025

# s = "I am learning Python. hello, WORLD!"
# print(s.rfind('h') + 1)
# a = s[:s.find('h')] # s[:17]
# b = s[s.find('h'):s.rfind('h') + 1] # [17:23] # hon. h
# c = s[s.rfind("h") + 1:]  # s[23:]
# print(a + b[::-1] + c)


# print("Строка разделенная пробелами".split())
# print("www.python.org".split('.',1))


# s = input("Введите ФИО: ").split()
# print(s)
# print(f"{s[0]} {s[1][0]}. {s[2][0]}.")  # Никонов Валерий Анатольевич делает Никонов В А
#


# s = input("Введите числа через пробел: ").split()
# print(s)
# num = list(map(int, s))
# print(num)
# print(sum(num))


# Регулярные выражения

# import re

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта."
# # print(dir(re))
# reg = r"\."
# print(re.findall(reg, s))  # возвращает список совпадений с шаблоном
# print(re.search(reg, s))  # возвращает только первое совпадение с шаблоном
# # print(re.search(reg, s).span())  # от начала до конца
# # print(re.search(reg, s).start())  # начало
# # print(re.search(reg, s).end())  # конец
# # print(re.search(reg, s).group())  # слово
# print(re.split(reg, s))  # возвращает список который разбит по заданному шаблону
# print(re.sub(reg,"!", s)) # поиск и замена


# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта.6789.Hel_lo World"
# reg = r"[2025]"
# reg = r"[0-9]"
# reg = r"[0-9][0-9][0-9][0-9]"
# reg = r"[а-яА-Я]"
# reg = r"[А-яЁё.]"
# reg = r"[A-z]"
# reg = r"[A-Za-z]"
# reg = r"[^0-9]" # ищет все кроме цифр
# print(re.findall(reg, s))

# \ этот список экранирует


# Задача

# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg = "[0-9][0-9]:[0-5][0-9]"
# print(re.findall(reg, st))


# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта.6789.Hel_lo World"
# # reg = r"\d"  # [0-9]
# # reg = r"\D"  # [^0-9]
# # reg = r"\s"  # [ ]
# # reg = r"\S"  # [^ ]
# # reg = r"\w"  # [А-яА-Za-z0-9_]
# reg = r"\w+"  # [^А-яА-Za-z0-9_]
# print(re.findall(reg, s))
#

# Кол-во повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1 повторения


# d = "Цифры: 7, +17, -42, 0013, 0.3"
# reg = r"[+-]\d+"
# print(re.findall(reg, d))


# st = "05-03-1987 # Дата рождения"
#
# print("Дата рождения:", re.sub(r"\s#.+", "", st))
# print(re.sub("-",".", st))


# st = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# # reg = r"\w+\s*=\s*\w+\s*\w*\.?\w*\.?"
# # reg = r"\w+\s*=\s*\w+[\s*\w*\.?\w.]"
# reg = r"\w+\s*=[^;]+"
# print(re.findall(reg, st))
# print(re.split(r";\s", st))
#
# st = "12 сентября 2025 год 456 789456123"
# # reg = r"{2,4}"
# # reg = r"\d{2,4}"
# reg = r"\d{,4}"
# print(re.findall(reg, st))


# st = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, st))

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта.6789.Hel_lo World"
#

# # reg = r"^\w+\s\w+"
# reg = r"\w+\s\w+$"
# print(re.findall(reg, s))


# def validate_login(login):
#     return re.findall(r"^[a-zA-Z0-9_-]{3,16}$", login)
#
#
# print(validate_login("Python_master"))
# print(validate_login("pyt"))
#

# 18.03.2025
# import re


# print(re.findall(r"\w+","12 + й"))
# print(re.findall(r"\w+","12 + й", flags=re.ASCII))
#
# text = "hello world"
# print(re.findall(r"\w\+",text))
# print(re.findall(r"\w\+",text,re.DEBUG))


# text = "hello worLd"
# print(re.findall(r"L",text,re.IGNORECASE))

# text = """
# one
# two
# """
#
# # print(re.findall(r"one.\w+", text))
# # print(re.findall(r"one.\w+", text, re.DOTALL))
#
# print(re.findall(r"one$", text, re.MULTILINE))


# print(re.findall("""
# [a-z.-]+
# @
# [a-z.]+
# """, "test@mail.ru", re.VERBOSE))  # может разбить текст на шаблоны
#


# text = """Python,
# python,
# PYTHON
# """
#
# reg = "(?im)^python"
# print(re.findall(reg, text))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))

# s = "Петр, Ольга, и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий|Василий"
# print(re.findall(reg, s))


# s = "int = 4, float = 4.0f, double = 8.0"
# # reg = r"\w+\s*=\s*\d[\w.]*|float\s*=\s*\d[\w.]*"
# reg = r"(?:int|float)\s*=\s*\d[\w.]*"
# print(re.findall(reg, s))


# s = "Word2016, PS6, AI5"
# reg = r"([a-z])+(\d+)"  # (\d+) - скобки выводя цифры. ([a-z]) - текст . с двух сторон скобки выводит как ключи
# print(re.findall(reg, s, re.IGNORECASE))

# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))


# s = "58-01-2021"  # 01 - 31
# reg = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# print(re.findall(reg, s))
# # print(re.search(reg, s))


# s = "Word2016, PS6, AI5"
# reg = r"([a-z]+)(\d+)"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE).group())
# m = re.search(reg, s, re.IGNORECASE)
# print(m[1])
# print(m[2])
# print(m[0])

# s = "Самолет прилетает 10/23/2025. Будем рады вас видеть после 10/24/2025"
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "yandex.com and yandex.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))

# Рекурсия

# def elevator(n):  # 5
#     if n == 0:  # базовый случай
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)  # стек 5 4 3 2 1
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def sum_list(lst): # [1, 3, 5, 7, 9]
#     if len(lst) == 1:
#         print(lst, "=> lst [0]:", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst [0]:", lst[0])
#         return lst[0] + sum_list(lst[1:]) # 1 +
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25


# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(254,16))
#
#
# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
# print(names)
# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1], list)
# print(isinstance(names[1][1][0], list))
#


# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
#
#
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#
#     return count
#
#
# print(count_items(names))


# 20.03.2025
#
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


# print("Текст в локальном репозитории")


# 25.03.2025

# Файлы

# f = open("test.txt")
# print(*f)
# print(f)
# print(f.mode)
# print(f.name)
# print(f.encoding)
#
# f.close()
# print(f.closed)

# f = open("test.txt" , "r")
# print(f.read())
#
# f.close()


# 27.03.2025

# f = open("xyz.txt", "w")
# f.write("This is line1.\nThis is line2.\nThis is line2.\n")
# f.close()


# f = open("xyz.txt")
# # print(f.read())
#
# # print(f.readline())
# # print(f.readline(8))
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
#
# print(f.readline(15))
# f.close()

# f = open("xyz.txt")
# for line in f:
#     print(line)
# f.close()


# lines = ["This is line1.\n", "This is line1.\n", "This is line1.\n"]
#
#
# f = open("lines.txt", "w")
# f.writelines(lines)
# f.close()


# lines = [str(i) for i in range(10,1000,15)]
# print(lines)
#
# f = open("lines.txt", "w")
# for index in lines:
#     f.write(index + "\t")
# f.close()

# file = ("text2.txt")
#
#
# f = open(file, "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# f.close()
#
# f = open(file, "r")
# read_line = f.readlines()
# print(read_line)
# read_line[1] ="Hello world!\n"
# print(read_line)
# f.close()
#
# f = open(file, "r")
# f.writelines(read_line)
# f.close()


# f = open("test.txt", "r")
# print(f.read(3))
# print(f.tell()) # возвращает текущую позицию условного курсора в файле
# print(f.seek(1)) # перемещает условный курсоров в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()


# f = open("test2.txt", "w+")
# print(f.write("I am learning Python"))
# print(f.seek(0))
# print(f.write("--new string--"))
#
#
# f.close()

# with open("text.txt", "w") as f:
#     print(f.write("0123456789"))
# print(f.closed)

# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 5.04]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return " " .join(lt)
#
# # print(get_line(lst))
# with open("res.txt", "w") as f:
#     f.write(get_line(lst))
#
# print("Конец строки")


# with open("res.txt") as f:
#     nums = f.read()
#
# print(nums)
#
# print(sum(list(map(float, nums.split()))))


# with open("res2.txt", "w") as f:
#     f.write("Файл — именованная область данных на носителе информации, используемая как базовый объект взаимодействия"
#             " с данными в операционных системах.")
#
#
# def longest_words(file):
#     with open(file) as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_words("res2.txt"))


# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
# with open("one.txt", "w") as f:
#     f.write(text)
#
# with open("one.txt", "r") as fr, open("two.txt", "w") as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)


# import os

# print(os.getcwd()) # путь к текущей директории
#
# print(os.listdir()) # возвращает список директорий и файлов
# print(os.listdir(".."))
# print(os.listdir(".venv"))

# os.mkdir("folder") # создает папку
# os.rmdir("folder")  # удаляет папку


# os.makedirs("nested1/nested2/nested3") # создает папки в папках по заданному в скобках

# os.remove("xyz.txt") # удаляет файл

# os.rename("two.txt", "www.txt") # переименовывает файл

# os.rename("www.txt","folder/www.txt" ) # переместили файл в заданную папку
# os.renames("www.txt","folder/www.txt" ) # переместил файл, создавая промежуточные папки


# 01.04.2025

# print(os.walk("nested1"))
# for root, dirs, files in os.walk("nested1", topdown=True):
#     print("Root:", root)
#     print("\tdirs:", dirs)
#     print("\tfiles:", files)


# import os.path
#
# print(os.path.split(r"C:\Users\User\Desktop\Python\nested1\text.txt"))
#
# print(os.path.join(r"C:\Users", "User", "Desktop", "Python", "nested1", "text.txt"))


# dirs = [r"Work\F1", r"Work\F2\F21"]
# # for d in dirs:
# #     os.makedirs(d)
#
# files = {
#     "Work": ["w.txt"],
#     r"Work\F1": ["f11.txt", "f12.txt", "f13.txt"],
#     r"Work\F2\F21": ["f211.txt", "f212.txt"]
# }
#
# for d, files in files.items():
#     for file in files:
#         file_path = os.path.join(d, file)
#         # print(file_path)
#         open(file_path, "w").close()
#
#
# file_with_text = [r"Work\w.txt", r"Work\F1\f12.txt", r"Work\F2\F21\f211.txt", r"Work\F2\F21\f212.txt"]
#
# for file in file_with_text:
#     with open(file, "w") as f:
#         f.write(f"Такой-то текст в файле {file}")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root1, directory, file_name in os.walk(root, topdown):
#         print(root1)
#         print(directory)
#         print(file_name)
#     print("-" * 50)
#
#
# print_tree("Work", False)
# print_tree("Work", True)

# import os
# import time
#
# # print(os.path.exists(r"C:\Users\User\Desktop\Python\nested1"))  # проверяет правильно указан путь к файлу
# # print(os.path.isfile(r"C:\Users\User\Desktop\Python\nested1"))  # проверяет это файл или папка
# # print(os.path.isdir(r"C:\Users\User\Desktop\Python\nested1"))  # проверяет папка ли это
#
# file = r"C:\Users\User\Desktop\Python\nested1"
#
# print(os.path.getsize(r"C:\Users\User\Desktop\Python\nested1"))  # проверяет размер файла в байтах
# print(os.path.getatime(r"C:\Users\User\Desktop\Python\nested1"))  # возвращает время последнего доступа к файлу
# print(os.path.getmtime(r"C:\Users\User\Desktop\Python\nested1"))  # время послдеднего изменения в файле
# print(os.path.getctime(r"C:\Users\User\Desktop\Python\nested1"))  # возвращает время создания файла
#
#
# a = os.path.getatime(file)
# m = os.path.getatime(file)
# c = os.path.getatime(file)
#
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(a)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(m)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(c)))
#
#

# ООП

# class Point:
#     x = 1 # 100
#     y = 2
#
#
# p1 = Point()
# p1.x = 10
# p1.y = 20
# # Point.x = 100
# print(p1.x, p1.y)
# print(p1.__dict__)
#
#
# p2 = Point()
# print(p2.x, p1.y)
# p2.x = 5
# print(p2.__dict__)
#
# print(Point.__dict__)


# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 2
#
#     def set_coord(self, x1, y1):
#         self.x = x1
#         self.y = y1
#
# p1 = Point()
# print(Point.__doc__)
# print(Point.__dict__)
# print(type(p1))
# # p1.x = 5
# # p1.y = 10
# p1.set_coord(5, 10)
# print(p1.__dict__)
# Point.set_coord(p1, 20, 30)
# print(p1.__dict__)
#
# p2 = Point()
# p2.set_coord(100, 200)
# print(p2.__dict__)


# 03. 04. 2025


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя:{self.name}\Дата рождения:{self.birthday}\Номер телефона: {self.phone}"
#               f"Страна: {self.country}\Город:{self.city}\Домашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # устанавливаем имя
#         self.name = name
#
#     def get_name(self):  # получаем имя
#         return self.name
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-32-56", "Россия", "Москва", "Чистопрудный бульвар 1А")
# h1.print_info()
# h1.set_name("Юлия")
# h1.print_info()
# print(h1.get_name())


# 2 задача


# class Person:
#     skill = 10
#     # name = ""
#     # surname = ""
#
#     def __init__(self,name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __del__(self):
#         print("Удаление экземпляра")
#
#     def print_info(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print("Данные сотрудника", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника", self.skill, "\n")
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info("Виктор", "Резник")
# p1.add_skill(3)
# p2 = Person("Анна", "Долгих")
# p2.print_info("Анна", "Долгих")
# p2.add_skill(2)


# class Point:
#     count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.count)
# print(p1.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         print("Работающих роботов осталось", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
# print("Роботы закончили свою работу. Давайте их выключим")
#
# print("Численность роботов", Robot.k)


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(s):
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         # if (isinstance(x, int) or isinstance(x, float)) and isinstance(y, int) or isinstance(y, float):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coord_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coord_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#
# p1 = Point(5, 10)
# # print(p1.__dict__)
# # p1.z = 20
# # print(p1.__x, p1.__y)
# # p1.x = 50
# # p1.y = "abc"
# p1.set_coord(50, 100)
# print(p1.get_coord())
# p1.set_coord_x(10)
# p1.set_coord_y(50)
# p1._Point__x = "abc"
# print(p1._Point__x)
# print(p1.__dict__)
# # p1.__check_value(5)


# 08.04.2025

# import os
#
# file_path = "test/text4.txt"
#
# if os.path.exists(file_path):
#     directory, name = os.path.split(file_path)
#     atime = os.path.getatime(file_path)
#     print(f"{name} ({directory}) - время последнего доступа к файлу {atime} секунд")
# else:
#     print(f"Файл {file_path} не существует")


# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def set_width(self, width):
#         if Rectangle.__check_value(width):
#             self.__width = width
#
#     def set_length(self, length):
#         if Rectangle.__check_value(length):
#             self.__length = length
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     def get_area(self):
#         return self.__length * self.__width
#
#     def get_perimetr(self):
#         return 2 * (self.__length * self.__width)
#
#     def get_hypotenuse(self):
#         return round(math.sqrt(self.__length ** 2 + self.__width ** 2), 2)
#
#     def get_draw(self):
#         for i in range(self.__length):
#             for j in range(self.__width):
#                 print("*", end="")
#             print()
#
#         # print("*" * self.__width * self.__length)
#
#
# r1 = Rectangle(4, 12)
# r1.set_width(9)
# r1.set_length(3)
# print("Длина прямоугольника", r1.get_length())
# print("Щирина прямоугольника", r1.get_width())
# print("Площадь прямоугольника", r1.get_area())
# print("Площадь прямоугольника", r1.get_perimetr())
# print("Площадь прямоугольника", r1.get_hypotenuse())
# print(r1.get_draw())


# class Point:
#     __slots__ = ["x", "y", "z"]
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.x, p1.y, p1.z)
# # print(p1.__dict__)

# не работает
# class Point():
#     def __int__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __check_value(s):
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     def set_coord_x(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Неверный формат данных")
#
#     def get_coord_x(self):
#         return self.__x, self.__y
#
#     def del_coord_x(self):
#         # if Point.__check_value(x)
#         del self.__x
#
#     def get_coord_y(self):
#         return self.__y
#
#
# p1 = Point(5, "10")
# p1.coordX = "abc"
# print(p1.x)
# def p1.x
# print(p1.__del__)


# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.__old = year
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Igor"
# p1.old = 31
# print(p1.__dict__)
# del p1.name
# print(p1.__dict__)


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# p4 = Point()
#
#
# print(Point.get_count())
# print(p1.get_count())


# def inc(x):
#     return x + 1
#
# def dec(x):
#     return x -1
#
# print(inc(10), dec(10))
#
#
# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#     @staticmethod
#     def dec(x):
#         return x - 1
#
# ch = Change()
# print(Change.inc(10), Change.dec(10))

# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         mx = a
#         if b > mx:
#             mx = b
#         if c > mx:
#             mx = c
#         if d > mx:
#             mx = d
#         return mx
#
#     @staticmethod
#     def min(*args):
#         mn = args[0]
#         for i in args:
#             if i < mn:
#                 mn = i
#         return mn
#
#     @staticmethod
#     def averange(*args):
#         return sum(args) / len(args)
#
#     @staticmethod
#     def factorial(n):
#         fact = 1
#         for i in range(1, n + 1):
#             fact *= i
#         return fact
#
#
# print("Максимальное число", Numbers.max(3, 5, 7, 9))
# print("Минимальное число", Numbers.min(3, 5, 7, 9))
# print("Среднее арифметическое", Numbers.averange(3, 5, 7, 9))
# print("Факториал числа", Numbers.factorial(5))
# # print(Numbers.max(3,5,7,9))
# # min = 5
# # lst = [1, 2, 3, 4, 5, 6, 7]
# # print(max(lst))


# 10.04.2025


# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split("."))
#         date = cls(day, month, year)
#         return date
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# # string_date = "23.01.2025"
# # day, month, year = map(int, string_date.split("."))  # [23, 01, 2025]
# # print(string_date)
# # d = Date(day, month, year)
#
# d = Date.from_string("23.01.2025")
# print(d.string_to_db())

# #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт")
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def convert_to_usd(self):
#         eur_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix} ")
#
#     def print_info(self):
#         print("Информация о счете: ")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#     def edit_owwner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешны начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято")
#             self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#
#
# acc = Account(12345, "Долгих", 0.03, 1000)
# # acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.edit_owwner("Дюма")
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()


# -----------------------

# import re
# from collections.abc import


# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.verifi_fio(fio)
#         self.verifi_old(old)
#         self.verifi_weight(weight)
#         self.verifi_ps(ps)
#
#         self.__fio = fio
#         self.__old = old
#         self.__password = ps
#         self.__weight = weight
#
#     @staticmethod
#     def verifi_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall(r"[a-za-яё-]", fio, flags=re.IGNORECASE))
#         for s in f:
#             # print(s.strip(letters))
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verifi_old(old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 100")
#
#     @staticmethod
#     def verifi_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным")
#
#     @staticmethod
#     def verifi_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # ['1234', '567890'] проверяет 2 ли элемента
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verifi_fio(fio)
#         self.__fio = fio
#
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = "Ветров Игорь Николаевич"


# 15.04.2025

# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verifi_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall(r"[a-za-яё-]", fio, flags=re.IGNORECASE))
#         for s in f:
#             # print(s.strip(letters))
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verifi_old(old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 100")
#
#     @staticmethod
#     def verifi_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным")
#
#     @staticmethod
#     def verifi_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # ['1234', '567890'] проверяет 2 ли элемента
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verifi_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#
#         self.verifi_old(year)
#         self.__old = year
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verifi_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.__weight = w
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = "Ветров Игорь Николаевич"
# print(p1.fio)
# print(p1.__dict__)

# -----------------------------------


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
# print(Point.__dict__)
# print(issubclass(Point, object))
# print(type(5))
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self) -> str:
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20), "green", 5)
# line.draw_line()
#
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()

# -------------------


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if isinstance(w, int) and w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Ширина должна быть положительным числом")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if isinstance(h, int) and h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Высота должна быть положительным числом")
#
#     def area(self):
#         print(f"Площадь {self.color} прямоугольника:", end=" ")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
#
# print(rect.area())
# print(rect.__dict__)

# -------------


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
# # class RectBorder(Rect):
# #     ...
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# # shape2 = RectBorder(600,300,"1px","red")
# # shape2.show_rect()

# -----------

# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)  # "1 2 3"
# print(type(v))


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coord(self, x, y=None):
#         if y is None:
#             self.x = x
#         elif x is None:
#             self.y = y
#         else:
#             self.x = x
#             self.y = y
#
#
# p1 = Point(5, 10)
# p1.set_coord(20, 30)
# print(p1.__dict__)
# p1.set_coord(50)
# print(p1.__dict__)

# 17.04.2025
# Абстрактные методы

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# class Prop:
#     def __init__(self, sp, ep, color, width):
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.width = width
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self.sp}, {self.ep},{self.color}, {self.width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self.sp}, {self.ep},{self.color}, {self.width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование эллипса: {self.sp}, {self.ep},{self.color}, {self.width}")
#
#
# shapes = list()
# shapes.append(Line(Point(0,0),Point(10,10),"yellow", 10))
# shapes.append(Line(Point(10,10),Point(20,20),"red", 6))
# shapes.append(Line(Point(50,50),Point(70,70),"blue", 4))
# shapes.append(Line(Point(80,80),Point(100,100),"green", 3))
#
#
# for i in shapes:
#     i.draw()

# ----------------

# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную доску")
#
#     @abstractmethod
#     def move(self):
#         print("Метод Move() в базовом классе")
#
#
# class Queen(Chess):
#
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на е2е4")
#
# # q = Chess()
# q = Queen()
# q.draw()
# q.move()

# -------------


# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):  # 20, None, None
#         if radius is None:
#             if length is None:
#                 self.width = self.length = width
#             else:
#                 self.width = width
#                 self.length = length
#         else:
#             self.radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class RectangleTable(Table):
#     def calc_area(self):
#         return self.width * self.length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self.radius ** 2, 2)
#
#
# t = RectangleTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t1 = RectangleTable(20)
# print(t1.__dict__)
# print(t1.calc_area())
#
# t2 = RoundTable(radius=20)
# print(t2.__dict__)
# print(t2.calc_area())

# --------------

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     suffix = "RUB"
#
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#     def print_info(self):
#         self.print_value()  # Dollar(5)
#         print(f"= {self.convert_to_rub():.2f} {Currency.suffix}")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
# print("*" * 50)
# for elem in d:
#     elem.print_info()
#
#
# print("*" * 50)
# for elem in e:
#     elem.print_info()
#

# --------------------

# Интерфейсы

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child Class")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild Class")
#
#
# gc = GrandChild()
# gc.display1()
# gc.display2()


# Вложенные классы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_static_method():
#         print("Статический метод")
#
#     class MyInner:
#         def __init__(self, inner_inner, obj):
#             self.inner_inner = inner_inner
#             self.obj = obj
#
#         def inner_method(self):
#             print("Метод внутреннего класса", MyOuter.age, self.obj.name)
#             print(self.inner_inner)
#             MyOuter.outer_static_method()
#             self.obj.outer_obj_method()
#
#         def outer_obj_method(self):
#             print("Метод экземпляра", self.name)
#
#
# out = MyOuter("Внешний")
# print(out.name)
# # inner = MyOuter.MyInner("внутренний")
# inner = out.MyInner("внутренний", out)
# print(inner.inner_inner)
# inner.inner_method()

# ---------

# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightColor()
#         self.dg = self.DarkColor()
#
#     def show(self):
#         print("Name", self.name)
#
#     class LightColor:
#         def __init__(self):
#             self.name = "LightGreen"
#
#         def display(self):
#             print("Name", self.name)
#
#     class DarkColor:
#         def __init__(self):
#             self.name = "DarkGreen"
#
#         def display(self):
#             print("Name", self.name)
#
#
# outer = Color()
# outer.show()
# print(outer.name)
# g = outer.lg
# g.display()
# g1 = outer.dg
# g1.display()

# --------
# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#
#     class CPU:
#         def make(self):
#             return "intel"
#
#         def model(self):
#             return "Core -i9"
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())

# ------------
# 22.04.2025

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     # def __str__(self):
#     #     return f"{self.name}"
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)

# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(10, 20)
# # p1.z = 30
# # print(p1.__dict__)
# print(p1.length)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(10, 20)
# p2 = Point2D(10, 20)
# print("p1 = ", p1.__sizeof__())
# print("p2 = ", p2.__sizeof__() + p2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
#
# class Point3D(Point):
#     __slots__ = 'z',
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# print(pt3.x, pt3.y, pt3.z)
# # pt3.z = 30
# # print(pt3.z)
# # print(pt3.__dict__)

# ------------------------
# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " os barking")
#
#
# dog = Dog("Buddy")
# dog.bark()
# dog.sleep()
# dog.play()


# class A:
#     def __init__(self):
#         print("Инициализатор класса А")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#
# class C(A):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Инициализатор класса D")
#
# d = D()
# print(D.mro())
# # print(D.__mro__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"{self.__x}, {self.__y}"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self.color = color
#         self.width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инициализатор класса Pos")
#         self.sp = sp
#         self.ep = ep
#         Styles.__init__(self, *args)
#         super().__init__(*args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()


# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 17:15")
#
#
# class Goods:
#     def __init__(self, name, weight, price):
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#         super().__init__()
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class Notebook(Goods, MixinLog):
#     pass
#
#
# n = Notebook("HP", 1.5, 35000)
# n2 = Notebook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()
# n2.save_sell_log()

# ------------------------------

# Перегрузка операторов

# Число секунд в одном дне: 24 * 60 * 60 = 86400

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

# ------------
# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         return self.marks[2]
#
#
# s1 = Student("Сергей", 5, 3, 3, 4, 5)
# print(s1.marks[2])
# print(s1[2])


# 25.04.2025
# ---------------------

# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#         # self.marks[key] = value
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # off = 10 + 1 - 5 => 6
#             self.marks.extend([None] * off)  # [5,5,3,4,None, None, None, None, None]
#
#         self.marks[key] = value    # [5, 3, 3, 4, 5, None, None, None, None, None, 4]
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Сергей", 5, 3, 3, 4, 5)
# print(s1.marks[2])
# print(s1[2])
# s1[10] = 4
# del s1[2]
# print(s1.marks)
#
# print([None] * 6)

# ------------------

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
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError(" Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         if item == "min":
#             return (self.sec // 60) % 60
#         if item == "sec":
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError(" Ключ должен быть строкой")
#
#
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == "hour":
#             self.sec = s + 60 * m * value * 3600
#         if key == "min":
#             self.sec = s + 60 * value + h * 3600
#         if key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
#
# c1 = Clock(8000)
# print(c1.get_format_time())
# c1["hour"] = 1
# c1["min"] = 20
# c1["sec"] = 30
# print(c1["hour"], c1["min"], c1["sec"])


# ---------
# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         if self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name={self.name}, age={self.age}, pol={self.pol})"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(["M", "F"])) for _ in range(randint(2,9))]
#
#         else:
#             raise TypeError("Type are not supported")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# # cat3 = Cat("Murzik", 3, "R")
# print(cat1)
# print(cat2)
# # print(cat3)
# print(cat1 + cat2)
#
#
# ----------------
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def perimeter(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def perimeter(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.perimeter())

# ----------------
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Cat(Animal):
#     def info(self):
#         print(f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}.")
#
#     def make_sound(self):
#         print(f"{self.name} мяукает.")
#
#
# class Dog(Animal):
#     def info(self):
#         print(f"Я собака. Меня зовут {self.name}. Мой возраст {self.age}.")
#
#     def make_sound(self):
#         print(f"{self.name} гавкает.")
#
#
# cat = Cat("Пушок", 2.5)
# dog = Dog("Мухтар", 4)
#
# for animal in cat, dog:
#     animal.info()
#     animal.make_sound()
#


# ---------------

# from abc import ABC, abstractmethod
#
#
# class Human(ABC):
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     @abstractmethod
#     def info(self):
#         print(f"\n{self.surname} {self.name} {self.age}", end=" ")
#
#
# class Student(Human):
#     def __init__(self, name, surname, age, speciality, groups, rating):
#         super().__init__(name, surname, age)
#         self.speciality = speciality
#         self.groups = groups
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.groups} {self.rating}", end=" ")
#
#
# class Teacher(Human):
#     def __init__(self, name, surname, age, subject, experience):
#         super().__init__(name, surname, age)
#         self.subject = subject
#         self.experience = experience
#
#     def info(self):
#         super().info()
#         print(f"{self.subject} {self.experience}", end=" ")
#
#
# class Graduate(Student):
#     def __init__(self, name, surname, age, speciality, groups, rating, topic):
#         super().__init__(name, surname, age, speciality, groups, rating)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f"{self.topic}")
#
#
# group = [
#     Student("Даши", "Батодалаев", 16, "ГК", "Web_011", 5),
#     Student("Линар", "Загидуллин", 32, "РПО", "PD_011", 5),
#     Teacher("Андрей", "Даньшин", 38, "Астрофизика", 110),
#     Graduate("Сергей", "Шугани", 15, "PПО", "PD_011", 5,
#              "Защита персональных данных")
# ]
#
# for i in group:
#     i.info()


# Функторы

# class Counter:
#     def __init__(self):
#         self.count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         print(self.count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()


# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(chars)
#
#     return wrap
#
# s1 = string_strip("?:!.;")
# print(s1("Hello World! ..."))
#
#
# class StringStrip:
#     def __init__(self,chars):
#         self.chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return args[0].strip(self.chars)
#
#
# s2 = string_strip("?:!.;")
# print(s1("Hello World! ..."))


# 29.05.2025 (31 урок)

# class MyDecorator:
#     def __init__(self,fn):
#         self.func = fn
#
#
#     def __call__(self, *args, **kwargs):
#         print("Перед вызовом функции")
#         self.func()
#         print("После вызова фурнкции")
#
# @MyDecorator
# def func():
#     print("text")
#
# func()


# class MyDecorator:
#     def __init__(self,fn):
#         self.func = fn
#
#
#     def __call__(self, a, b):
#         # print("Перед вызовом функции")
#         # self.func()
#         # print("После вызова фурнкции")
#         return f"Перед вызовом функции \n{self.func(a, b)} \nПосле вызова функции"
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
# print(func(2, 5))


# -------------

# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         return self.func(a, b) ** 2
#
#
# @Power
# def multiply(a, b):
#     return a * b
#
#
# print(multiply(2, 3))

# --------------


# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, *args, **kwargs):
#         return f"Перед вызовом функции \n{self.func(*args, **kwargs)} \nПосле вызова функции"
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# @MyDecorator
# def func2(a, b, c):
#     return a * b * c
#
#
# print(func(2, 5))
# print(func2(2, 5, 3))


# ----------

#
# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrapper(a, b):
#             return func(a, b) ** self.arg
#
#         return wrapper
#
#
# @Power(3)
# def multiply(a, b):
#     return a * b
#
#
# @Power(5)
# def multiply1(a, b):
#     return a + b
#
#
# print(multiply(2, 2))
# print(multiply1(3, 2))


# -----------------

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#     @dec
#     def method1(self, arg):
#         print("Вывод аргумента:", arg)
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()
# p1.method1("значение")


# Метаклассы


# a = 5
# print(type(a))
# print(type(int))


# class MyList(list):
#     def get_length(self):
#         return len(self)

# MyList = type(
#     "MyList",
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
#
# lst = MyList()
# lst.append(5)
# lst.append(7)
# lst.append(9)
# print(lst, lst.get_length())


# Создание модулей
# import geometry.rect
# import geometry.sq
# import geometry.trian

#
# from geometry import rect, sq, trian
# from geometry import *
#
# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
#
# s1 = sq.Square(10)
# s2 = sq.Square(20)
#
# t1 = trian.Triangle(1, 2, 3)
# t2 = trian.Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.perimeter())

# def ran():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.perimeter())


# занятие 32 13.06.2025

# import pickle


# file_name = "basket.txt"
#
#
# shop_list = {
#     "Фрукты": ["яблоки", "манго"],
#     "овощи": ("морковь", "лук"),
#     "бюджет": 1000
# }
#
# with open(file_name, "wb") as f:
#     pickle.dump(shop_list, f)
#
# with open(file_name, "rb") as f:
#     shop_list2 = pickle.load(f)
#
# print(shop_list2)

# class Test:
#     num = 25
#     st = "Привет"
#     lst = [1,2,3]
#     tpl = [22,33]
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\nКортеж: {Test.tpl}"
#
# obj = Test()
# # print(obj)
#
# string = pickle.dumps(obj)
# print(string)
#
# string2 = pickle.loads(string)
# print(string2)


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
# item1 = Test2()
# print(item1)
# item2 = pickle.dumps(item1)
# print(item2)
# item3 = pickle.loads(item2)
#
# print(item3.__dict__)

# import json
#
# data = {
#     'name': 'Olga',
#     'age': 35,
#     '20': None,
#     'None': "no",
#     'True': False,
#     'hobbies': ('running', 'signing'),
#     'children': [
#         {
#             "firstName": 'Alice',
#             'age': 6
#         }
#     ]
# }

# with open("data_file.json", "w") as f:
#     json.dump(data, f, indent=4)
#
# with open("data_file.json", "r") as f:
#     data1 = json.load(f)
#
# print(data1)
# ---------


# string = json.dumps(data, sort_keys=True)
# print(string, type(string))
#
# data1 = json.loads(string)
# print(data1, type(data1))

# ----
# x = {"name": "Виктор"}
# print(json.dumps(x))
# print(json.dumps(x, ensure_ascii=False))
#
# st = json.dumps(x)
# print(json.loads(st))


# -------
# import json
# from random import choice
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person
#
#
# def write_json(person_dict):  # {'name': ..., 'tel': ...}
#     try:
#         data = json.load(open("persons.json"))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#
#     with open("persons.json", "w") as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())
#


#--------------

import json

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        # st = ''
        # for i in self.marks:
        #     st += str(i) + ", "
        # return f"Студент => {self.name}: {st[:-2]}"
        # st = ", ".join(map(str, self.marks))
        # return f"Студент => {self.name}: {st}"
        return f"Студент => {self.name}: {', '.join(map(str, self.marks))}"

    def add_mark(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self, index, new_mark):
        self.marks[index] = new_mark

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 1)

    def get_file_name(self):
        return self.name + ".json"  # 'Bodnya.json'

    def dump_to_json(self):
        data = {"name": self.name, "marks": self.marks}
        with open(self.get_file_name(), "w") as f:
            json.dump(data, f)

    def load_from_file(self):
        with open(self.get_file_name(), "r") as f:
            print(json.load(f))


class Group:
    def __init__(self, students, group):
        self.students = students
        self.group = group

    def __str__(self):
        st = "\n".join(map(str, self.students))
        return f"Группа: {self.group}\n{st}"

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)

    @staticmethod
    def change_group(gr1, gr2, index):
        # st = gr1.remove_student(index)
        # gr2.add_student(st)
        gr2.add_student(gr1.remove_student(index))

    def get_file_name(self):
        return self.group.lower().replace(" ", "-") + ".json"

    def dump_to_json(self):
        data = [
            {'name': student.name, 'marks': student.marks} for student in self.students
        ]
        with open(self.get_file_name(), "w") as f:
            json.dump(data, f, indent=2)

    def load_from_file(self):
        with open(self.get_file_name(), "r") as f:
            print(json.load(f))


st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
# print(st1)
# st1.add_mark(4)
# print(st1)
# st1.delete_mark(2)
# print(st1)
# st1.edit_mark(4, 4)
# print(st1)
# print(st1.average_mark())
# st1.dump_to_json()
# st1.load_from_file()
sts1 = [st1, st2]
group1 = Group(sts1, "ГК Python")
# print(group1)
# print()
group1.add_student(st3)
# print(group1)
# print()
group1.remove_student(1)
print(group1)
print()
sts2 = [st2]
group2 = Group(sts2, "ГК Web")
print(group2)
print()
Group.change_group(group1, group2, 0)
print(group1)
print(group2)

group2.dump_to_json()
group2.load_from_file()