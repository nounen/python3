#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

b = Student('Bart', 20)
c = Student('Cast', 30)

b.print_score()
c.print_score()
