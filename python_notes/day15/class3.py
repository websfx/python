#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 封装到init方法中
class foo:
    # 初始化
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        self.blood = "o"
    def test(self,content):
        print(self.name,self.sex,self.blood,content)

obj = foo("huahua","male") # 自动执行init方法
obj.test("xxxxxxxxx")


