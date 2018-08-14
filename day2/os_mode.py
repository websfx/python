#! /usr/bin/env python
# -*- coding: utf8 -*-

import os
#os.system("dir") #在系统上执行命令
cmd = os.popen("dir").read()

print("---", cmd)
