#! /usr/bin/env python
# -*- coding: utf-8 -*-

# import time
#
# time_tup = time.time()
# print((time_tup))
# t1 = "2019-01-14 00:00:00"
#
# time_tup2 = time.mktime(time.strptime(t1,'%Y-%m-%d %H:%M:%S'))
# print(time_tup2)

import datetime

now_time = datetime.datetime.now()

before_time = now_time + datetime.timedelta(days=-7)

print(before_time)