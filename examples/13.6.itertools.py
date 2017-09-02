#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

# 无线迭代器
natuals = itertools.count(1)
for n in natuals:
    print(n)
    if n == 10: # 因为count()会创建一个无限的迭代器
        break

# 无限重复
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)

# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c) # 'A' 'B' 'C' 'X' 'Y' 'Z'


# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
"""
A ['A', 'A', 'A']
B ['B', 'B', 'B']
C ['C', 'C']
A ['A', 'A', 'A']
"""

# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算
