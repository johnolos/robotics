#!/usr/bin/env python2
"""
ME/ECE 179P, Homework #3 Python
This is a sketch of the breadth-first-search algorithm.
Notice that all indices in this example are one less than in
MATLAB code.

Written by John O. Storvold
Date: 28th of October, 2014
"""

def bfs_edges(start, adj_table, return_parent_table=None):
  """
  Exercise E2.7 i)
  Finds all edges by using breadth-first-search algorithm.
  """
  num_nodes = len(adj_table)
  parent = num_nodes*[None]
  parent[start] = -1
  queue = [start]
  edges = []
  # This runs a BFS to discover edges based on the adj_table
  while queue:
    node1 = queue.pop(0)  # remove the element at the front of the queue
    for node2 in adj_table[node1]:  # loop over all neighbors of node1
      if parent[node2] is None:
        parent[node2] = node1
        edges.append((node1,node2))
        queue.append(node2)
  if return_parent_table:
    return edges, parent
  return edges

def compute_bfs_path(start, goal, adj_table):
  """
  Exercise E2.7 ii)
  Finds a path by using the edges computed by bfs_edges(...)
  """
  edges, parent = bfs_edges(start, adj_table, return_parent_table=True)
  x_list, y_list = zip(*edges)
  path = [goal]
  while(True):
    try:
      index = y_list.index(path[0])
    except ValueError:
      # There is no path possible from start to goal.
      return []
    path.insert(0, x_list[index]) # Insert node at front of list
    if path[0] == start:
      return path

def main():
  """
  Exercise E2.7
  Run this python file and both E2.7 i) and ii) will run.
  """
  start = 0
  goal = 20
  adj_table = [
  [1],
  [0,2,5],
  [1,3],
  [2,4,6,12],
  [3,5],
  [1,4],
  [3,7],
  [6,8],
  [7,9,13],
  [8,10],
  [9,11],
  [10,12],
  [3,11],
  [8,14],
  [13,15],
  [14,16],
  [15,17],
  [16,18],
  [17,19,20],
  [18],
  [18]]

  edges = bfs_edges(start, adj_table)
  print "\nEdges computed by bfs_edges(start, adj_table):\n", edges
  path = compute_bfs_path(start, goal, adj_table)
  print "\nPath computed by compute_bfs_path(start, goal, adj_table):\n", path

if __name__ == '__main__':
  main()  # execute the BFS on the data provided
