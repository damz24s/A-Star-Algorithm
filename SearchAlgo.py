# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 21:29:11 2025

@author: samue
"""

import heapq
from Node import Node
import LoadData as ld
import GridConstructor as gc


class Astar:
    
    def isGoal(self, node):
        
        if node.coord == ld.goal:
            print("Goal found!!!")
            return True
        else:
            return False



    def pathReconstruct(self, node, grid): 
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
        
        gc.printGrid(grid)


    def gCostCalculator(self, curr_node, movement_cost):
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)]   
        parent = curr_node.parent
        dx = (curr_node.coord[0] - parent.coord[0])
        dy = (curr_node.coord[1] - parent.coord[1])

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
        for items in gc.GridItems:
            if i == gc.GridItems.OBSTACLE.value:
                return False
            return True
            
       



    def neighbourGenerator(self, curr_node, grid, heu_name):
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)]   

        if heu_name == 'manhattan':
            for dir in directions[0:4]:
                neighbour = (curr_node.coord[0] + dir[0], curr_node.coord[1] + dir[1])
                if self.isValid(neighbour, grid):
                    new_neighbour = self.nodeCreator(neighbour)
                    yield new_neighbour
                
                continue
        
        elif heu_name == 'octile':
            for dir in directions:
                neighbour = (curr_node.coord[0] + dir[0], curr_node.coord[1] + dir[1])
                if self.isValid(neighbour, grid):
                    new_neighbour = self.nodeCreator(neighbour)
                    yield new_neighbour
                
                continue




    def pathFinder(self):
        start = Node(ld.start)
        goal = Node(ld.goal)
        open_list = [] #Open List for Priority tracking
        open_dict = {} #Open dictionary for membership trcking
        heapq.heapify(open_list)
        closed_list = []
        heu = ld.heuristic
        heu_name = ld.heu_name
        grid = gc.loadGrid()
        movement = ld.movement_costs
        
        curr_node = start
        heapq.heappush(open_list,(curr_node.f_val, curr_node))
        open_dict[curr_node] = curr_node.f_val
        
        while True:
            if len(open_dict) == 0:
                print("Goal not found!")
                break
            
            
            else:
                tuple = heapq.heappop(open_list)
                curr_node = tuple[1]
                open_dict.pop(curr_node)
                prev_node = curr_node
                closed_list.append(curr_node)

                if self.isGoal(curr_node):
                    self.pathReconstruct(curr_node, grid)
                    return

                generator = self.neighbourGenerator(curr_node, grid, heu_name)
                
                for neighbour in generator:
                    if neighbour not in open_dict.keys():
                        if neighbour in closed_list:
                            continue
                        neighbour.parent = prev_node
                        
                        neighbour.g_val = self.gCostCalculator(neighbour, movement)
                        neighbour.h_val = heu(neighbour.coord[0] , neighbour.coord[1], goal.coord[0], goal.coord[1])
                        neighbour.f_val = neighbour.g_val + neighbour.h_val
                        if self.isGoal(neighbour):
                            self.pathReconstruct(neighbour, grid)
                            return

                        heapq.heappush(open_list, (neighbour.f_val, neighbour))
                        open_dict[neighbour] = neighbour.f_val
                        
                    
                    else:
                        old_parent = neighbour.parent
                        neighbour.parent = prev_node
                        old_g = neighbour.g_val
                        curr_g = self.gCostCalculator(neighbour, movement)

                        if curr_g < old_g:
                            neighbour.g_val = curr_g
                            neighbour.f_val = neighbour.g_val + neighbour.h_val
                            heapq.heappush(open_list, (neighbour.f_val, neighbour))
                            open_dict.update({neighbour: neighbour.f_val})
                            
                        neighbour.parent = old_parent
                        continue






a1 = Astar()
a1.pathFinder()
