# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 21:29:11 2025

@author: samue
"""

import heapq
from Node import Node
from Heuristic import Heuristic
from Grids import Grid


class Astar:
    
    def __init__(self, start_node, goal_node, matrix_num, ):
        self. start_node = start_node
        self.goal_node = goal_node
        self.matrix_num = matrix_num



    def isGoal(self, node, matrix):
        
        if matrix[node.coord[0]][node.coord[1]] == 'g':
            print("Goal found!!!")
            return True
        else:
            return False



    def pathReconstruct(self, node): 
        path = []
        coordPath = []
        current = node
        path.append(current)
        
        while current.parent != None:
            current = current.parent
            path.append(current)
        
        for node in path:
            coordPath.append(node.coord)
        coordPath.reverse()
        print("path:", coordPath)
    
    
    
    def isValid(self, node, matrix):
        
        if matrix[node.coord[0]][node.coord[1]] == '#':
            return False
        else:
           return True
        
        
        
    def neighbourGenerator(self, node, matrix):
        directions = {"down" : [(1,0), 1],
                      "bottomright" : [(1,1), 1],
                      "right" : [(0,1), 1],
                      "topright" : [(-1,1), 1],
                      "up" : [(-1,0), 1],
                      "topleft" : [(-1,-1), 1],
                      "left" :[(0,-1), 1],
                      "bottomleft" : [(1,-1), 1],
                      }
        
        for key in directions.keys():
            new_node = Node((node.coord[0] + directions[key][0][0], node.coord[1] + directions[key][0][1]))
        
            try:
                if matrix[new_node.coord[0]][new_node.coord[1]] != None:
                    if matrix[new_node.coord[0]][new_node.coord[1]] == "#":
                        continue
                yield new_node
                    
                    
            except Exception:
                continue
            
            

    def pathFinder(self):
        start = Node(self.start_node)
        goal = Node(self.goal_node)
        grid = Grid()
        matrix = grid.matrices(1)
        open_list = []
        heapq.heapify(open_list)
        closed_list = set()
        heu = Heuristic()
        open_dict = {}
        
        
        curr_node = start
        g = curr_node.g_val
        curr_node.h_val = (heu.octile(curr_node.coord[0], curr_node.coord[1], goal.coord[0], goal.coord[1]))
        h = curr_node.h_val
        curr_node.f_val = g + h
        heapq.heappush(open_list, curr_node)
        open_dict[curr_node] = [curr_node.f_val]
        
        while True:
                
            if len(open_list) == 0:
                print("Goal not found!")
                break
            
            
            else:
                curr_node = heapq.heappop(open_list)
                prev_node = curr_node
                closed_list.append(curr_node)
                self.neighbourGenerator(curr_node, matrix)
                
                # --- down ---
                node_below = Node((curr_node.coord[0] + 1, curr_node.coord[1])) 
                if node_below.coord[0] <= len(matrix) - 1 and self.isValid(node_below, matrix): #checking node below current node
                    if node_below in open_list:
                        parent_g = prev_node.g_val
                        curr_g = parent_g + 1
                        if curr_g < node_below.g_val:
                            f = curr_g + node_below.h_val
                            node_below.g_val = curr_g
                            node_below.f_val = f
                            node_below.parent = prev_node
                            heapq.heappush(open_list, node_below)
                    
                    else:
                        node_below.parent = prev_node
                        if self.isGoal(node_below, matrix):
                            self.pathReconstruct(node_below)
                            break
                        
                        parent_g = prev_node.g_val
                        g = node_below.g_val + parent_g + 1
                        
                        h = heu.octile(node_below.coord[0] , node_below.coord[1], goal.coord[0], goal.coord[1])
                        node_below.f_val = g + h
                        heapq.heappush(open_list, node_below)
            
                
                
                # --- bottom right ---
                node_bottomright = Node((curr_node.coord[0] + 1, curr_node.coord[1] + 1)) 
                if node_bottomright.coord[0] <= len(matrix) - 1 and node_bottomright.coord[1] <= len(matrix[0]) - 1:
                    if self.isValid(node_bottomright, matrix):
                        if node_bottomright in open_list:
                            parent_g = prev_node.g_val
                            curr_g = parent_g + 1.4
                            if curr_g < node_bottomright.g_val:
                                f = curr_g + node_bottomright.h_val
                                node_bottomright.g_val = curr_g
                                node_bottomright.f_val = f
                                node_bottomright.parent = prev_node
                                heapq.heappush(open_list, node_bottomright)
                            
                        else:
                            node_bottomright.parent = prev_node
                            if self.isGoal(node_bottomright, matrix):
                                self.pathReconstruct(closed_list, node_bottomright)
                                break
                            
                            parent_g = prev_node.g_val
                            g = node_bottomright.g_val + parent_g + 1.4
                            
                            h = heu.octile(node_bottomright.coord[0] , node_bottomright.coord[1], goal.coord[0], goal.coord[1])
                            node_bottomright.f_val = g + h
                            heapq.heappush(open_list, node_bottomright)


                                
                # --- right ---
                node_right = Node((curr_node.coord[0], curr_node.coord[1] + 1))
                if node_right.coord[1] <= len(matrix[0]) - 1 and self.isValid(node_right, matrix): #checking node on the right of current node 
                    if node_right in open_list:
                        parent_g = prev_node.g_val
                        curr_g = parent_g + 1
                        if curr_g < node_right.g_val:
                            f = curr_g + node_right.h_val
                            node_right.g_val = curr_g
                            node_right.f_val = f
                            node_right.parent = prev_node
                            heapq.heappush(open_list, node_right)
                        
                    else:
                        node_right.parent = prev_node
                        if self.isGoal(node_right, matrix):
                            self.pathReconstruct(node_right)
                            break
                         
                        parent_g = prev_node.g_val
                        g = node_right.g_val + parent_g + 1
                        
                        h = heu.octile(node_right.coord[0] , node_right.coord[1], goal.coord[0], goal.coord[1])
                        node_right.f_val = g + h
                        heapq.heappush(open_list, node_right)
                
                
                                
                # --- top right ---
                node_topright = Node((curr_node.coord[0] - 1, curr_node.coord[1] + 1))
                if node_topright.coord[1] <= len(matrix[0]) - 1 and node_topright.coord[0] >= 0 and self.isValid(node_topright, matrix):
                    if node_topright in open_list:
                        parent_g = prev_node.g_val
                        curr_g = parent_g + 1.4
                        if curr_g < node_topright.g_val:
                            f = curr_g + node_topright.h_val
                            node_topright.g_val = curr_g
                            node_topright.f_val = f
                            node_topright.parent = prev_node
                            heapq.heappush(open_list, node_topright)
                        
                    else:
                        node_topright.parent = prev_node
                        if self.isGoal(node_topright, matrix):
                            self.pathReconstruct(node_topright)
                            break
                         
                        parent_g = prev_node.g_val
                        g = curr_node.g_val + parent_g + 1.4
                        
                        h = heu.octile(node_topright.coord[0] , node_topright.coord[1], goal.coord[0], goal.coord[1])
                        node_topright.f_val = g + h
                        heapq.heappush(open_list, node_topright)
                
                
                                
                # --- up ---
                node_above = Node((curr_node.coord[0] - 1, curr_node.coord[1]))
                if node_above.coord[0] >= 0 and self.isValid(node_above, matrix): #checking node above current node 
                    if node_above in open_list:
                        parent_g = prev_node.g_val
                        curr_g = parent_g + 1
                        if curr_g < node_above.g_val:
                            f = curr_g + node_above.h_val
                            node_above.g_val = curr_g
                            node_above.f_val = f
                            node_above.parent = prev_node
                            heapq.heappush(open_list, node_above)
                        
                     
                    else:
                        node_above.parent = prev_node
                        if self.isGoal(node_above, matrix):
                            self.pathReconstruct(closed_list, node_above)
                            break
                         
                        parent_g = prev_node.g_val
                        g = node_above.g_val + parent_g + 1
                        
                        h = heu.octile(node_above.coord[0] , node_above.coord[1], goal.coord[0], goal.coord[1])
                        node_above.f_val = g + h
                        heapq.heappush(open_list, node_above)
                            
                            
                                            
                # --- top left ---
                node_topleft = Node((curr_node.coord[0] - 1, curr_node.coord[1] - 1))
                if node_topleft.coord[1] >= 0 and node_topleft.coord[0] >= 0 and self.isValid(node_topleft, matrix):  #checking node on the top left of current node
                    if node_topleft in open_list:
                        parent_g = prev_node.g_val
                        curr_g = parent_g + 1.4
                        if curr_g < node_topleft.g_val:
                            f = curr_g + node_topleft.h_val
                            node_topleft.g_val = curr_g
                            node_topleft.f_val = f
                            node_topleft.parent = prev_node
                            heapq.heappush(open_list, node_topleft)
                        
                     
                    else:
                        node_topleft.parent = prev_node
                        if self.isGoal(node_topleft, matrix):
                            self.pathReconstruct(node_topleft)
                            break
                         
                        parent_g = prev_node.g_val
                        g = node_topleft.g_val + parent_g + 1.4
                        
                        h = heu.octile(node_topleft.coord[0] , node_topleft.coord[1], goal.coord[0], goal.coord[1])
                        node_topleft.f_val = g + h
                        heapq.heappush(open_list, node_topleft)
                
                
                                
                # --- left ---
                node_left = Node((curr_node.coord[0], curr_node.coord[1] - 1))
                if node_left.coord[1] >= 0 and self.isValid(node_left, matrix): #checking node on the left of current node 
                    if node_left in open_list:
                        parent_g = prev_node.g_val
                        curr_g = parent_g + 1
                        if curr_g < node_left.g_val:
                            f = curr_g + node_left.h_val
                            node_left.g_val = curr_g
                            node_left.f_val = f
                            node_left.parent = prev_node
                            heapq.heappush(open_list, node_left)
                        
                     
                    else:
                        node_left.parent = prev_node
                        if self.isGoal(node_left, matrix):
                            self.pathReconstruct(node_left)
                            break
                         
                        parent_g = prev_node.g_val
                        g = node_left.g_val + parent_g + 1
                        
                        h = heu.octile(node_left.coord[0] , node_left.coord[1], goal.coord[0], goal.coord[1])
                        node_left.f_val = g + h
                        heapq.heappush(open_list, node_left)
                
                         
                                
                # --- bottom left ---
                node_bottomleft = Node((curr_node.coord[0] + 1 , curr_node.coord[1] - 1))
                if node_bottomleft.coord[1] >= 0 and node_bottomleft.coord[0] <= len(matrix) - 1 and self.isValid(node_bottomleft, matrix): #checking node on the left of current node 
                    if node_bottomleft in open_list:
                        parent_g = prev_node.g_val
                        curr_g = parent_g + 1.4
                        if curr_g < node_bottomleft.g_val:
                            f = curr_g + node_bottomleft.h_val
                            node_bottomleft.g_val = curr_g
                            node_bottomleft.f_val = f
                            node_bottomleft.parent = prev_node
                            heapq.heappush(open_list, node_bottomleft)
                        
                     
                    else:
                        node_bottomleft.parent = prev_node
                        if self.isGoal(node_bottomleft, matrix):
                            self.pathReconstruct(node_bottomleft)
                            break
                         
                        parent_g = prev_node.g_val
                        g = node_bottomleft.g_val + parent_g + 1.4
                        
                        h = heu.octile(node_bottomleft.coord[0] , node_bottomleft.coord[1], goal.coord[0], goal.coord[1])
                        node_bottomleft.f_val = g + h
                        heapq.heappush(open_list, node_bottomleft)

    



a1 = Astar((3,2), (4,6), 1)

a1.pathFinder()










