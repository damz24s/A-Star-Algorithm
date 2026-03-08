import pygame
import yaml


def visuals(obstacles, reconstructed, explored):
  pygame.init()


  with open("config.yaml", "r") as file:
    data = yaml.safe_load(file)

  #Data pulled from Config file
  cells = data['grid_size']
  start = data['start']
  goal = data['goal']
  cellSize = data['cell_size']


  #Rows x Columns of the Grid and the size of the cells
  cells_row = cells[0]
  cells_col = cells[1]
  cell_size = cellSize[0]

  width = cells_row * cell_size 
  height = cells_col * cell_size 



  #Creates 2D Array with cells
  grid = []
  x, y = 0, 0
  for rows in range(cells_row):
    cellRow=[]
    for cols in range(cells_col):
      cell = pygame.Rect((x, y, cell_size, cell_size))
      cellRow.append(cell)
      x += cell_size+1
      #After adding a cell, move 1 cell to the right
    y += cell_size+1
    #After a row is completed move 1 cell down
    x = 0
    grid.append(cellRow)



  #COLOURS
  YELLOW = ((255, 215, 0))
  RED = ((255, 0, 0))
  GREEN = ((0, 255, 0))
  BLUE = ((0, 0, 255))
  BLACK = ((0, 0, 0))
  GREY = ((50, 50, 50))
  WHITE = ((255, 255, 255))

  clock = pygame.time.Clock()

  #Setting screen width and height based on Cell and Grid sizes
  screen_width = width
  screen_height = height
  screen = pygame.display.set_mode((screen_width, screen_height))
  pygame.display.set_caption("A* Visualisation")


  counter = 0
  counter2 = 0

  running = True
  while running:
    
    #Makes background black
    screen.fill(BLACK)


#Setting the Colours for, start, goal cells
    for row in grid:
      for cell in row:
        pygame.draw.rect(screen, WHITE, cell)

        if grid[start[0]][start[1]] == cell:
          pygame.draw.rect(screen, GREEN, cell)

        elif grid[goal[0]][goal[1]] == cell:
          pygame.draw.rect(screen, RED, cell)


    if len(obstacles) != 0:
      for pair in range(0, len(obstacles), 2):
        obs = obstacles[pair]
        obs1 = obstacles[pair + 1]
        #assign the first two obstacle coords in the list
        #first two coords represent the start(obs) and end(obs1) of the 'wall' obstacle

        cell = grid[obs[0]][obs[1]]
        if cell == pygame.draw.rect(screen, WHITE, cell):
          pygame.draw.rect(screen, GREY, cell)
        #if the current cell isn't an obstacle, make it one
    
        beginning = (obs[0], obs[1])
        dx = (obs[0] - obs1[0])
        dy = (obs[1] - obs1[1])
        #calculate the change in x and y coords between 'start' and 'end' of the obstacle

        curr = beginning
        if dx > 0:
          for i in range(dx):
            curr = (curr[0] - 1, curr[1])
            cell = grid[curr[0]][curr[1]] 
            pygame.draw.rect(screen, GREY, cell)
            #if difference in x is greater than 0
            #the wall is vertical, going *up* from the start point

        elif dx < 0:
          for i in range(abs(dx)):
            curr = (curr[0] + 1, curr[1])
            cell = grid[curr[0]][curr[1]] 
            pygame.draw.rect(screen, GREY, cell)
            #the wall is vertical, going *down* from start point

        elif dy > 0:
          for i in range(dy):
            curr = (curr[0], curr[1] - 1)
            cell = grid[curr[0]][curr[1]]
            pygame.draw.rect(screen, GREY, cell)
            #if y difference greater than 0
            #wall is horizontal, going *left* from the start point

        elif dy < 0:
          for i in range(abs(dy)):
            curr = (curr[0], curr[1] + 1)
            cell = grid[curr[0]][curr[1]] 
            pygame.draw.rect(screen, GREY, cell)
            #the wall is goint *right* from the starting point

    
    for i in range(1, counter, 1):
      cell = grid[explored[i][0]][explored[i][1]]
      pygame.draw.rect(screen, BLUE, cell)
    if counter < len(explored):
      counter += 1
    
    else: 
      for i in range(1, counter2 - 1, 1):
        cell = grid[reconstructed[i][0]][reconstructed[i][1]]
        pygame.draw.rect(screen, YELLOW, cell)
      if counter2 < len(reconstructed):
        counter2 += 1


    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False



    pygame.display.flip()
    clock.tick(12)
  pygame.quit()

