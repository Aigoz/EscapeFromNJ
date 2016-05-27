# -*- coding:utf-8 -*-
'''
Created on 2016-2-28

@author: y00272684
'''

import telnetlib
import os
import re

class Device(object):
    '''
    classdocs
    '''
    def __init__(self, ipAddress = '', username = '', password = '', dTag = 'iGeek'):
        self.ipAddr     = ipAddress
        self.usrName    = username
        self.passwd     = password
        self.__consoleIPAddr = ''
        self.__consolePasswd = ''
        self.__telnet = None    #telnet��¼ʱʹ��
        self.deviceType = ''
        self.eVersion = ''
        self.deviceTag = dTag
 
    '''
    Property: Ip Address, ipAddr, string
    '''       
    @property
    def ipAddr(self):
        return self._ipAddr
    
    @ipAddr.setter
    def ipAddr(self, valueIpAddrStr):
        if not isinstance(valueIpAddrStr, (str, )):
            raise ValueError('IP Address is not a string')
        '''
        ip address 合法值判断，推荐使用 正则
        '''
        self._ipAddr = valueIpAddrStr
        
    '''
    Property: User Name, usrName, string 
    '''
    @property
    def usrName(self):
        return self._usrName
    
    @usrName.setter
    def usrName(self, valueUserNameStr):
        if not isinstance(valueUserNameStr, (str, )):
            raise ValueError('User name is not a string')
        self._usrName = valueUserNameStr
        
    '''
    Property: Password, passwd, string 
    '''
    @property
    def passwd(self):
        return self._passwd
    
    @passwd.setter
    def passwd(self, valuePasswordStr):
        if not isinstance(valuePasswordStr, (str, )):
            raise ValueError('Password is not a string')
        self._passwd = valuePasswordStr



if __name__ == '__main__':
    esapDevice = Device('103','222') 
    #print(esapDevice.__dict__)
    
    oscommand = 'dir'
    osResult = os.popen(oscommand).readlines()
    
    #printf(osResult)
    try:
        tn = telnetlib.Telnet('10.136.6.204')
    except BaseException as e:
        print('BaseException: ' + e)
    else:
        '''
        tnResult = tn.read_until('Password:', 5)
        print (tnResult)
        #tnResult = tn.write('huawei123\n')
        print tn.read_until('>', 10)
        '''
    finally:
        #print(tn)
        tn.close()
    

    
    
    