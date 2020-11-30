#-*-coding:utf-8-*-




import os
import shutil
import sys
import time
import math
import json
import zipfile
import types 
from tkinter import messagebox

# from FrameWork import Utils



# logger = Utils.LoggerUtils
# FileUtils = Utils.FileUtils
# StringUtils = Utils.StringUtils
# ArrayUtils = Utils.ArrayUtils


# from PIL import Image

from framework.UtilsHelper import FileUtils

# import framework.UtilsHelper.FileUtils 
# import framework.UtilsHelper.LoggerUtils 
# import framework.UtilsHelper.StringUtils 




sys.dont_write_bytecode = True

curPath = os.getcwd()

# projectPath = os.path.abspath(os.path.join(os.path.dirname(curPath), os.pardir))



def isInArrry(_str,array):
	for val in array:
		if(val == _str):
			return True
	
	return False



def export(filePath):
	#导出所有的json
	exportJsonPath = os.path.join(curPath,"导出")
	def callback(filepath):
		print("filepath -->"+exportJsonPath)
		FileUtils.copyFile(filepath,exportJsonPath)
		pass

	FileUtils.diguiDirWithTail(filepath,callback,".json")


	#导出所有图片
	pass


#arg[1]:渠道名:proj.ios_mac_appstore
if __name__ == "__main__":
	
	print("curPath = "+curPath)
	configPath = os.path.join(curPath,"export.json")
	config = FileUtils.getJsonFileData(configPath)
	notExportArray = config["notExport"]


	#清理导出下面的文件
	filelist1 = os.path.join(curPath,"导出/images")
	FileUtils.tryRmDir(filelist1)
	FileUtils.makedirs(filelist1)

	#导出美术资源
	filelist = os.listdir(os.path.join(curPath,"源文件"))
	print("filelist =",filelist)



	#第一层文件夹"源文件"
	for filename in filelist:
		filepath = os.path.join(curPath,"源文件", filename)
		print("filepath = "+filepath)
		if os.path.isdir(filepath):
			if not isInArrry(filename,notExportArray):
				export(filepath)
			else:
				print("忽略导出文件夹:"+filename)
			







	



























