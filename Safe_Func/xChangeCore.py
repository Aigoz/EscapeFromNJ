'''
Created on 2015-12-2

@author: y00272684
'''
import os
import re

RE_MEM_ZERO_IN  = 'VOS_Mem_Zero\((.*),(.*)\);'
RE_MEM_ZERO_OUT = 'VOS_Mem_Zero_S(\\1,\\2,\\2);'

RE_MEM_SET_IN   = 'VOS_Mem_Set\((.*),(.*),(.*)\);'
RE_MEM_SET_OUT  = 'VOS_Mem_Set_Safe(\\1,\\3,\\2,\\3);'

XCHANGETYPE_MEM_ZERO    = 1
XCHANGETYPE_MEM_SET     = 2

def xChange_Mem_Zero(tar_File, out_File, xChangeTyep = 1):
    if not os.path.isfile(tar_File):
        print("Error: Scan error input file: " + tar_File)
        return False
    
    if XCHANGETYPE_MEM_ZERO == xChangeTyep:
        re_in = RE_MEM_ZERO_IN
        re_out = RE_MEM_ZERO_OUT
    elif XCHANGETYPE_MEM_SET == xChangeTyep:
        re_in = RE_MEM_SET_IN
        re_out = RE_MEM_SET_OUT
    else:
        return False
    
#    if not os.path.isfile(out_File):
#        print("Error: Scan error output file: " + out_File)
#        return False
    
    print("Scan File: " + tar_File + "..........")
    f_tar = open(tar_File, "r")
    f_out = open(out_File, "w")
    
    f_tar_str = f_tar.read()
    print("xChanging...............")
    f_out_str = re.sub(re_in, re_out, f_tar_str)
    
    f_out.write(f_out_str)
    print("Scan File Done, xChange sucessed.\r\n")
    
    f_tar.close()
    f_out.close()

    return True