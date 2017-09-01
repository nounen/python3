#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 过滤, 保留奇数
def is_odd(n):
    return n % 2 == 1

l = list(filter(is_odd, [1, 2, 3, 4, 5, 6]))
print(l) # 1, 3 , 5



# filter 求素数, 埃式算法

# 定义一个 3 开始的奇数序列, 注意这个是一个生成器, 且是一个无线序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


# 定义一个生成器，不断返回下一个素数：

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印100以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break
