# -*- coding: utf-8 -*-

'''
共用函数帮助类
'''

import os
import shutil
import json
import sys
import codecs
import subprocess
import hashlib
import zipfile
import io


sys.dont_write_bytecode = True

CUR_PATH = os.path.dirname(os.path.realpath(__file__))


#srcFileDir:文件路径
#tarDir:目标目录
def copy(srcDir,tarDir):
	shutil.copytree(srcDir,tarDir)


#srcFileDir:文件路径
#tarDir:目标目录
def copyFile(srcFile,tarDir):
	shutil.copy(srcFile,tarDir)


# 功能：移动文件或者文件夹
# 格式：shutil.move(来源地址,目标地址)
# 返回值：目标地址
#srcDir:来源地址
#tarDir:目标地址
def move(srcDir,tarDir):
	shutil.move(srcDir,tarDir)




# 功能：移除整个目录，无论是否空
# 格式：shutil.rmtree(目录路径)
# 返回值：无
def rmtree(tarDir):
	if(os.path.exists(tarDir)):
		shutil.rmtree(tarDir)


def isDir(path):
	if os.path.isdir(path):
		return True

def rmDir(tarDir):
	rmtree(tarDir)

def tryRmDir(tarDir):
	if isDir(tarDir):
		rmtree(tarDir)

def tyrRmDir(tarDir):
	tryRmDir(tarDir)


#删除文件
def removeFile(file):
	if(os.path.exists(file)):
		os.remove(file)


def isFileExist(filePath):
	return os.path.exists(filePath)




def printMyName():
	print("fileUtils")



# 拷贝并覆盖
def megre(src, dest):
	if os.path.isdir(src):
		if not os.path.isdir(dest):
			os.makedirs(dest)

		files = os.listdir(src)

		for f in files:
			megre(os.path.join(src, f), os.path.join(dest, f))
	else:
		shutil.copyfile(src, dest)


# 递归文件夹指定后缀的文件
def diguiDirWithTail(path,callback,tailStr):
	filelist = os.listdir(path)

	for filename in filelist:
		filepath = os.path.join(path, filename)
		# print("diguiDir---->" + filepath)
		if os.path.isdir(filepath):
			# print("dir -----> " + filepath)
			diguiDirWithTail(filepath,callback,tailStr)
		else:
			# print("not dir -------->" + filepath)
			if filepath.endswith(tailStr):
				callback(filepath)



#递归
def diguiDir(path,callback):
	filelist = os.listdir(path)

	for filename in filelist:
		filepath = os.path.join(path, filename)
		if os.path.isdir(filepath):
			diguiDir(filepath,callback)
		else:
			callback(filepath)




# 复制源文件夹到目标文件夹
def copyDir(src, dist):
	if os.path.isdir(dist):
		shutil.rmtree(dist)

	shutil.copytree(src, dist)


# 获得json文件的数据
def getJsonFileData(filePath):
	file = io.open(filePath, 'r',encoding='UTF-8')
	if file:
		jsonStr = file.read()
		jsonStruct = json.loads(jsonStr)
		file.close()
		return jsonStruct

# 获得json文件的数据
def readJsonFileData(filePath):
	return getJsonFileData(filePath)

# 获得json文件的数据
def writeJsonToFile(filePath,data):
	print("文件路径:"+filePath)
	file = open(filePath, "w+b")
	file.write(json.dumps(data,indent=4))
	file.close()


# 获得json文件的数据
def writeToFile(filePath,data):
	print("文件路径:"+filePath)
	file = open(filePath, "w+b")
	file.write(data)
	file.close()

# 获得json文件的数据
def readFileData(filePath):
	file = open(filePath, 'r')
	if file:
		_str = file.read()
		file.close()
		return _str




#fileAbsPath:字符串
#ignorFileArray:字符串数组
#功能:判断str是否在strArray里面的某一个字符串之内,不一定全等,
#例子:str == "abcd" strArray = ["abc"] return true
def isIgnorFile(fileAbsPath,ignorFileArray):
	for i in range(len(ignorFileArray)):
		curIgnorFileName = ignorFileArray[i-1]
		# print("\t忽略名字:" + curIgnorFileName)
		# print("\t文件名字:" + fileAbsPath)
		if fileAbsPath.find(curIgnorFileName) >= 0:
			return True
	return False


#加入小游戏版本文件
def addGameVersionFile(dirPath):

	pass

#编译lua
def compileLuaFile(compileScriptsPhpPath,osName,srcPath,outPath,EK_VALUE,ES_VALUE):
	# ios为64位加密，Android为32位加密，不考虑iphone5c以及以下的iphone手机
	bit = '32'
	if osName == 'ios':
		bit = '64'

	callPhp = 'php ' + compileScriptsPhpPath + ' -b ' + bit + ' -i ' + srcPath + ' -o ' + outPath + ' -m files -e xxtea_chunk -ek ' + EK_VALUE + ' -es ' + ES_VALUE
	print(callPhp)
	proc = subprocess.Popen(callPhp, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	response = proc.stdout.read()
	print(response)
	pass


#加密资源
def encryptFile(scriptsPhpPath,srcPath,outPath,EK_VALUE,ES_VALUE):
	callPhp = 'php ' + scriptsPhpPath + ' -i ' + srcPath + ' -o ' + outPath + ' -m files -ek ' + EK_VALUE + ' -es ' + ES_VALUE
	print(callPhp)
	proc = subprocess.Popen(callPhp, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	response = proc.stdout.read()
	print(response)
	pass

#压缩图片
def compressPng(filePath,outPath):
	cmd = "pngquant --output %s --ext .png %s"%(outPath,filePath)
	print(cmd)
	os.popen(cmd)
	pass

#压缩图片 直接覆盖写入
def compressPngOverWrite(filePath):
	cmd = "pngquant --force --ext .png %s"%(filePath)
	print(cmd)
	os.popen(cmd)
	pass


#递归创建文件夹
def makedirs(dirPath):
	if not os.path.exists(dirPath): 
		os.makedirs(dirPath)


def md5(filePath):
	data = readFileData(filePath)
	return hashlib.md5(data).hexdigest()



# files = []
# testPath = "/Users/mac/project/gamePlatformClient/SiRuiClientGit_ddz_xiuxian/tools/hot_update/Source/1.1.40/LastCodeANDROID/src"
# zipPath = "/Users/mac/project/gamePlatformClient/SiRuiClientGit_ddz_xiuxian/tools/hot_update/Source/src.zip"
# def callback(fileName):
# 	files.append(fileName)
# 	pass
# FileUtils.diguiDir(testPath,callback)
# FileUtils.zipFiles(files,zipPath,"/Users/mac/project/gamePlatformClient/SiRuiClientGit_ddz_xiuxian/tools/hot_update/Source/1.1.40/LastCodeANDROID/")

#subPath:删减的路径,剩下的就是相对路径
def zipFiles( files, zip_name ,subPath):
	subLen = len(subPath)
	zip = zipfile.ZipFile( zip_name, 'w', zipfile.ZIP_DEFLATED )
	for file in files:
		print ('compressing', file)
		zip.write( file , file[subLen:])
		# zip.write( file)
	zip.close()
	print ('compressing finished')


#获得文件大小
def getFileSize(filePath):
	fsize = os.path.getsize(filePath)
	return fsize