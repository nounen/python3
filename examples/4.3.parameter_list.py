#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add_end(L=[]):
    L.append('end')
    return L


print(add_end())
# ['END']


print(add_end([1, 2, 3]))
# [1, 2, 3, 'END']


print(add_end())
# 'END', 'END'] 异常


# 修正异常
def fix_add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
