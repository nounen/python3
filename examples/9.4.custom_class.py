#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 把对象当作字符串输出

class Student(object):
    def __str__(self):
        return "Student object"

    _repr__ = __str__

s = Student()

print(s) # Student object

print(Student())



# 把对象当作迭代对象

class StudentIteration(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10:
            raise StopIteration()
        return self.a

for n in StudentIteration():
    print(n)
"""
1
1
2
3
5
8
"""



# 像list那样按照下标取出元素
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib()
print(f[10]) # 89
print(f[1]) # 1
"""
其他特殊方法还有:
    * __setitem__()
    * __delitem__()
"""

# TODO: 把 Fib 类扩展成支持切片操作的



# __getattr__, 调用不存在的属性或方法
class StudentAttr(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99

s = StudentAttr()
print(s.name) # Michael
# 当调用不存在的属性时, Python解释器会试图调用 __getattr__(self, 'score') 来尝试获得属性


class StudentFunc(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25

s = StudentFunc()
r = s.age()
print(r) # 25



# __call__, 把对象当作函数来调用
class StudentCall(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = StudentCall('Calling')
s() # My name is Calling.


# 怎么判断一个变量是对象还是函数呢
r = callable(Student())
print(r) # False

r = callable(StudentCall('xx'))
print(r) # True
