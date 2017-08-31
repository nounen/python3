#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

print(s.name)
print(s.score)

del s.name
# print(s.name) # AttributeError, 不能通过对象属性访问, 但是还能通过类属性访问到


class StudentNew(object):
    name = 'StudentNew'

# 访问类的属性, 没有通过实例化
print(StudentNew.name)
