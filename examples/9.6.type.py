#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Hello(object):
    def hello(self, name='World'):
        print('Hello, %s.' % name)

h = Hello()
h.hello()

# 类, 它的类型是 'type'
print(type(Hello)) # <class 'type'>

# 对象, 它的类型就是 Hello
print(type(h))     # <class '__main__.Hello'>



# 通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义

# 先定义函数

def fn(self, name="world"):
    print('hello, %s. ' % name)

# 创建 Hello class
Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()
print(type(Hello))  # <class 'type'>
print(type(h))      # <class '__main__.Hello'>
"""
要创建一个class对象，type()函数依次传入3个参数：

1.class的名称；
2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上
"""
