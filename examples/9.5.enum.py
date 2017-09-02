#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 直接访问枚举类的某个属性
print(Month.Jan)
print(Month.Jan.value) # 1, value 是从 1 开始自动赋值给枚举成语的

# 遍历枚举类
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
"""
Jan => Month.Jan , 1
Feb => Month.Feb , 2
Mar => Month.Mar , 3
...

注意: value 属性则是自动赋给成员的 int 常量，默认从1开始计数
"""

# 更精确地控制枚举类型
# @unique装饰器可以帮助我们检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Sun) # Weekday.Sun
print(Weekday.Sun.value) # 0
