#% Computes the path a Bug would follow until it hits an obstacle.
#% Function requires start and goal point as well as a cell array of
#% polygonal obstacles and returns an ordered list of all of the points
#% visited by the bug along its path. Note that each polygon is
#% defined by a n x 2 array of counterclockwise points.

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#% Intro to Robotics, ME170A/ECE181A, Spring 2009
#% Joey Durham
#% April 25, 2010
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import math
import sys
import time
import numpy as np
import matplotlib.pyplot as pp
from geometry import dist

def computeBug1Path(start,goal,PolyList):
  maxStepSize = 0.07
  # Initialize the path variable
  path = [start];
  # Loop continuously until Bug reaches a termination condition and breaks
  #out of the loop
  distance_length = 0

  while(True):
    distToGoal = dist(path[-1], goal)
    # Has bug reached goal location?
    if( distToGoal < maxStepSize ):
      break

    distToClosestObstacle = distToGoal + maxStepSize;
    closestPolygon = None

    #% Loop through each polygonal obstacle in the list to find the closest
    #% one to the Bug's current position.
    for p in PolyList:
      distToObstacle = p.get_distance_point_to_polygon(path[-1])
      if(distToObstacle < distToClosestObstacle):
        distToClosestObstacle = distToObstacle
        closestPolygon = p

    #% Is bug inside polygon?
    #I do not have a built in function inpolygon. So.. Here you have to make your own, or find a package

    if closestPolygon != None:
      if len(closestPolygon.points) > 0 and closestPolygon.point_inside(path[-1]):
        print('Error - Bug inside polygon')
        return path

    #% Limit the length of a step the Bug will take based on proximity to
    #% obstacles, goal so that it does not over shoot and enter an obstacle
    #% or pass the goal location.
    stepSize = min(maxStepSize, distToClosestObstacle/5, distToGoal)

    #% Has bug hit an obstacle?
    if(distToClosestObstacle < maxStepSize):
      start = path[-1]
      circumPath = []
      circum_navigating = True
      index, cnt = 0, 0
      closest_distance_to_goal = float("inf")
      # Base condition to avoid redudance points in path.
      u_x, u_y = closestPolygon.get_tangent_vector(start)
      step = [stepSize*u_x, stepSize*u_y]
      x = start[0] + step[0]
      y = start[1] + step[1]
      newPoint = (x,y)
      distance_length += dist(start, newPoint)
      circumPath.append(newPoint)

      while(circum_navigating):
        u_x, u_y = closestPolygon.get_tangent_vector(circumPath[-1])
        step = [stepSize*u_x, stepSize*u_y]
        x = circumPath[-1][0] + step[0]
        y = circumPath[-1][1] + step[1]
        newPoint = (x,y)
        distance_length += dist(circumPath[-1],newPoint)
        circumPath.append(newPoint)
        temp_distance = dist(newPoint,goal)
        if temp_distance < closest_distance_to_goal:
          closest_distance_to_goal = temp_distance
          index = cnt
        if dist(start,newPoint) < maxStepSize and cnt > 10:
          circum_navigating = False
        cnt+=1
      for i in range(1,index):
        distance_length += dist(circumPath[i-1], circumPath[i])
      path.extend(circumPath[0:index])

      # Robot steps inside if point is inside polygon. Then terminates
      u_x = (goal[0] - path[-1][0])/distToGoal
      u_y = (goal[1] - path[-1][1])/distToGoal

      #% Add new step to end of the path
      step = [stepSize*u_x, stepSize*u_y]
      newPoint = path[-1][0]+step[0],path[-1][1]+ step[1]
      distance_length += dist(path[-1], newPoint)
      path.append(newPoint)

    else:
      #% Step towards goal along unit vector u between current point and goal
      u_x = (goal[0] - path[-1][0])/distToGoal
      u_y = (goal[1] - path[-1][1])/distToGoal

      #% Add new step to end of the path
      step = [stepSize*u_x, stepSize*u_y]
      newPoint = path[-1][0]+step[0],path[-1][1]+ step[1]
      distance_length += dist(path[-1], newPoint)
      path.append(newPoint)
  print "Total length traveled: ", distance_length
  return path
