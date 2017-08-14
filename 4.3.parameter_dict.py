#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# name: Adam age: 45 other: {'job': 'Engineer', 'gender': 'M'}
person('Adam', 45, gender='M', job='Engineer')


extra = {'city': 'Beijing', 'job': 'Engineer'}

# **xx 简化 dict 传参
person('Jack', 24, **extra)
