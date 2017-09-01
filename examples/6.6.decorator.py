#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 装饰器

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()
"""
call now():
2015-3-25
"""

# 把@log放到now()函数的定义处，相当于执行了语句 `now = log(now)`



# decorator 本身需要传入参数

def log_new(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log_new('execute')
def now_new():
    print('2015-3-25')

now_new()
"""
execute now_new():
2015-3-25
"""

# 和两层嵌套的decorator相比，3层嵌套的效果是这样的： `now = log('execute')(now)`
"""
剖析上面的语句，首先执行log('execute')，返回的是decorator函数，
再调用返回的函数，参数是now函数，
返回值最终是wrapper函数
"""

# 问题: now_new 的 __name__ 属性已经变成 wrapper
print(now_new.__name__)

# 解决上面的问题, 一个完整的decorator的写法如下:
import functools

def log_full(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log_full('execute')
def now_full():
    print('2015-3-25')

now_full()
print(now_full.__name__) # now_full, 正确
