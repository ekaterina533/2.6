#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Вариант 8. Объявите функцию, которая вычисляет площадь круга и возвращает вычисленное значение.
#В качестве аргумента ей передается значение радиуса.


def decorator(func):
    def decorator1(x):
        c = "Площадь круга"
        ret = func(x)
        print(f'{c} = {ret}')
        return ret
    return decorator1


@decorator
def add(x):
    pi = 3.14
    return x * x * pi


if __name__ == "__main__":
    r = float(input("Введите значение радиуса:"))
    add(r)
