#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 远程执行

from fabric.api import *

env.user = "root"
env.password = "123456"
env.hosts = ["192.168.29.101"]

def getHostname():
    run("hostname")