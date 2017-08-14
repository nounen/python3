#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2))


nums = [1, 2, 3]

# *nums表示把nums这个list的所有元素作为可变参数传进去
print(calc(*nums))
