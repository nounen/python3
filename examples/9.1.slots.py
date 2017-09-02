#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    pass

# 给实例绑定一个属性
s = Student()
s.name = "Michael"
print(s.name)


# 给实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25)
print(s.age) # 25


# 给一个实例绑定方法, 对另一个实例是不起作用的 (又不是绑定在 类 上, 当然没有作用)


# 给 类 绑定方法, 所有实例均可调用
Student.set_age = set_age # 给 class 绑定方法

s = Student()
s.set_age(666)
print(s.age) # 666


# 使用 __slots__
# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性
# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性

class StudentNew(object):
    __slots__ = ('name', 'age') # 使用 tuple 定义允许绑定的属性名称

s = StudentNew()
s.name = "Michael"
s.age = 24
# s.score = 11 # 报错, AttributeError: 'StudentNew' object has no attribute 'score'

# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
