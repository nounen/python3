#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成元素 1 到 10 的 list
l = list(range(1, 11))
print(l)

# 生成[1x1, 2x2, 3x3, ..., 10x10]
l = [x * x for x in range(1, 11)]
print(l)

# for循环后面还可以加上if判断
l = [x * x for x in range(1, 11) if x % 2 == 0] # 只保留偶数
print(l)

# 把 list 中所有的字符串编程小写:
L = ['Hello', 'Wrold']
l = [s.lower() for s in L]
print(l) # ['hello', 'wrold']
