#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

be = base64.b64encode(b'binary\x00string')
print(be) # b'YmluYXJ5AHN0cmluZw=='

bd = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(bd) # b'binary\x00string'

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
# b'abcd++//'

base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
# b'abcd--__'

base64.urlsafe_b64decode('abcd--__')
# b'i\xb7\x1d\xfb\xef\xff'
