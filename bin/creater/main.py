
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@NAME		:creater
@TIME		:2020/09/26 22:16:00
@AUTHOR     :watalo
@VERSION	:0.0.x
'''

import datetime
import os
import sys

import config
# from docs import conf


class Portfiolo:
    '''
    构建文件夹模版的类
    '''
    def __init__(self,name):
        self.name = name
        self.desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        self.init()

    def init(self):
        target_ = os.path.join(self.desktop_path,self.name)
        time = datetime.datetime.now()
        if os.path.exists(target_) == False:
            target_ = ''.join([target_,str(time)])
            os.mkdir(os.path.join(target_))
            for i in ['1-基本情况','2-经营情况','3-财务情况','4-融资情况','5-担保措施','6-调查报告','7-业务资料','8-贷后管理']:
                target_sub = os.path.join(target_,i)
                os.mkdir(target_sub)
                print(target_sub)
        else:
            print('文件夹已存在，请仔细检查！')


        def notice():
            pass


if __name__ == '__main__':
    name ='测试'
    p = Portfiolo(name)
    print(p.desktop_path)
    path = config.Path()
    print(path.root_path)
    # conf.main()