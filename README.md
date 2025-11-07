Foxes and Chickens Search Algorithms:
----
This is a Python project that solves the classic Foxes and Chickens problem using three uninformed search 
algorithms: Breadth-First Search (BFS), Depth-First Search (DFS), and Iterative Deepening Search (IDS).

The goal is to move all foxes and chickens safely across the river without ever allowing the foxes to 
outnumber the chickens on either side.


Project Overview:
----
  - FoxProblem.py – defines the problem setup, rules, and valid state transitions
  - uninformed_search.py – implements BFS, DFS, and IDS search algorithms
  - SearchSolution.py – formats and stores the results of each search
  - foxes.py – main script that runs the algorithms and prints the results


How to Run:
----
Clone the repository and run the main script:

python3 foxes.py


Example output:
----
Chickens and foxes problem: (5, 4, 1)
attempted with search method BFS
number of nodes visited: 27
solution length: 11
path: [(5, 4, 1), (4, 4, 0), (4, 2, 1), ... , (0, 0, 0)]


Requirements:
----
Python 3.10 or later
No external libraries required


Purpose:
---

This project was created as a simple way to understand and compare different search algorithms for solving a well-known AI problem. It’s a useful example for anyone learning about state space search and algorithm design in Python.
