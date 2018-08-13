#! /usr/bin/env python
# -*- coding: utf8 -*_
age = 25
count = 0
while count <3:
    guess_age = int(input("guess_age: "))
    if guess_age == age:
        print("you got it")
        break
# break是结束当前循环
# continue 跳出本次循环，进入下一次循环
    elif guess_age > age:
        print("biger")
    else:
        print("smaller")
    count +=1
    if count ==3:
        continue_confirm = input("continue: ")
        if continue_confirm != 'n':
            count = 0
#else:
 #   print("you have tried too many times")