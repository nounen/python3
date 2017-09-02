#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一大类
class Animal(object):
    pass


# 第二大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass


# 第三大类
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# 现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类

class Runnable(object):
    def run(self):
        print('Running')

class Flyable(object):
    def fly(self):
        print('Flying')


# 多重继承
class Dog(Mammal, Runnable):
    pass

d = Dog()
d.run() # Running

class Bat(Mammal, Flyable):
    pass

b = Bat()
b.fly() # Running



# MixIn
# TODO: 不明白 MixIn, 不就是多重继承麽?
