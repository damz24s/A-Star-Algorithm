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
    
    def __init__(self, start_node, goal_node):
        self. start_node = start_node
        self.goal_node = goal_node



    def isGoal(self, node):
        
        if node.h_val == 0:
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
    

        
        
        
    def neighbourGenerator(self, node, matrix, closed_list):
        directions = {"down" : [(1,0), 1],
                      "bottomright" : [(1,1), 1.4],
                      "right" : [(0,1), 1],
                      "topright" : [(-1,1), 1.4],
                      "up" : [(-1,0), 1],
                      "topleft" : [(-1,-1), 1.4],
                      "left" :[(0,-1), 1],
                      "bottomleft" : [(1,-1), 1.4],
                      }
        check = False
        for key in directions.keys():
            new_node = Node((node.coord[0] + directions[key][0][0], node.coord[1] + directions[key][0][1]))
            g_val = directions[key][1]
            try:
                if matrix[new_node.coord[0]][new_node.coord[1]] != None:
                    if matrix[new_node.coord[0]][new_node.coord[1]] == "#":
                        continue
                    
                    elif new_node in closed_list:
                        continue
                    
                yield (new_node, g_val)
                check = True    
                
            except Exception:
                continue
            
        if check == False:
            yield None
            
            

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
        curr_node.h_val = (heu.octile(curr_node.coord[0], curr_node.coord[1], goal.coord[0], goal.coord[1]))
        curr_node.f_val = curr_node.g_val + curr_node.h_val
        heapq.heappush(open_list, curr_node)
        open_dict[curr_node.coord] = [curr_node.f_val]
        
        while True:
                
            if len(open_list) == 0:
                print("Goal not found!")
                break
            
            
            else:
                curr_node = heapq.heappop(open_list)
                prev_node = curr_node
                closed_list.add(curr_node)
                generator = self.neighbourGenerator(curr_node, matrix, closed_list)
                
                for node in generator:
                    if node == None:
                        print("Goal Not Found!")
                        break
        
                    
                    else: 
                        if node[0].coord in open_dict.keys():
                            curr_g = prev_node.g_val + node[1]
                            if curr_g < node[0].g_val:
                                node[0].g_val = curr_g
                                node[0].f_val = node[0].g_val + node[0].h_val
                                node[0].parent = prev_node
                                heapq.heappush(open_list, node[0])
                                open_dict[node[0]] = [node[0].f_val]
                        
                        else:
                            node[0].parent = prev_node
                            
                            node[0].g_val = prev_node.g_val + node[1]
                            node[0].h_val = heu.octile(node[0].coord[0] , node[0].coord[1], goal.coord[0], goal.coord[1])
                            node[0].f_val = node[0].g_val + node[0].h_val
                            if self.isGoal(node[0]):
                                self.pathReconstruct(node[0])
                                break
                            heapq.heappush(open_list, node[0])
                            open_dict[node[0].coord] = [node[0].f_val]



a1 = Astar((3,2), (4,6))

a1.pathFinder()










