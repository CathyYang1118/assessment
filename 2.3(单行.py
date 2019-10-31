# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:46:49 2019

@author: Think
"""

def Read (txtname):
    PCode = []
    PDes = []
    PRet = []
    File = open(txtname,'r')
    num = 0
    for i in File.readlines():
        SpaceCount = 0
        code = ''
        des = ''
        ret = ''
        for j in i[:-1]:
            
            if SpaceCount == 0:
                code += j
                
            elif SpaceCount == 1:
                des += j
                
            elif SpaceCount == 2:
                ret += j
            
            if j == ' ':
                SpaceCount += 1

        PCode.append(code)
        PDes.append(des)    
        PRet.append(ret)
        
    print('Code:',PCode,'Des',PDes,'Ret',PRet)

Read('2.2.txt')