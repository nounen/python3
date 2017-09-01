#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f)      # <function lazy_sum.<locals>.sum at 0x7f65958fc7b8>
print(f())    # 25


# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，
# 所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1()) # 9
print(f2()) # 9
print(f3()) # 9
# 全部是都是 9 , 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量


# 闭包优化
def count_new():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count_new()
print(f1()) # 1
print(f2()) # 4
print(f3()) # 9
