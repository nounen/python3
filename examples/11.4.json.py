#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# json 编码
d = dict(name='Bob', age=20, score=88)
j = json.dumps(d)
print(j) # '{"score": 88, "age": 20, "name": "Bob"}'

# json 解码
j = '{"score": 88, "age": 20, "name": "Bob"}'
d = json.loads(j)
print(d) # dict, {'score': 88, 'age': 20, 'name': 'Bob'}
print(d['name']) # Bob


# JSON 进阶
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

# Student 对象不是一个可序列化为 JSON 的dict


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score,
    }

# Student 实例首先被 student2dict() 函数转换成 dict，然后再被顺利序列化为JSON
s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))


# 如果遇到一个 Teacher 类的实例，照样无法序列化为 JSON
# 我们可以偷个懒，把任意 class 的实例变为 dict
# 因为通常 class 的实例都有一个 __dict__ 属性，它就是一个 dict，用来存储实例变量
print(json.dumps(s, default=lambda obj: obj.__dict__))

# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，
# loads()方法首先转换出一个dict对象，然后，我们传入的 object_hook 函数负责把 dict 转换为Student实例
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

j_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(j_str, object_hook=dict2student)) # json 编码出来是 Student 对象, <__main__.Student object at 0x7f841016cef0>
