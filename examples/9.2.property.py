#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 检查参数, 为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数
class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100!')
        self._score = value

s = Student()
s.set_score(60)
# s.set_score(1000) # ValueError: score must between 0 - 100!


# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单
# 所有有了内置的 @property 装饰器: 负责把一个方法变成属性调用

class StudentProperty(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = StudentProperty()
s.score = 60    # OK，实际转化为s.set_score(60)
print(s.score)  # OK，实际转化为s.get_score()
