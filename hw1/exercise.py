#!/usr/bin/env python2
import math, sys
import numpy as np
import pylab as pp
import hw1
"""
Exercise E1.6 Lines and Segments

Author: John Storvold
Date: 13th of October, 2014
"""

def exercise():
  p1 = (1, 1)
  p2 = (2, 2)
  plotPoint(p1)
  plotPoint(p2)
  plotLine(p1,p2)
  pp.show()


def distance(q, p1, p2):
  """
  Returns the distance between a point q and a line created by point p1 and
  point p2.
  """
  a, b, c = hw1.get_line_through_two_points(p1, p2)
  r = np.absolute(a*q[0]+b*q[1]+c) / np.sqrt(np.power(a,2.0) + np.power(b,2.0))
  return r

def distanceToLineSegment(q, p1, p2):
  """
  Returns the shortest distance between a point q and a line segment made by
  point p1 and point p2.
  """
  d = hw1.dist(p1,p2)
  if d == 0: return hw1.dist(q,p1)
  k = ((q[0] - p1[0]) * (p2[0] - p1[0]) + (q[1] - p1[1]) * (p2[1] - p1[1])) / d
  if k < 0: return hw1.dist(q, p1)
  if k > 1: return hw1.dist(q, p2)
  dx = p1[0] + k * (p2[0] - p1[0])
  dy = p1[1] + k * (p2[1] - p1[1])
  dp = (dx, dy)
  return hw1.dist(q,dp)

def plotPoint(p):
  pp.plot(p[0],p[1],"or")

def plotLine(p1,p2):
  pp.plot((p1[0],p2[0]),(p1[1],p2[1]),"b")

"""
Run the exercise
"""

exercise()

p1 = (1.0, 0.0)
p2 = (2.0, 0.0)
q = (1.5, -0.5)

r = distance(q,p1,p2)
print r

r = distanceToLineSegment(q, p1, p2)
print r
