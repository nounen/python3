#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("Begin")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s ...' % self.name)

# 把自己写的资源对象用于with语句
with Query('Bob') as q:
    q.query()
"""
Begin
Query info about Bob ...
End
"""



# @contextmanager
# 编写 __enter__ 和 __exit__ 仍然很繁琐，因此 Python 的标准库 contextlib 提供了更简单的写法，上面的代码可以改写如下
from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

# @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了

with create_query('Bob') as q:
    q.query()
"""
End
Begin
Query info about Bob...
End
"""


# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")
"""
<h1>
hello
world
</h1>

代码的执行顺序是：
    1. with 语句首先执行 yield 之前的语句，因此打印出<h1>；
    2. yield 调用会执行 with 语句内部的所有语句，因此打印出hello和world；
    3. 最后执行yield之后的语句，打印出</h1>。
"""



# @closing
# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)


# closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
