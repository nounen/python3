#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 对 list 进行排序
l = sorted([34, 5, -12, -21])
print(l) # [-21, -12, 5, 34]


# 按绝对值大小排序
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
l = sorted([34, 5, -12, -21], key=abs)
print(l) # [5, -12, -21, 34]


# 按字符串排序, 是按 ASCII 的大小比较的,
l = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(l) # ['Credit', 'Zoo', 'about', 'bob']


# 按字符串忽略大小写排序
l = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(l) # ['about', 'bob', 'Credit', 'Zoo']


# 反向排序，不必改动key函数，可以传入第三个参数` reverse=True`
l = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(l) # ['Zoo', 'Credit', 'bob', 'about']
