#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Intro to Robotics, ME170A/ECE181A, Spring 2009
# Joey Durham
# April 25, 2010
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import math
import sys
import time
import polygon as pol
from geometry import dist
import computeBug1Path as bug
import numpy as np
import matplotlib.pyplot as pp

def testBugEnviroment():
  print("#________________TESTING_____________________#")
  #Define start and goal positions plus a couple of polygonal obstacles
  start = (.3,.3)
  #goal = (5.4,4.2)
  goal = (3.5,3.5)

  Poly1 = pol.Polygon()
  Poly1.initiate_list([-0.6,-0.4,0.7,0.6,0.2,-0.296057],[0.3,-0.4,-0.3,0.4,0.3,0.596997])


  Poly2 = pol.Polygon()
  Poly2.initiate_list([-0.8,-0.1,0.9,0.3,0.102922,-0.3],[-0.4,-0.1,-0.4,0.2,0.598169,0.4])

  #Shift polygons into positions along path to create obstacles
  Poly1.set_shift(1.5, 1.5)
  Poly2.set_shift(2.0, 3.5)

  #Need to create a list of these obstacles to define the environment
  PolyList = [Poly1,Poly2]

  path = []

  #Bug algorithm invocation goes here
  tic = time.time()
  path = bug.computeBug1Path(start,goal,PolyList);
  toc = time.time()
  print "Time to find path in ms: ", (toc-tic)*1000

  totalPathLenght = 0
  for i in range(0,len(path)-1):
      totalPathLenght += dist(path[i],path[i+1])
  print "Total path length: ", totalPathLenght

  #Plot path of Bug
  drawPolygonAndPoint(PolyList,start,goal,path)

  #Plot distance to goal
  distanceToGoal = []
  total_distance_traveled = 0
  for i in range(len(path)):
    distanceToGoal.append(dist((path[i][0],path[i][1]),goal))
  drawDistanceToGoal(distanceToGoal)

def drawPolygonAndPoint(P,start,end,path):
  #Plot each polygon in P on pp
  for p in P:
    #x_list, y_list = p.get_points_as_lists()
    lines = p.get_lines()
    for p1, p2 in lines:
      p.plot_line(p1,p2)
    pp.ylim(0,6)
    pp.xlim(0,6)
    pp.grid()

  #Plot the path
  for p in path:
      pp.plot(p[0],p[1],'ro');

  #Plot start and end
  pp.plot(start[0],start[1],'ro')
  pp.plot(end[0],end[1],'ro')
  pp.show()

def drawDistanceToGoal(distanceToGoal):
  #Plot the graph
  #for i in range(0,len(distanceToGoal)):
  pp.ylim(0,max(distanceToGoal))
  pp.xlim(0,len(distanceToGoal))
  pp.grid()
  pp.plot(distanceToGoal,'ro')
  pp.show()

testBugEnviroment()
