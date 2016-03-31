# -*- coding: utf-8 -*-
'''
Created on 2016-3-31

@author: Aigoz
'''

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):

    return t[0].lower()

L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_score)
print(L2)