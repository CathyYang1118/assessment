# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:15:37 2019

@author: Think
"""
import numpy as np

Hours = [5,10,10]
Pro = np.array([[10,20,9],
               [11,16,11],
               [10,24,13],
               [14,20,17]])
Total = ['','','']

for num in range(0,3):
    Total[num] = 0
    
for num in range(0,3):
    for day in range(0,4):
        Total[num] += int(Pro[day,num])
        
print(Total)

for num in range(0,3):
    #average = int(Total)/(4*int(Hours[num])
    a = int(Total[num])
    b = 4*int(Hours[num])
    if a/b < 2:
        print('bad',num)