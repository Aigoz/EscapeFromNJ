# -*- coding:utf-8 -*-
'''
Created on 2016-5-28

@author: y00272684
'''
import telnetlib, time, sys, os
from _socket import gaierror, timeout

'''
def xChange_ByPath(inPath_local = inputPath, outPath_local = OUTPUT_PATH, type = xChangeCore.XCHANGETYPE_MEM_ZERO):
    
    for tempX in os.listdir(inPath_local):
        tempDir_or_File = os.path.join(inPath_local, tempX)
        
'''

curTimeout = 0.5

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

def get_FileHandle(filePath):
    try:
        fileHanle = openUserFile(filePath)
        return fileHanle
    except BaseException as e:
        print e
        return None
    
def do_checkPassword(tn):
    global curTimeout
    
    if tn:
        if isinstance(tn, telnetlib.Telnet):
            tnTuple_temp = tn.expect(['Authentication failed', '>'], curTimeout)
            if tnTuple_temp[0] == 0:
                print 'Authentication failed.' 
                return False
            elif tnTuple_temp[0] == 1:
                print 'Authentication successed'
                return True
            else:
                print 'Authentication wrong......'
                print tnTuple_temp
                return False
            '''
            tStr = tn.read_until('Authentication failed', curTimeout)
            if len(tStr):
                print tStr
                print 'Debug: -------Authentication failed'
                return False
            
            tStr = tn.read_until('>', curTimeout)
            if len(tStr):
                print tStr
                print 'Debug: -------Authentication Success'
                return True 
            '''    
        else:
            raise ValueError('tn is not instance of Telnet.')
    else:
        raise ValueError('tn is none!')

def show_result(result):
    print '\n\n\nResult:'
    print result
    
if __name__ == '__main__':

    isPasswd = True
    isUsername = True
    isCorect = False
    isUsernameUpdate = True
    isPasswordRefresh = False
    
    userHost = raw_input('IP: ')
    userPort = raw_input('Port: ')
    '''
    userHost = '10.136.124.131'
    userPort = '23'
    '''
    username = ''
    password = ''
    
    try: 
        fileUsername = get_FileHandle(r'.\usrname.txt')
        filePassword = get_FileHandle(r'.\password.txt')
        tn = None
        
        while True:
            tn = telnetlib.Telnet(userHost, userPort, timeout = curTimeout)
            
            tnTuple = tn.expect(['Username:', 'Password:', '<'], curTimeout)
            print 'Debug: tuple1 ', tnTuple
            if tnTuple[0] == -1:
                raise ValueError('Expect Keyword Error. Step login one....')
            elif tnTuple[0] == 0:
                if isUsernameUpdate:
                    username = fileUsername.readline().strip()
                    print 'Debug: get username: ', username
                    isUsernameUpdate = False
                    isPasswordRefresh = True
                
                if len(username):
                    tn.write(str(username) + '\n')
                else:
                    tn.close()
                    print 'There is no username to try.'
                    break
                
                tnTuple_1 = tn.expect(['Password:'], curTimeout)
                print 'Debug: tuple2 ', tnTuple_1
                if tnTuple_1[0] == -1:
                    raise ValueError('Expect Keyword Error. Step login two....')
            
            if tnTuple[0] == 2:
                tn.close()
                show_result('''    No password''')
                break
            
            if tnTuple[0] == 1 or tnTuple_1[0] == 0:
                if isPasswordRefresh:
                    filePassword.close()
                    filePassword = get_FileHandle(r'.\password.txt')
                    isPasswordRefresh = False
                password = filePassword.readline().strip()
                print 'Debug: get password: ', password
                
                if len(password):
                    tn.write(str(password) + '\n')
                    print 'do check password'
                    if do_checkPassword(tn):
                        isCorect = True
                else:
                    isUsernameUpdate = True
                    
            

            tn.close()

            if isCorect:
                show_result('''
                Username: %s
                Passwod: %s
                ''' % (username, password)
                )
                break
                
    except gaierror as e:
        print 'Error: ', e
        print 'Please check your IP address or port.'
        
    except timeout as e:
        print 'Error: ', e
        print 'da wang you TMD feng bao le???'
        
    except BaseException as e :
        print (' ',e)
        
    finally:
        if tn:
            tn.close()
        
        if fileUsername:
            fileUsername.close()
            
        if filePassword:
            filePassword.close()
            
        raw_input('Press any key to close this window.')