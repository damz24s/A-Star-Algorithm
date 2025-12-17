import yaml
#read the config file
with open("config.yaml", "r") as file:
  data = yaml.safe_load(file)

#load grid size - format: [r, c]  
grid_size = data["grid_size"]
g = grid_size

#load start and goal coordinates - format: [x, y]
start_coord = data["start"]
goal_coord = data["goal"]

#load heuristics of choice
heuristic = data["heuristic"]

obstacles = []
f = data["obstacle_shape"]
#load obstacles in the shape of a list of a dict within a dict - format: [{key:{key:[val],},...}]


for item in f:
  for k, v in item.items():
    for val in v.values():
      obstacles.append(val)
#for each item in the obstacles list, (dict)
#for each key(k) and value(v) pair, key == key, value == {key:[val]}
#search through the values of values, {key:[val]}, and append them to the list


    
  
