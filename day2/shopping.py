#! /usr/bin/env python
# -*- coding: utf8 -*-


product = [
    ("huahua", 1000),
    ("zaizai", 2000),
    ("meimei", 3000),
]

salary = input("请输入工资：")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(product):
            print(index + 1, item)
        break
