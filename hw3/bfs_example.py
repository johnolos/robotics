#!/usr/bin/env python2
"""
ME/ECE 179P, Homework #3
This is a sketch of the breadth-first-search algorithm.
Notice that all indices in this example are one less than in
MATLAB code.
"""

def main():
  """
  BFS algorithm
  """
  num_nodes = 21
  # in python, indexing starts at zero, so we'll subtract one from every index
  # could also use dictionaries, but this is slightly more cumbersome
  adj_table = [[1],[0, 2, 3],[1, 4],[1],[2]]
  start = 4
  goal = 0

  # initialize the parent pointers as a list of "None"
  parent = num_nodes*[None]
  parent[start] = -1  # give a special marking for the start node
  queue = [start]  # initialize the queue

  edges = []

  while queue:
    node1 = queue.pop(0)  # remove the element at the front of the queue
    for node2 in adj_table[node1]:  # loop over all neighbors of node1
      if parent[node2] is None:
        parent[node2] = node1
        queue.append(node2)
        edges.append((node1, node2))
      # report the state of the queue
    print "processed node:", node1, "queue =", queue

    # finally, extract the path from the parent pointers
  path = [goal]
  current_node = goal
  while parent[current_node] != -1:
    current_node = parent[current_node]
    path.insert(0, current_node)  # insert current node at beginning of list

  print "path from", start, "to", goal, ":", path
  print edges


if __name__ == '__main__':
  main()  # execute the BFS on the data provided
