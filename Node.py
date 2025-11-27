# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 21:34:10 2025

@author: samue
"""

class Node:
    
    def __init__(self, coord = None, f_val=0, g_val=0, h_val=0, parent=None):
        self.coord = coord
        self.f_val = f_val
        self.g_val = g_val
        self.h_val = h_val
        self.parent = parent
        
        
    
    def __eq__(self, other):
       if not isinstance(other, Node):
            return False
       return self.coord == other.coord


    
    def __hash__(self):
        return hash(self.coord)
        
    
    def __lt__(self, other):
        return self.f_val < other.f_val

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        