#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Вариант 8. Объявите функцию, которая вычисляет площадь круга и возвращает вычисленное значение.
#В качестве аргумента ей передается значение радиуса.
def decorator(func):
    def decorator1(x):
        ret = func(x)
        print('Площадь круга равна')
        return ret
    return decorator1


@decorator
def add(x):
    pi = 3.14
    return x * x * pi


r = float(input("Введите значение радиуса:"))
print("=", round(add(r), 2))


