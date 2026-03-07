import yaml
import Heuristic as h

#read the config file
with open("config.yaml", "r") as file:
  data = yaml.safe_load(file)

#load grid size - format: [r, c]  
grid_size = data["grid_size"]

 
#load movement costs - format: [m, m1]/[m]  
movement_costs = data['movement_costs']


#load start and goal coordinates - format: [x, y]
start_coord = data["start"]
start = (start_coord[0], start_coord[1])
goal_coord = data["goal"]
goal = (goal_coord[0], goal_coord[1])

#load heuristics of choice
heuristic = data["heuristic"]

if heuristic == 'octile':
  heuristic = h.octile 
  heu_name = 'octile'

elif heuristic == 'manhattan':
  heuristic = h.manhattan
  heu_name = 'manhattan'


obstacles = []
f = data["obstacle_shape"]
#load obstacles in the shape of a list of a dict within a dict - format: [{key:{key:[val],},...}]


for item in f:
  for k, v in item.items():
    for val in v.values():
      obstacles.append(val)
#for each item in the obstacles list, (dict)
#for each key(k) and value(v) pair, key == wall, value == {coord1:[row, col], coord2:[row, col]}
#search through the values of values, {[row, col]}, and append them to the list


    
  
