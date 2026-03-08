from Node import Node
import LoadData as ld
import GridConstructor as gc
from SearchAlgo import Astar as A
import Display as D
import Visualiser as v

def main():
  start = Node(ld.start)
  goal = Node(ld.goal)
  heu = ld.heuristic
  heu_name = ld.heu_name
  grid = gc.loadGrid()
  movement = ld.movement_costs
  a_star = A()
  obstacles = ld.obstacles

  path = a_star.pathFinder(start, goal, grid, movement, heu, heu_name)
  while True:
    try:
      print("\n------Main Menu------")
      print("------Select choices between 1 - 3 ------\n")
      print("1) Find Shortest Path")
      print("2) Display Grid")
      print("3) Exit")

      choice = int(input("Enter choice here: "))

      if choice == 1:
        v.visuals(obstacles, path[0], path[1])
        continue

      elif choice == 2:
        D.display(obstacles)
        continue
      
      elif choice == 3:
        print("----- GoodBye -----\n")
        return
      
    except ValueError:
      print("Please enter a valid ~ integer ~\n")
      continue

main()