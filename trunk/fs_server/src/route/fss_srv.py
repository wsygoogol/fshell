# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2016-12-09
# desc: server 数据接入模块主函数


import os
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

import sys    
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("..")
sys.path.append("../net")
sys.path.append("../base")
sys.path.append("../dao")
sys.path.append("../bean")

from fss_cfg import *
from fss_net import *
from fss_srv_manager import *

    
class FssSrv:
    
    def __init__(self):

        self.fssNet         =   FssNet()
        self.managerSrv     =   FssManagerSrv()   


    def init(self):
        
        self.fssNet = g_fssNet
        self.fssNet.append(self.managerSrv.ip, self.managerSrv.port, self.managerSrv.mode,
                           None, self.managerSrv.deal_pkg, None)
        
        return True, None
    
    
    def run(self):
        
        self.fssNet.run()
        

if __name__ == "__main__":
    
    fssSrv = FssSrv()
    bRet = fssSrv.init()
    if bRet:
        fssSrv.run()
    
    
