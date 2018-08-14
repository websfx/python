#! /usr/bin/env python
# -*- coding: utf8 -*-


names = ["zhouhua", "baobao", "huahua", "zaizai"]
#print(names[1:3]) #不包括结束位置，包括起始位置，即顾头不顾尾。

#print(names[-3:-1])#切片
#names.remove("baobao")
#names.append("meimei")
#del names[1]
names.pop() #默认删除掉最后一个
names.insert(1, "meimei")
# names.copy()复制一份到另外的数组 只copy第一层
#names2 = list(names)
#names.clear() 清空
print(names)

print(names[0:-1:2])