#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score, private_name="Pname"):
        self.name = name
        self.score = score
        self.__private_name = private_name

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

b = Student('Bart', 20)
c = Student('Cast', 30)

b.print_score()
c.print_score()

# print(b.__private_name)       # 不能直接访问私有属性, 会报错
print(b._Student__private_name) # 访问私有属性的小技巧
