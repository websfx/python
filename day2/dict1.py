#! /usr/bin/env python
# -*- coding: utf8 -*-


cinema = {
    "american": {
        "001": ["001", "002"]
    },
    "rihai": {
        "002": ["003", "004"]
    },
    "dalu": {
        "003": ["005", "006"]
    },
}

print(cinema)
#cinema.update() 合并，有就更新，无就增加
cinema["dalu"]["003"][1] = "000"
c = cinema.fromkeys([11, 22, 33]) #初始化字典，前提是只有一层
print(c)
print(cinema)

print(cinema.items())

print("------------------")

#for k, v in cinema.items():
 #   print(k, v)  这种循环不高效，因为需要转换成列表，使用下面一种

for item in cinema:
    print(item, cinema[item])