#!/usr/bin/env python2
import geometry as geo
import math
import numpy as np
import pylab as pp

class Polygon(object):
  def __init__(self):
    self.points = []

  def initiate_list(self, list_of_points):
    self.points = list_of_points

  def add_point(self, point_tuple):
    self.points.append(point_tuple)

  def get_distance_point_to_polygon(self, q):
    lines = self.get_lines()
    p1, p2 = lines[0]
    distance = geo.get_distance_to_segment(q,p1,p2)
    for p1, p2 in lines:
      temp_distance = geo.get_distance_to_segment(q,p1,p2)
      if distance > temp_distance:
        distance = temp_distance
    return distance

  def plot_point(self, p1):
    pp.plot(p1[0],p1[1],"or")

  def plot_line(self, p1, p2):
    pp.plot((p1[0],p2[0]),(p1[1],p2[1]),"b")

  def plot(self):
    if len(self.points) < 2:
      return -1
    x_list, y_list = zip(*self.points)
    pp.ylim(min(y_list) - 5, max(y_list) + 5)
    pp.xlim(min(x_list) - 5, max(x_list) + 5)
    lines = self.get_lines()
    for p1, p2 in lines:
      self.plot_point(p1)
      self.plot_line(p1,p2)
    pp.show()

  def get_lines(self):
    array_of_pairs = []
    array_length = len(self.points)
    for index, value in enumerate(self.points):
      if index != array_length - 1:
        p1 = value
        p2 = self.points[index + 1]
      else:
        p1 = value
        p2 = self.points[0]
      array_of_pairs.append(( p1, p2 ))
    return array_of_pairs

  def get_closest_segment(self, q):
    lines = self.get_lines()
    ret_p1, ret_p2 = lines[0]
    distance = geo.get_distance_to_segment(q,ret_p1,ret_p2)
    for p1, p2 in lines:
      temp_distance = geo.get_distance_to_segment(q,p1,p2)
      if distance > temp_distance:
        distance = temp_distance
        ret_p1 = p1
        ret_p2 = p2
    return ret_p1, ret_p2, distance

  def get_tanget_vector(self, q):
    p1, p2, distance = self.get_closest_segment(q)
    closest_point = None
    if geo.dist(q, p1) == distance:
      closest_point = p1
    elif geo.dist(q, p2) == distance:
      closest_point = p2
    print closest_point
    if closest_point != None:
      # Need to rotate vector -90 degrees corresponding to origin point
      # Rotating by -90 degrees (-PI /2 rads)
      computed_point = (closest_point[0] - q[0], closest_point[1] - q[1]) # Computed line
      #lot = (cp[0]*4.0,cp[1]*4.0)
      normal_point = (q[0] + computed_point[0], q[1] + computed_point[1])
      theta = -math.pi/2
      rp = geo.rotate_point_around_fixed_point(normal_point, q, theta)
    else:
      # Segment closest
      x = p2[0] - p1[0]
      y = p2[1] - p1[1]
      rp = (x, y)
    return rp


def main():
  pol = Polygon()
  list_of_points = [(1,0),(3,0),(4,1),(4,3),(3,4),(1,4),(0,3),(0,1)]
  point = (-0.33,3.1)
  pp.plot(point[0],point[1],"or")
  pol.initiate_list(list_of_points)
  dist = pol.get_distance_point_to_polygon(point)
  print dist
  p1, p2, distance = pol.get_closest_segment(point)
  print p1, p2
  tangent_point = pol.get_tanget_vector(point)
  pol.plot_line(tangent_point, point)
  pol.plot()
main()
