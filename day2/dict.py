#! /usr/bin/env python
# -*- coding: utf8 -*-


# 字典是一种key-value的数据类型。就像使用字典一样。
# 有则改，无则添加
dict_test = {
    'stu1': "huahua",
    'stu2': "zaizai",
    'stu3': "zhouzhou",
}

print(dict_test)
print(dict_test["stu1"])
dict_test["stu1"] = "张三"
print(dict_test)
dict_test["stu55"] = "李四"
del dict_test["stu1"]
dict_test.pop("stu2")
print(dict_test)

print(dict_test.get("stu1000"))
print("stu200" in dict_test)