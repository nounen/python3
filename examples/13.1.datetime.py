#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

# 获取当前日期和时间
now = datetime.now()
print(now) # 2017-09-02 21:37:37.310937

print(type(now)) # <class 'datetime.datetime'>

# 注意到 datetime 是模块，datetime 模块还包含一个 datetime 类，通过 from datetime import datetime 导入的才是 datetime 这个类

# 如果仅导入import datetime，则必须引用全名datetime.datetime


# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20) # 2015-04-19 12:20:00

print(dt)


# datetime转换为timestamp
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为 **timestamp**

dtt = dt.timestamp()
print(dtt) # 1429417200.0

# Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数


# timestamp转换为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t)) # 2015-04-19 12:20:00


# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday) # 2015-06-01 18:19:59
