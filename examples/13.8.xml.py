#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()

parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data

parser.Parse(xml)

"""
sax:start_element: ol, attrs: {}
sax:char_data:

sax:char_data:
sax:start_element: li, attrs: {}
sax:start_element: a, attrs: {'href': '/python'}
sax:char_data: Python
sax:end_element: a
sax:end_element: li
sax:char_data:

sax:char_data:
sax:start_element: li, attrs: {}
sax:start_element: a, attrs: {'href': '/ruby'}
sax:char_data: Ruby
sax:end_element: a
sax:end_element: li
sax:char_data:

sax:end_element: ol
"""


# 生成 XML
