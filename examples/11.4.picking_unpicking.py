#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
import os

pwd = os.path.dirname(__file__)

# 序列化 (为二进制)
d = dict(name = "Bob", age = 20, score = 80)

# 把任意对象序列化成一个 bytes (可以把这个 bytes 写入文件)
pickle_d = pickle.dumps(d)
print(pickle_d)


# 直接把对象序列化后写入一个file-like Object
f = open(pwd + "/dump.txt", 'wb')
pickle.dump(d, f)
f.close()

# 把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象
f = open(pwd + "/dump.txt", 'rb')
d = pickle.load(f)
f.close()
print(d)

# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是 **它只能用于Python**
