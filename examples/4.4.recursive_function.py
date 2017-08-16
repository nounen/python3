#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(3))

# 递归实际计算过程
'''
===> fact(3)
===> 3 * fact(2)
===> 3 * (2 * fact(1))
===> 3 * (2 * 1)
===> 3 * 2
===> 1
'''


# 递归调用栈溢出
'''
print(fact(1000))
'''

# 解决递归调用栈溢出的方法是通过 **尾递归** 优化，事实上尾递归和循环的效果是一样的，
# 所以，把循环看成是一种特殊的尾递归函数也是可以的


# 什么是尾递归
'''
尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
'''


# 尾递归
def fact_new(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact_new(1000))
# 然而还是挂了,
'''
遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，
所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
'''
