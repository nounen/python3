#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# 系统信息
print(os.name) # posix, 操作系统类型

print(os.uname()) # 获取操作系统详细的系统信息

print(os.environ) # 获取系统环境变量

print(os.environ.get('PATH')) # 某个环境变量的值


# 操作文件和目录

# 当前目录的绝对路径, 怎么少了一级的目录
pwd = os.path.abspath('.')
print(pwd) # /home/lazyou/Nounen/python3

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
# 这样可以正确处理不同操作系统的路径分隔符
testdir = os.path.join(pwd, 'testdir')
print(testdir)

mktestdir = os.mkdir(testdir)
print(mktestdir) # 创建一个目录, 返回值 None; 目录已存在 FileExistsError

rmtestdir = os.rmdir(testdir)
print(rmtestdir) # 同样返回 None


# 文件操作
testfile = pwd + "/file.txt"

filesplit = os.path.split(testfile)
print(filesplit)

filesplitext = os.path.splitext(testfile)
print(filesplitext)

# 文件重命名
# os.rename('test.txt', 'test.py')

# os.remove('test.py')

# 过滤文件, 只要列出目录下的所有目录
dirlist = [x for x in os.listdir('.') if os.path.isdir(x)]
print(dirlist)

# 过滤文件, 只列出 .py 后缀的文件
dirlist = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(dirlist)
