#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct

# struct的pack函数把任意数据类型变成bytes
r = struct.pack('>I', 10240099)
print(r) # b'\x00\x9c@c'

# '>I'的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数


# unpack把bytes变成相应的数据类型
r = struct.unpack('>I', b'\x00\x9c@c')
print(r) # (10240099,)
