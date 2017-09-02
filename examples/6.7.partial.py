#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

int2 = functools.partial(int, base = 2)

r = int2('1000000')
print(r) # 64

r = int2('1000000', 10)
print(r)
