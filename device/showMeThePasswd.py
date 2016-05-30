# -*- coding:utf-8 -*-
'''
Created on 2016-5-28

@author: y00272684
'''
import telnetlib, time, sys, os

'''
def do_telnet(Host, Port, username, password, finish):  
    #连接Telnet服务器  
    tn = telnetlib.Telnet(Host, Port, timeout=1)  
    tn.set_debuglevel(3)  
      
    #输入登录用户名  
    tn.read_until("login: ")  
    tn.write(str(username)+'\n')  
      
    # 输入登录密码  
    tn.read_until("Password: ")  
    tn.write(str(password)+'\n')  
        
    # 判断密码错误提示，如果没有这个提示说明登录成功  
    if tn.read_until(finish):  
        print "****** login incorrect!\n"  
    tn.close();  
      
if __name__=='__main__':  
    
    Host = raw_input("IP:")           # Telnet服务器IP  
    Port = raw_input("Port:")        # Telnet服务器端口  
    username = 'root'          # 登录用户名  
    finish = 'incorrect'       # 密码错误提示  
    pw_file = open('.\\pw.txt','r+') #密码文件  
    Index = 0  
    print time.asctime(),":   ****** begin","\n"  
    while True:  
        password = pw_file.readline()  
        Index +=1;  
        print Index,time.asctime(),":   ****** try","",username,":",password,""  
        if len(password) == 0:  
            break;  
        do_telnet(Host, Port, username, password, finish)  
    pw_file.close();  
    
    raw_input('End')
'''

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
def openUserFile(filePath):
    '''
    Need close fileObj
    '''
    if os.path.isfile(filePath):
        fileObj = open(filePath, 'r+')
    else:
        fileObj = open(filePath, 'w')
        fileObj.close()
        fileObj = open(filePath, 'r+')
    return fileObj

def get_UserName():
    fileHanle = openUserFile('.\\usrname.txt')
    
if __name__ == '__main__':

    #oscommand = 'dir'
    #osResult = os.popen(oscommand).readlines()
    
    #print osResult
    userHost = raw_input('IP: ')
    userPort = raw_input('Port: ')
    
    try: 
        tn = telnetlib.Telnet(userHost, userPort, timeout = 0.5)
        tnResult = tn.read_until('Username:', 1)
    except BaseException as e :
        print e
    finally:
        if tn:
            tn.close()
            
    
    try:
        usrNameFileHandle = openUserFile('.\\usrname.txt')
    except BaseException as e:
        print 'Read username file error. '
        
    try:
        usrPasswdFileHandle = openUserFile('.\\password.txt')
    except BaseException as e:
        print 'Read password file error. '

    tnStr = ''
    tn1 = telnetlib.Telnet('fafa.124.300', port = 23, timeout = 0.5)
    while True:
        try:
            tnStr += tn1.read_some()
        except BaseException as e:
            print tnStr
            print e
            break
    tn1.close()
    '''
    try:
        tn = telnetlib.Telnet('10.136.6.204', port = 23, timeout = 2)
        if None == tn :
            print 'tn = Null'
        
    except BaseException as e:
        #print('BaseException: ' + e)
        print 'BaseException: ', e
    else:
        tnResult = tn.read_until('Password:', 5)
        print (tnResult)
        #tnResult = tn.write('huawei123\n')
        print tn.read_until('>', 5)
        tn.close()
    finally:
        #print(tn)
        #tn.close()
        pass
    '''