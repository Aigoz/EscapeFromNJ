# -*- coding: utf-8 -*-
'''
Created on 2016��3��21��

@author: Aigoz
'''
from functools import reduce

if __name__ == "__main__":
    
    # 练习1
    def normalize(name):
        return name[0].upper() + name[:1].lower()
            
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)
    
    #练习2
    def prod(L):
        return reduce(lambda x,y: x * y, L)
    
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    
    #练习3
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    def str2floatGt0(s):
        return reduce(lambda x,y: x*10 + y, map(char2num,s))
        
    def str2floatLt0(s):
        """
        z利用了list翻转 然后依次 0.1*x 累加就行   翻转功能 [::-1]
        """
        return (reduce(lambda x,y: 0.1*x + y, map(char2num, s[::-1]))/10)
      
    def str2float(s):
        pointIndex = s.index('.')
        return str2floatGt0(s[:pointIndex]) + str2floatLt0(s[(pointIndex+1):])
    
    print('str2float(\'123.456\') =', str2float('123.456'))