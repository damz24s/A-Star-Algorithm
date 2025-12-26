# A* Pathfinding Algorithm (Python)

A built-from-scratch implementation of the A* pathfinding algorithm, designed with a strong focus on algorithmic correctness, state management, and robustness against common implementation fails.

This project allows users to configure the grid, heuristic, and movement costs via a YAML configuration file without modifying the core code.

---

## Features

- Custom implementation of the A* search algorithm (no pathfinding libraries)
- Coordinate-based state representation for consistent state comparison
- Priority queue (heap) open list with lazy removal of outdated nodes
- Global cost dictionary tracking best-known g-values per state
- Correct handling of node re-opening when a lower-cost path is found
- Parent tracking for deterministic path reconstruction
- Configurable heuristics and movement costs via `config.yaml`

---

## Project Structure

.
├── SearchAlgo.py
├── Node.py
├── GridConstructor.py
├── Heuristic.py
├── LoadData.py
├── utils.py
├── config.yaml
├── requirements.txt
└── README.md

---

## Requirements

- Python 3.10+
- Dependencies listed in `requirements.txt`

Install dependencies:
pip install -r requirements.txt

---

## How to Run

From the project root:

The algorithm will:
1. Load parameters from `config.yaml`
2. Construct the grid
3. Run A* search using the selected heuristic
4. Print the resulting path and grid output

---

## Configuration (`config.yaml`)

The behaviour of the algorithm can be modified without changing code.

Example options include:
- Start and goal coordinates
- Grid size and obstacle placement
- Heuristic function (e.g. Manhattan, Octile)
- Movement costs (orthogonal vs diagonal)

After modifying `config.yaml`, simply re-run the program.

---

## Algorithm Notes

- Lazy removal is used instead of decrease-key due to Python’s `heapq` limitations.
- A global cost dictionary acts as the single source of truth for best-known g-values.
- Outdated nodes are discarded when popped from the open list.
- Nodes may be re-opened if a lower-cost path is discovered.

---

## Future Improvements

- Add automated tests for heuristic admissibility
- Optional visualisation of the search process
- Performance benchmarking on larger grids

---

## Author

Samuel Adegbusi
