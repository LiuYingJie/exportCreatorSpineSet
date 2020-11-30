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

reload(sys)

sys.setdefaultencoding('utf8')

sys.dont_write_bytecode = True






def dict2JsonStr(dict):
	return json.dump(dict)










