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


    def gCostCalculator(self, curr_node):
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)]   
        parent = curr_node.parent
        dx = (curr_node.coord[0] - parent.coord[0])
        dy = (curr_node.coord[1] - parent.coord[1])

        if (dx, dy) in directions[0:4]:
            curr_node.g_val = parent.g_val + 10
            return curr_node.g_val
        
        else:
            curr_node.g_val = parent.g_val + 14
            return curr_node.g_val



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
        
        curr_node = start
        heapq.heappush(open_list,(curr_node.f_val, curr_node))
        open_dict[curr_node.coord] = curr_node.f_val
        
        while True:
            if len(open_dict) == 0:
                print("Goal not found!")
                break
            
            
            else:
                tuple = heapq.heappop(open_list)
                curr_node = tuple[1]
                popped = open_dict.pop(curr_node.coord)
                prev_node = curr_node
                closed_list.append(curr_node.coord)

                if self.isGoal(curr_node):
                    self.pathReconstruct(curr_node, grid)
                    return

                generator = self.neighbourGenerator(curr_node, grid, heu_name)
                
                for node in generator:
                    if node.coord in open_dict.keys() or node.coord in closed_list:
                        old_parent = node.parent
                        node.parent = prev_node
                        old_g = node.g_val
                        curr_g = self.gCostCalculator(node)
                        if curr_g < old_g:
                            node.g_val = curr_g
                            node.f_val = node.g_val + node.h_val
                            heapq.heappush(open_list, (node.f_val, node))
                            open_dict.pop(node.coord)
                            open_dict[node.coord] = node.f_val
                            continue 

                        node.parent = old_parent
                        continue
                    
                    else:
                        node.parent = prev_node
                        
                        node.g_val = self.gCostCalculator(node)
                        node.h_val = heu(node.coord[0] , node.coord[1], goal.coord[0], goal.coord[1])
                        node.f_val = node.g_val + node.h_val
                        if self.isGoal(node):
                            self.pathReconstruct(node, grid)
                            return

                        heapq.heappush(open_list, (node.f_val, node))
                        open_dict[node.coord] = node.f_val



a1 = Astar()
a1.pathFinder()
