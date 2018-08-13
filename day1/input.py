#! /usr/bin/env python
# -*- coding: utf8 -*-

#username = input("username: ")
#password = input("password: ")
#print(username, password)
username = input("username: ")
password = input("password: ")

info = ''' === info of %s ====
Name: %s
password: %s
''' % (username, username, password)
print(info)