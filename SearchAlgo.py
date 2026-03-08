# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 21:29:11 2025

@author: samue
"""

import heapq
from Node import Node



class Astar:
    
    def isGoal(self, node_coord, goal_coord):
        
        if node_coord == goal_coord:
            return True
        else:
            return False



    def pathReconstruct(self, start, goal, overall, grid): 
        coordPath = []
        coordPath.append(goal)
        current = goal

        while current != start:
            list = overall.get(current)
            coordPath.append(list[1])
            current = list[1]

        coordPath.reverse()
        return coordPath



    def gCostCalculator(self, curr_node, parent_coord, movement_cost):
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)]   

        dx = (curr_node.coord[0] - parent_coord[0])
        dy = (curr_node.coord[1] - parent_coord[1])

        if (dx, dy) in directions[0:4]:
            g_val = movement_cost[0]
            return g_val
        
        else:
            g_val = movement_cost[1]
            return g_val



    def nodeCreator(self, new_node_coord):
        new_node = Node((new_node_coord))
        return new_node



    def isValid(self, curr_node, grid):
        if curr_node[0] < 0 or curr_node[0] > (len(grid) - 1) or curr_node[1] < 0 or curr_node[1] > (len(grid[0]) - 1):
            return False
        
        i = grid[curr_node[0]][curr_node[1]]
        if i == '#':
            return False
        return True
            
       



    def neighbourGenerator(self, curr_node_coord, grid, heu_name):
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)]   

        if heu_name == 'manhattan':
            for dir in directions[0:4]:
                neighbour = (curr_node_coord[0] + dir[0], curr_node_coord[1] + dir[1])
                if self.isValid(neighbour, grid):
                    new_neighbour = self.nodeCreator(neighbour)
                    yield new_neighbour
                
                continue
        
        elif heu_name == 'octile':
            for dir in directions:
                neighbour = (curr_node_coord[0] + dir[0], curr_node_coord[1] + dir[1])
                if self.isValid(neighbour, grid):
                    new_neighbour = self.nodeCreator(neighbour)
                    yield new_neighbour
                
                continue




    def pathFinder(self, start, goal, grid, movement, heu, heu_name):
        open_list = [] #Open List for Priority tracking
        overall_dict = {} #Overall dictionary for membership tracking
        explored = []
        heapq.heapify(open_list)
        closed_list = []
 
        
        curr_node = start
        heapq.heappush(open_list,(curr_node.f_val, curr_node.g_val, curr_node.coord))
        parent = curr_node.parent
        overall_dict[curr_node.coord] = [curr_node.g_val, None]
        
        while True:
            if len(open_list) == 0:
                return None
            
            
            
            else:
                tuple = heapq.heappop(open_list)
                curr_node_coord = tuple[2]
                curr_g = tuple [1]
                best_known = overall_dict.get(curr_node_coord)
                if curr_g > best_known[0]:
                    continue

                elif curr_g == best_known[0]:
                    closed_list.append(curr_node_coord)
                    explored.append(curr_node_coord)
                    generator = self.neighbourGenerator(curr_node_coord, grid, heu_name)
                    
                    for neighbour in generator:
                        parent = curr_node_coord
                        curr_g_val = self.gCostCalculator(neighbour, parent, movement) + overall_dict[parent][0]
                        
                        if neighbour.coord in overall_dict.keys():
                            best_known = overall_dict.get(neighbour.coord)
                            if curr_g_val >= best_known[0]:
                                continue

                            elif curr_g_val < best_known[0]:
                                overall_dict[neighbour.coord] = [curr_g_val, parent]
                                neighbour.f_val = curr_g_val + neighbour.h_val
                                heapq.heappush(open_list, (neighbour.f_val, curr_g_val, neighbour.coord))
                                continue

                        else:
                            neighbour.g_val = curr_g_val
                            neighbour.h_val = heu(neighbour.coord[0], neighbour.coord[1], goal.coord[0], goal.coord[1])
                            neighbour.f_val = neighbour.g_val + neighbour.h_val
   
                            overall_dict[neighbour.coord] = [neighbour.g_val, parent]
                            heapq.heappush(open_list, (neighbour.f_val, neighbour.g_val, neighbour.coord))
                            if self.isGoal(neighbour.coord, goal.coord):
                                return self.pathReconstruct(start.coord, neighbour.coord, overall_dict, grid), explored
                            
                            continue


