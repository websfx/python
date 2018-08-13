#! /usr/bin/env python
# -*- coding: utf8 -*_


import getpass

_username = "xiyangxixi"
_password = "123456"
username = input("username: ")
password = getpass.getpass("password: ")

if _username == username and _password == password:
    print("welcome username {name} login ".format(name=username))
else:
    print("not correct")

