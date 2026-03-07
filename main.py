from Node import Node
import LoadData as ld
import GridConstructor as gc
from SearchAlgo import Astar as A

def main():
  start = Node(ld.start)
  goal = Node(ld.goal)
  heu = ld.heuristic
  heu_name = ld.heu_name
  grid = gc.loadGrid()
  movement = ld.movement_costs
  a_star = A()


  while True:
    try:
      print("\n------Main Menu------")
      print("------Select choices between 1 - 3 ------\n")
      print("1) Path Finder")
      print("2) Print Grid")
      print("3) Exit")

      choice = int(input("Enter choice here: "))

      if choice == 1:
        path = a_star.pathFinder(start, goal, grid, movement, heu, heu_name)
        print(path)
        continue

      elif choice == 2:
        g = gc.printGrid(grid)
        continue
      
      elif choice == 3:
        print("----- GoodBye -----\n")
        return
      
    except ValueError:
      print("Please enter a valid ~ integer ~\n")
      continue

main()