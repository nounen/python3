#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}

# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
for key in d:
    print(key)

# 字符串也是可迭代对象
for ch in 'ABC':
    print(ch)

# 如何判断一个对象是可迭代对象呢？
# 方法是通过collections模块的Iterable类型判断
print(isinstance('abc', Iterable)) # True

print(isinstance([1, 2, 3], Iterable)) # True

print(isinstance(123, Iterable)) # False

# list 下标循环
# 使用 enumerate 函数把一个 list 编程 索引-元素 对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
"""
0 A
1 B
2 C
"""

# for 循环里同时引用两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
"""
1 1
2 4
3 9
"""
