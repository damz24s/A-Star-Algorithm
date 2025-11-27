# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 21:36:40 2025

@author: samue
"""

class Grid:
    
    def matrices(self, gridNum):
        if gridNum == 1:
            matrix1 = [[0  , 0 ,  0 ,  0,  0 , 0 ,0, 0],
                      [0  , 0 ,  0 ,  0,  0 , 0 ,0, 0],
                      [0  , 0 ,  0 ,  0, '#', 0, 0, 0],
                      [0  , 0 , 's',  0, '#', 0, 0, 0],
                      [0  ,'#', '#', '#','#', 0,'g',0],
                      [0  , 0 , 0 ,  0,   0,  0, 0, 0]]
            return matrix1
        
        
        