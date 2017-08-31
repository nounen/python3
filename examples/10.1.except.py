#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

try:
    print('Try...')
    r = 10 / 0
    print("result: ", r)
except ZeroDivisionError as e:
    print('except:', e) # except: division by zero
    # logging.exception(e)
finally:
    print('finally...')

# 出现 ZeroDivisionError 错误才会被捕捉
# 当然也可以一次性捕捉多个异常, 例如 ValueErroor

# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else: # 如果没有发生错误, 会自动执行 else 语句
#     print('no error!')
# finally:
#     print('finally...')


# 调用堆栈
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     bar('0')
#
# main()


# 记录错误
"""
logging.exception(e)
需要通过配置才能把错误记录到日志文件里
"""

# 抛出错误
class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
