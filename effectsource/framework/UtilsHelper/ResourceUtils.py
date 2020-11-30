# -*- coding: utf-8 -*-

'''
资源处理类，主要是对图片进行pngquant压缩，对csb,png,plist,ccz,jpg格式文件进行加密
'''

import os
import shutil
import subprocess
import sys

import FileUtils

sys.dont_write_bytecode = True

# from helper import helper


EK_VALUE = 'SiGZ2018RuI'	#加密key
ES_VALUE = 'sirui'			#加密sign




# 资源压缩
def pngquant(compressPath):
	file_path = []

	# 获取指定后缀的文件
	def getNameList(dir, wildcard, recursion):
		exts = wildcard.split(" ")
		files = os.listdir(dir)
		for name in files:
			fullname = os.path.join(dir, name)
			if os.path.isdir(fullname) & recursion:
				getNameList(fullname, wildcard, recursion)
			else:
				for ext in exts:
					if (name.endswith(ext)):
						file_path.append(fullname)
						break

	def startCompilePng():
		file_name_list = file_path
		for file_name in file_name_list:
			# 对png图片进行压缩
			a = file_name.find(".png")
			if a<> -1:
				# 调用pngquant对图片进行压缩
				cmd = "pngquant --force --ext .png %s"%(file_name)
				os.popen(cmd)

	getNameList(compressPath, ".png .jpg", 1)
	startCompilePng()

#projectPath:工程路径
#pngPath :图片路径
#outPath:加密图片输出路径
def encodePng(projectPath,pngPath,outPath):
	# 开始加密
	phpPath = os.path.join(projectPath,'tools/quick/lib/pack_files.php')
	print("phpPath = " + phpPath)
	callPhp = 'php ' + phpPath + ' -i ' + pngPath + ' -o ' + outPath + ' -m files -ek ' + EK_VALUE + ' -es ' + ES_VALUE
	os.system(callPhp)







# #projectPath:工程路径
# #pngPath :图片路径
# #outPath:加密图片输出路径
# def encodePng111(projectPath,pngPath,outPath):
# 	phpPath = os.path.join(projectPath,'tools/quick/lib/pack_files.php')


# 	projectLen = len(projectPath)


# 	def test(filePath):
# 		begin = projectPath.find(os.path.join(filePath,"res"))
# 		if begin >= 0:
# 			print(filePath)
# 			print("begin =  "+str(begin))
# 			head = filePath[begin:projectLen-1]
# 			tail = filePath[projectLen:]
# 			print("tail = " + tail)

# 			absPath = os.path.abspath(filePath)
# 			print("absPath = "+absPath)
# 			#递归创建文件夹
# 			# os.makedirs(absPath)

# 			# callPhp = 'php ' + phpPath + ' -i ' + filePath + ' -o ' + os.path.join(outPath,tail) + ' -m files -ek ' + EK_VALUE + ' -es ' + ES_VALUE
# 			# os.system(callPhp)
# 			# print(filePath)
# 	# 开始加密
# 	# print("phpPath = " + phpPath)
# 	# callPhp = 'php ' + phpPath + ' -i ' + pngPath + ' -o ' + outPath + ' -m files -ek ' + EK_VALUE + ' -es ' + ES_VALUE
# 	# os.system(callPhp)
# 	FileUtils.diguiDirWithTail(pngPath,test,".png")




























