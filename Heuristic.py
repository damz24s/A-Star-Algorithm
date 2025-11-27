# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 20:22:10 2025

@author: samue
"""

import math as m

class Heuristic:
        
    
    def octile(self, curr_x, curr_y, goal_x, goal_y):
        dx = abs(goal_x - curr_x)
        dy = abs(goal_y - curr_y)
        h = max(dx, dy) + (m.sqrt(2) - 1) * min(dx, dy)
        return h
        
    
    def manhattan(self, curr_x, curr_y, goal_x, goal_y):
        dx = abs(goal_x - curr_x)
        dy = abs(goal_y - curr_y)
        d = dx + dy
        return d
    
    def euclidian(self, curr_x, curr_y, goal_x, goal_y):
        pass