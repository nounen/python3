#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

# md5 算法
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest()) # d26a53750bc40b38b65a520292f69306

# 如果数据量很大，可以分块多次调用update(), 并不影响计算结果
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest()) # d26a53750bc40b38b65a520292f69306



# sha1
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest()) # 2c76b57293ce30acef38d98f6046927161b46a44
