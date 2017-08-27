#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 创建一个generator，有很多种方法。
# 第一种方法很简单，只要把一个列表生成式 range 的[]改成()，就创建了一个generator
g = (x * x for x in range(10))
print(g) # <generator object <genexpr> at 0x7efcc2c32258>

# 打印 generator 的每一个元素, next() 函数
# print(next(g)) # 0
# print(next(g)) # 1
# print(next(g)) # 4


# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，
# 直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误


# generator也是可迭代对象, 所以可以使用 for 循环
# 基本上永远不会调用next()，而是通过for循环来迭代它
for n in g:
    print(n)


# 斐波拉契数列（Fibonacci）, 除第一个和第二个数外，任意一个数都可由前两个数相加得到:
# eg: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)

# 上面的函数和generator仅一步之遥
# 要把fib函数变成generator，只需要把print(b)改为 yield b就可以了
def fib_yield(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib_yield(6)
print(f) # <generator object fib_yield at 0x7fa7153362b0>

for v in f:
    print(v) # 但是拿不到 return 的返回值

# 可以捕捉 StopIteration 错误来拿到 return 的返回值
g = fib_yield(6)

while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
