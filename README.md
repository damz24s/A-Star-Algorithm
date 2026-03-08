A* Pathfinding Algorithm (Python)

A built-from-scratch implementation of the A* pathfinding algorithm, designed with a strong focus on algorithmic correctness, state management, and robustness against common implementation pitfalls. This project allows users to configure the grid, heuristic, and movement costs via a YAML configuration file without modifying the core code. A pygame-based visualiser is included to display the grid and animate the search process in real time.


Features

* Custom implementation of the A* search algorithm (no pathfinding libraries)
* Coordinate-based state representation for consistent state comparison
* Priority queue (heap) open list with lazy removal of outdated nodes
* Global cost dictionary tracking best-known g-values per state
* Correct handling of node re-opening when a lower-cost path is found
* Parent tracking for deterministic path reconstruction
* Configurable heuristics and movement costs via config.yaml
* Pygame visualiser with animated node exploration and shortest path reconstruction


Project Structure

Core Algorithm
── main.py
── SearchAlgo.py
── Node.py
── GridConstructor.py

Visualisation
── visualiser.py
── Display.py

Config / Utility
── LoadData.py
── Heuristic.py
── config.yaml
── utils.py
── requirements.txt


Requirements

* Python 3.10+
* pygame-ce
* Dependencies listed in requirements.txt

Install dependencies:
    pip install -r requirements.txt


How to Run

From the project root:
    python main.py

The program will present a menu with the following options:
1) Path Finder   - Runs A* and prints the resulting path
2) Display Grid  - Opens a pygame window showing the configured grid
3) Exit


Configuration (config.yaml)

The behaviour of the algorithm can be modified without changing any code.

Options include:
* Start and goal coordinates
* Grid size and obstacle placement
* Heuristic function (e.g. Manhattan, Octile)
* Movement costs (orthogonal vs diagonal)
* Cell size for the visualiser

After modifying config.yaml, simply re-run the program.


Algorithm Notes

* Lazy removal is used instead of decrease-key due to Python's heapq limitations.
* A global cost dictionary acts as the single source of truth for best-known g-values.
* Outdated nodes are discarded when popped from the open list.
* Nodes may be re-opened if a lower-cost path is discovered.


Author

Samuel Adegbusi
