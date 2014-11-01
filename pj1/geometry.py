#!/usr/bin/env python2
import math, sys
import numpy as np
import pylab as pp
"""
Exercise E1.6 Lines and Segments

Author: John Storvold
Date: 13th of October, 2014
"""
def get_distance_point_to_line(q, p1, p2):
  """
  :param q: the test point as a 2D tuple
  :param p1: the first point defining the line
  :param p2: the second point defining the line
  :return: the distance from the test point q to the line defined by p1 and p2
  """
  (a, b, c) = get_line_through_two_points(p1, p2)
  return abs(a*q[0] + b*q[1] + c)/math.sqrt(a**2 + b**2)

def get_distance_to_segment(q, p1, p2):
  """
  :param q: the test point as a 2D tuple
  :param p1: the first endpoint of the line segment
  :param p2: the second endpoint of the line segment
  :return: the distance from the test point q to the line segment
    with endpoints p1 and p2
  """
  # let us write the line as p1 + u(p2 - p1). We can find u as
  segment_length = dist(p1, p2)
  u = ((q[0] - p1[0])*(p2[0] - p1[0]) + (q[1] - p1[1])*(p2[1] - p1[1]))/(segment_length**2)

  # if projection lines between endpoints then return distance to line
  # otherwise return closer endpoint
  if 0.0 <= u <= 1.0:
    return get_distance_point_to_line(q, p1, p2)
  elif u < 0.0:
    return dist(q, p1)
  else:
    return dist(q, p2)

def dist(p1, p2):
    """
    :param p1: a point p1 = (x1, y1) in 2D space
    :param p2: a point p2 = (x2, y2) in 2D space
    :return: the Euclidean distance between p1 and p2
    """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def get_line_through_two_points(p1, p2):
    """
    :param p1: a point in 2D specified as a tuple
    :param p2: a point in 2D specified as a tuple
    :return: a tuple (a,b,c) containing the coefficients of the line ax+ by = c passing through
    p1 and p2
    """
    # test that points are sufficiently far apart from one another
    if dist(p1, p2) < 1e-5:
        sys.stderr.write('Cannot compute line:  the two points are too close together\n')
        sys.exit(1)

        # if they are then compute the coefficients and scale things nicely
        a = p1[1] - p2[1]
        b = p2[0] - p1[0]
        c = p1[0]*p2[1] - p2[0]*p1[1]
        scale = math.sqrt(a**2 + b**2)
        return a/scale, b/scale, c/scale


def rotate_point_around_fixed_point(point, rot_point, theta):
    """
    :param point: a point in 2D specified as a tuple
    :param rot_point: a point in 2D specified as a tuple
    :param theta: a float number in radians
    :return: a point in 2D specified as a tuple where the point point has been
    rotated around point rot_point using theta. (See rotation in geometry)
    """
    #Translate to origin
    trans_point = (point[0] - rot_point[0], point[1] - rot_point[1])

    # Rotation
    rx = trans_point[0] * math.cos(theta) - trans_point[1] * math.sin(theta)
    ry = trans_point[0] * math.sin(theta) + trans_point[1] * math.cos(theta)

    # Translate back
    rp = (rx + rot_point[0], ry + rot_point[1])
    return rp
