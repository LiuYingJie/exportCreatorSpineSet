# -*- coding: utf-8 -*-

'''
共用函数帮助类
'''

import os
import shutil
import json
import sys
import traceback

sys.dont_write_bytecode = True


# FuncUtils





def error(str):
	print("\n\n\n")
	print("*************** error *****************")
	print("\n")
	print("\t\t"+str)
	print("\n")
	traceback.print_stack()
	print("*************** error *****************")




def warning(str):
	print("\n")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print(str)
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("\n")


def info(str):
	print("\n")
	print("#############################################")
	print("\n")
	print(str)
	print("\n")
	print("#############################################")
	print("\n")




# sinfo:s=simple ,意思是简单打印
def sInfo(str):
	print("#############################################")
	print(str)
	print("#############################################")
















