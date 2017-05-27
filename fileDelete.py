#coding=utf-8

import os
import platform

# 删除文件

def deleteFileWithPath(path):
    sysstr = platform.system()
    print ("当前系统是： " + sysstr)
#对操作系统进行判断

    if (sysstr == "Windows"):
        os.remove(path)
    else:
        strig = 'rm -rf '+path    
        os.system(strig)

# 删除指定文件夹下带特殊后缀的文件

'''

path    文件夹路径，比如：“C:\\test”
suffix  后缀名,如.doc .mp3 .exe
eg:     deleteFileInPathAndSuffix("C:\\test", ".txt")   
'''
def deleteFileInPathAndSuffix(path,suffix):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            nameArr = os.path.splitext(filename)
            pycFile = nameArr[1]
            if pycFile == suffix:
                targetPath = os.path.join(dirpath, filename)
                # print targetPath

                # 删除文件

                deleteFileWithPath(targetPath)
