import pygame
import yaml
from LoadData import obstacles

pygame.init()

with open("config.yaml", "r") as file:
  data = yaml.safe_load(file)

cells = data['grid_size']
start = data['start']
goal = data['goal']

cells_row = cells[0]
cells_col = cells[1]
cell_size = 50

width = cells_row * cell_size 
height = cells_col * cell_size 

def posCalc(row, col):
  new_pos = (cells_row * row) + col
  return new_pos
    

start_pos = posCalc(start[0], start[1])
goal_pos = posCalc(goal[0], goal[1])
obs_pos_list = []

while len(obstacles)!=0:

  obs_start = obstacles[0]
  obs_end = obstacles[1] 
  #print(obs_start, obs_end)
  obstacles.pop(0)
  obstacles.pop(0)
  obs = (posCalc(obs_start[0], obs_start[1]), posCalc(obs_end[0], obs_end[1]))
  obs_pos_list.append(obs)

print(obs_pos_list)

cellList = []
x, y = 0, 0
for col in range(cells_col):
  for row in range(cells_row):
    cell = pygame.Rect((x, y, cell_size, cell_size))
    cellList.append(cell)
    x += cell_size+1
  y += cell_size+1
  x = 0

#print(cellList)


RED = ((255, 0, 0))
GREEN = ((0, 255, 0))
BLUE = ((0, 0, 255))
BLACK = ((0, 0, 0))
WHITE = ((255, 255, 255))

clock = pygame.time.Clock()

screen_width = width
screen_height = height
screen = pygame.display.set_mode((screen_width, screen_height))


running = True
while running:
  
  
  screen.fill(BLACK)
  pygame.key.start_text_input()



  for cell in cellList:
    pygame.draw.rect(screen, WHITE, cell)


  if len(obs_pos_list) != 0:
    for x, y in obs_pos_list:
      obs_start_pos = x
      obs_end_pos = y

      obs_start_pos = str(obs_start_pos)
      obs_end_pos = str(obs_end_pos)

      if obs_start_pos[0] == obs_end_pos[0]:
  
        slice = cellList[int(obs_start_pos[1]) : int(obs_end_pos[1])+1]
        for i in range(len(slice)):
          pygame.draw.rect(screen, BLUE, slice[i])
        
      elif obs_start_pos[1] == obs_end_pos[1]:

        slice = cellList[int(obs_start_pos[1]) : int(obs_end_pos[1])+1]
        for i in range(len(slice)):
          pygame.draw.rect(screen, BLUE, slice[i])



  counter = 0
  for cell in cellList:
    if counter == start_pos:
      pygame.draw.rect(screen, GREEN, cell)
    elif counter == goal_pos:
      pygame.draw.rect(screen, RED, cell)
    counter+=1



  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False



  pygame.display.flip()
  clock.tick(500)


pygame.quit()