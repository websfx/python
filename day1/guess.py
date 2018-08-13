#! /usr/bin/env python
# -*- coding: utf8 -*_

age_of_me = 25



guess_age =int(input("guess_age: "))

if guess_age == age_of_me:
    print("yes, you got it")
elif guess_age >age_of_me:
    print("no, small")
else:
    print("no, big")