# -*- coding: utf-8 -*-

'''
共用函数帮助类
'''

import os
import shutil
import json
import sys

sys.dont_write_bytecode = True


# FuncUtils





def runFunc(tag,func,_dict):

	print("================执行开始 " + tag + " ================")
	ret = func(_dict)
	print("================执行结束 " + tag + " ================")
	return ret




























