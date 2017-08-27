#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取前 3 个元素, 切片: L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3
print(L[0:3]) # ['Michael', 'Sarah', 'Tracy']

# 如果第一个索引是0，还可以省略
print(L[:3])

print(L[1:2])

# 取 倒数第一个元素
print(L[-1:])

# 前10个数，每两个取一个
print(L[:10:2])

# 每5个取一个
print(L[::5])

# 什么都不写，只写 [:] 就可以原样复制一个list
print(L[:])

# tuple也是一种list，唯一区别是tuple不可变。
# 因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
t = (0, 1, 2, 3, 4, 5)
print(t[:3]) # (0, 1, 2)

# 字符串也是一种 list, 也可以切片操作
print('ABCDE'[:3]) # ABC
