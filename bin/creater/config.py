#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   config.py
@Time    :   2020/09/27 12:40:23
@Author  :   watalo 
@Version :   1.0
@Contact :   watalo@163.com
'''

# 系统配置

import os
import sys
import datetime

class Path():
   def __init__(self):
       self.root_path = os.getcwd()

       

if __name__ == '__main__':

    path = Path()
    print(path.root_path)