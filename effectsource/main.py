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
from framework.UtilsHelper import LoggerUtils





sys.dont_write_bytecode = True

curPath = os.getcwd()

# projectPath = os.path.abspath(os.path.join(os.path.dirname(curPath), os.pardir))

allPngNameArray = []

def isInArrry(_str1,array):
	for val in array:
		if(val == _str1):
			return True
	
	return False

def exportJson(filePath):
	#导出所有的json
	exportJsonPath = os.path.join(curPath,"导出")
	def callback(filepath):
		FileUtils.copyFile(filepath,exportJsonPath)
		pass

	FileUtils.diguiDirWithTail(filepath,callback,".json")

def exportImages(filePath):
	#导出所有图片
	imageExportPath = os.path.join(curPath,"导出/images")

	# FileUtils.diguiDirWithTail(filepath,callback,".json")
	imagesPath = os.path.join(filepath,"images")
	if os.path.isdir(imagesPath):
		#导出所有的json
		def callback(filepath):
			fileBaseName = os.path.basename(filepath)
			if isInArrry(fileBaseName,allPngNameArray):
				LoggerUtils.error("重名图片:"+fileBaseName)
			allPngNameArray.append(fileBaseName)
			FileUtils.copyFile(filepath,imageExportPath)
			pass

		FileUtils.diguiDirWithTail(imagesPath,callback,".png")
	else:
		LoggerUtils.error("找不到文件夹"+imagesPath)

	pass


def export(filePath):
	exportJson(filePath)
	exportImages(filePath)
	LoggerUtils.sInfo("导出完成")


#arg[1]:渠道名:proj.ios_mac_appstore
if __name__ == "__main__":
	
	configPath = os.path.join(curPath,"export.json")
	config = FileUtils.getJsonFileData(configPath)
	notExportArray = config["notExport"]


	#清理导出下面的文件
	filelist1 = os.path.join(curPath,"导出")
	filelist2 = os.path.join(curPath,"导出/images")
	FileUtils.tryRmDir(filelist1)
	FileUtils.makedirs(filelist2)
	FileUtils.makedirs(filelist2)

	#导出美术资源
	filelist = os.listdir(os.path.join(curPath,"源文件"))



	#第一层文件夹"源文件"
	for filename in filelist:
		filepath = os.path.join(curPath,"源文件", filename)
		if os.path.isdir(filepath):
			if not isInArrry(filename,notExportArray):
				export(filepath)
			else:
				LoggerUtils.sInfo("忽略导出文件夹:"+filename)
			

	inputName = input("请输入你想输入的plist名字:")
	print("inputName = "+inputName)
	#复制tps到导出里面
	os.chdir(os.path.join(curPath,"导出"))
	FileUtils.copyFile(os.path.join(curPath,"images.tps"),os.path.join(curPath,"导出"))
	
	command = "TexturePacker.exe images.tps --data %s.plist --sheet %s.png"%(inputName,inputName) #--data  1.plist  --sheet 1.png
	os.system(command)

	FileUtils.removeFile(os.path.join(curPath,"导出/images.tps"))




	



























