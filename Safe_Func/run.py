# -*- coding:utf-8 -*-
'''
Created on 2015-12-1

@author: y00272684
'''
import os
import sys
import xChangeCore

inputPath = './old'
OUTPUT_PATH = './mem_zero'

print(xChangeCore.XCHANGETYPE_MEM_ZERO)
    

def xChange_ByPath(inPath_local = inputPath, outPath_local = OUTPUT_PATH, type = xChangeCore.XCHANGETYPE_MEM_ZERO):
    
    for tempX in os.listdir(inPath_local):
        tempDir_or_File = os.path.join(inPath_local, tempX)
        
        if os.path.isdir(tempDir_or_File):
            tempOutDir = os.path.join(outPath_local, tempX)
            os.mkdir(tempOutDir)
            xChange_ByPath(tempDir_or_File, tempOutDir, type)
        
        elif os.path.isfile(tempDir_or_File):
            tempOutFile = os.path.join(outPath_local, tempX)
            xChangeCore.xChange_Mem_Zero(tempDir_or_File, tempOutFile, type)
        else:
            pass

def globalIsValid():
    global inputPath
    global OUTPUT_PATH
    if not os.path.isdir(inputPath):
        print("Input Path is not Valid")
        return False
    elif not os.path.isdir(OUTPUT_PATH):
        os.mkdir(OUTPUT_PATH)
        print("Create output dir: %s" % os.path.abspath(OUTPUT_PATH))
    else:
        pass
    return True

def printEnd():
    print('XChange End.')
    print("********************iGeek provides********************")
    print('*               To Be Continued.......               *')
    print("********************iGeek provides********************")

def removeDir(dirPath):
    if not os.path.isdir(dirPath):
        return
    files = os.listdir(dirPath)
    try:
        for file in files:
            filePath = os.path.join(dirPath, file)
            if os.path.isfile(filePath):
                os.remove(filePath)
            elif os.path.isdir(filePath):
                removeDir(filePath)
        os.rmdir(dirPath)
    except Exception, e:
        print e

#Main Run
if __name__ == '__main__':
    args = sys.argv
    print('Input Args: %s' % str(args))
    if len(args) > 2:
        print('Input Args must be less than 1')
        exit()
    elif len(args) == 2:
        inputPath = args[1]
        print("Target Input Path: " + os.path.abspath(inputPath) + "\r\n")
    else:
        print("Default Input Path: " + os.path.abspath(inputPath) + "\r\n")

    if not globalIsValid():
        exit()
      
#VOS_Mem_Zero 修改  
    print('XChange VOS_Mem_Zero Start......\r\n')
    
    removeDir(OUTPUT_PATH)
    os.mkdir(OUTPUT_PATH)
    
    xChange_ByPath(inputPath, OUTPUT_PATH, xChangeCore.XCHANGETYPE_MEM_ZERO)

#VOS_Mem_Set 修改     
    inputPath   = OUTPUT_PATH
    delPath     = OUTPUT_PATH
    OUTPUT_PATH = './result'
    
    if not globalIsValid():
        exit()
  
    print('XChange VOS_Mem_Set Start......\r\n')
    
    removeDir(OUTPUT_PATH)
    os.mkdir(OUTPUT_PATH)
    
    xChange_ByPath(inputPath, OUTPUT_PATH, xChangeCore.XCHANGETYPE_MEM_SET)
    
#删除中间文件
    removeDir(delPath)
    print("Output Dir: " +  os.path.abspath(inputPath))
    printEnd()
    