#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import types

class Animal(object):
    def run(self):
        print('Animal is running...')


# 继承 Animal
class Dog(Animal):
    # 子类方法覆盖父类方法
    def run(self):
        print('Dog is running...')


# 使用 type()
print(type(123)) # <class 'int'>

print(type("123")) # <class 'str'>

print(type(Animal())) # <class '__main__.Animal'>

# 判断对象是否函数, 使用 types 模块中定义的常量
def fn():
    pass

print(type(fn) == types.FunctionType) # True

print(type(abs) == types.BuiltinFunctionType) # True

# types.LambdaType, types.GeneratorType 等等常量


# 使用 isinstance()
a = Animal()
d = Dog()

print(isinstance(a, Animal)) # True

print(isinstance(d, Animal)) # True, 多态

print(isinstance(d, Dog))    # True

# isinstance 也可以判断基本类型
print(isinstance('a', str))

print(isinstance(123, int))

# isinstance 可以判断多个类型
print(isinstance([1, 2, 3], (list, tuple)))


# 使用
print(dir('ABC'))
# ['__add__', '__class__', '__contains__', ... 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# 'ABC'.__len__()

print(dir(d))


# 对象属性相关操作
