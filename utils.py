import yaml

with open("config.yaml", "r") as file:
  data = yaml.safe_load(file)
 
movement_costs = data['movement_costs']
