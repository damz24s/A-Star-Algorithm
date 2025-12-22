import LoadData as ld
import math
from enum import Enum

class GridItems(Enum):
  START = 's'
  Goal = 'g'
  OBSTACLE = '#'
  WALKABLE = '0'


def loadGrid():
  grid = []
  #create a row for the number of rows specifed in the config file
  for rows in range(ld.grid_size[0]):
    row=[]
    for cols in range(ld.grid_size[1]):
      row.append('0')
    grid.append(row)
    #for each row created, fill it with '0's equal to the number of coloumns specified
    #and add the row to the grid

  start = ld.start_coord
  goal = ld.goal_coord
  grid[start[0]][start[1]] = 's'
  grid[goal[0]][goal[1]] = 'g'
  #initialise the start and goal cells within the grid

  return loadObstacles(grid)



def loadObstacles(grid):
  obstacle = ld.obstacles
  
  while len(obstacle) != 0:
    obs = obstacle[0]
    obs1 = obstacle[1]
    obstacle.pop(0)
    obstacle.pop(0)
    #assign the first two obstacle coords in the list and pop them from the list
    #first two coords represent the start and end of the 'wall' obstacl

    if grid[obs[0]][obs[1]] != '#':
      grid[obs[0]][obs[1]] = '#'
      #if the current cell isn't an obstacle, make it one

    start = (obs[0], obs[1])
    dx = (obs[0] - obs1[0])
    dy = (obs[1] - obs1[1])
    #calculate the change in x and y coords between 'start' and 'end' of the obstacle

    curr = start
    if dx > 0:
      for i in range(dx):
        curr = (curr[0] - 1, curr[1])
        grid[curr[0]][curr[1]] = '#'
        #if difference in x is greater than 0
        #the wall is vertical, going *up* from the start point

    elif dx < 0:
      for i in range(abs(dx)):
        curr = (curr[0] + 1, curr[1])
        grid[curr[0]][curr[1]] = '#'
        #the wall is vertical, going *down* from start point

    elif dy > 0:
      for i in range(dy):
        curr = (curr[0], curr[1] - 1)
        grid[curr[0]][curr[1]] = '#'
        #if y difference greater than 0
        #wall is horizontal, going *left* from the start point

    elif dy < 0:
      for i in range(abs(dy)):
        curr = (curr[0], curr[1] + 1)
        grid[curr[0]][curr[1]] = '#'
        #the wall is goint *right* from the starting point

  return grid  

 
def printGrid(grid):
  for row in grid:
    print(row)

