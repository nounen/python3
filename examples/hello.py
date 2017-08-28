#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'Lxxx'

import sys

def test():
    args = sys.argv

    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

"""
第1行和第2行是标准注释:
    第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，
    第2行注释表示.py文件本身使用标准UTF-8编码

第4行是一个字符串，表示模块的文档注释:
    任何模块代码的第一个字符串都被视为模块的文档注释

第6行使用 __author__ 变量把作者写进去

以上就是Python模块的标准文件模板，当然也可以全部删掉不写

可以在命令行执行 `python3 7.1.module_hello.py xxx`
"""


if __name__ == '__main__':
    test()
