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
import geometry as geo

def computeBugBasePath(start,goal,PolyList):
  maxStepSize = 0.02;
  # Initialize the path variable
  path = [start];
  # Loop continuously until Bug reaches a termination condition and breaks
  #out of the loop
  while(true):
    distToGoal = geo.dist(path[-1], goal)
    # Has bug reached goal location?
    if( distToGoal < maxStepSize ):
      break

    distToClosestObstacle = distToGoal + maxStepSize;
    closestPolygon = [];

    #% Loop through each polygonal obstacle in the list to find the closest
    #% one to the Bug's current position.
    for p in PolyList:
      distToObstacle = computeDistancePointToPolygon(path[-1],p)
        if( distToObstacle < distToClosestObstacle ):
          distToClosestObstacle = distToObstacle;
          closestPolygon = p

    #% Is bug inside polygon?
    #I do not have a built in function inpolygon. So.. Here you have to make your own, or find a package
    if(len(closestPolygon) > 0 && inpolygon(path[-1][0],path[-1][1], closestPolygon(:,1), closestPolygon(:,2)) ):
      print('Error - bug entered polygon')
      break

    #% Limit the length of a step the Bug will take based on proximity to
    #% obstacles, goal so that it does not over shoot and enter an obstacle
    #% or pass the goal location.
    stepSize = min(maxStepSize, distToClosestObstacle/5, distToGoal);

    #% Has bug hit an obstacle?
    if( distToClosestObstacle < maxStepSize )
      #% BugBase simply gives up if it hits an obstacle
      print('Could not find path to goal!')
      break
    else
      #% Step towards goal along unit vector u between current point and goal
      u_x = (goal[0] - path[-1][0])/distToGoal;
      u_y = (goal[1] - path[-1][1])/distToGoal;

      #% Add new step to end of the path
      step = [stepSize*u_x, stepSize*u_y];
      newPoint = path[-1][0]+step[0],path[-1][1]+ step[1];
      path.append(newPoint)
    return path
