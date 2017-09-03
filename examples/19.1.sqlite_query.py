#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('select * from user where id=?', ('1',))

values = cursor.fetchall()

print(values) # [('1', 'Michael')]

cursor.close()

conn.close()
