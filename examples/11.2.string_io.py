#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO

# 数据读写不一定是文件，也可以在内存中读写
# StringIO 顾名思义就是在内存中读写 str
f =  StringIO()

s = f.write('hello')
print(s) # 5, 为什么是 5?

s = f.write(' ') # 一个空格
print(s) # 1, 为什么是 1?

s = f.write('world!')
print(s)

print(f.getvalue()) # getvalue()方法用于获得写入后的st
f.close()


# StringIO 初始化字符串, 然后读取
f = StringIO('hello!\nhi\ngoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
