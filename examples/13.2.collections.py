#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# namedtuple: 扩展 tuple

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y']) # 一个坐标
p = Point(1, 2)
print(p.x)
print(p.y)

# namedtuple是一个函数, 它用来创建一个自定义的tuple对象, 并且规定了tuple元素的个数, 并可以用属性而不是索引来引用tuple的某个元素

r = isinstance(p, Point)
print(r) # True

r = isinstance(p, tuple)
print(r) # True



# deque: 扩展 list
# 使用list存储数据时, 按索引访问元素很快, 但是插入和删除元素就很慢了, 因为list是线性存储, 数据量大的时候, 插入和删除效率很低。

# deque 是为了高效实现插入和删除操作的双向列表, 适合用于队列和栈

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('Y')
print(q) # deque(['Y', 'a', 'b', 'c', 'x'])



# defaultdict: 扩展 dict 访问不存在的元素时返回默认值
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict

from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2']) # 访问不存在的元素返回默认值, N/A


# OrderedDict: 扩展 dict, 让 dict 的key 变成有序的 (重要)

from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d) # {'b': 2, 'c': 3, 'a': 1}, 每次打印元素的顺序都是随机的

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od) # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
od_keys = list(od.keys())
print(od) # rderedDict([('z', 1), ('y', 2), ('x', 3)])
print(od_keys) # ['z', 'y', 'x']

# OrderedDict 可以实现一个 FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key



# Counter, 扩展 dict, 一个简单的计数器

from collections import Counter

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)
# Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'n': 1, 'o': 1, 'i': 1, 'a': 1})
