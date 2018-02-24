#!/usr/bin/python3
# coding=utf-8

"""
检索指定路径下后缀是 py 的所有文件
来源: <http://www.runoob.com/python3/python3-file-methods.html> by "领悟悟悟"
源代码略有修改, 生成带绝对路径的列表, 可用于特定后缀名文件的移动, 生成目录等
"""

import os
import os.path


ls = []

def getAppointFile(path,ls):
    path = os.path.abspath(path)
    fileList = os.listdir(path)
    
    try:
        for tmp in fileList:
            pathTmp = os.path.join(path,tmp)
            if True==os.path.isdir(pathTmp):
                getAppointFile(pathTmp,ls)
            elif pathTmp[pathTmp.rfind('.')+1:].upper()=='PY':
                ls.append(pathTmp)
    except PermissionError:
        pass

def main():

    while True:
        path = input('请输入路径: ').strip()
        if os.path.isdir(path) == True:
            break

    getAppointFile(path,ls)
    print(ls)
    print('\nlength of python file: %d'%(len(ls)))

main()
