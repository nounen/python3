#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import struct

pwd = os.path.dirname(__file__)
thefile = pwd + "/io.text"

# 打开文件, 读取文件内容, 关闭文件
try:
    f = open(thefile, 'r')
    content = f.read() # 一次读取文件的全部内容, 读到内存
    print(content)
finally:
    f.close()


# 使用 with 语句自动调用 close() 方法
with open(thefile, 'r') as f:
    print(f.read())


# 分段读取文件内容
"""
1. read(size) 每次最多读取 size 字节的内容
2. 调用 readline() 每次读取一行内容
3. 调用 readlines() 一次读取所有内容并按行返回 list
"""

f = open(thefile, 'r')

for line in f.readlines():
    print(line.strip())

f.close()

## file-like Object
"""
像 open() 函数返回的这种有个 read() 方法的对象，在 Python 中统称为 file-like Object

除了 file 外，还可以是内存的字节流，网络流，自定义流等等

StringIO就是在内存中创建的file-like Object，常用作临时缓冲
"""

# 二进制文件
f = open(thefile, 'rb')
content = f.read()
print(content) # 十六进制表示的字节 b'\xe8\xbf\x99\xe9\xa3\x8e\x...'
f.close()

# 字符编码
# 比如文件是 gbk 格式的, 用 gbk 解码才查看才不会乱码
f = open(thefile, 'r', encoding='gbk', errors='ignore')
content = f.read()
print(content)
f.close()


# 写文件
f = open(pwd + "/io_w.text", 'w')
f.write('hello, world!')
f.close()

# 写二进制文件: 不同类型变量各自转为 二进制, 然后才能被写入
f = open(pwd + "/io_wb.text", 'wb')
theint = 11
thebites = struct.pack('i', theint)
print(thebites)
f.write(thebites)
f.close()

# 去读二进制文件: 读取出来的是二进制, 需要再转换 (不知道是什么格式的二进制岂不是很但疼)
f = open(pwd + "/io_wb.text", 'rb')
content = f.read()
content = struct.unpack('i', content) # unpack返回的是tupl
print(content)
f.close()
