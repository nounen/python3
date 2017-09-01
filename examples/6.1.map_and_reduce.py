#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# map
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4])

# 由于结果r是一个Iterator，Iterator是惰性序列
# 因此通过list()函数让它把整个序列都计算出来并返回一个list
print(list(r)) # [1, 4, 9, 16]


# 把这个list所有数字转为字符串
l = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)


# reduce. reduce 把结果继续和序列的下一个元素做累积计算
from functools import reduce

def add(x, y):
    return x + y

r = reduce(add, [1, 2, 3, 4]) # 10
print(r)

# 使用 lambda 函数进一步简化
r = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(r) # 15
