#!/usr/bin/env python2
from geometry import dist, get_distance_to_segment, rotate_point_around_fixed_point
import math
import numpy as np
import pylab as pp

class Polygon(object):
  def __init__(self):
    self.points = []
  def initiate_list(self, list_of_x, list_of_y):
    for x, y in zip(list_of_x, list_of_y):
      self.points.append((x,y))
  def add_point(self, point_tuple):
    self.points.append(point_tuple)
  def get_points_as_lists(self):
    return zip(*self.points)
  def get_distance_point_to_polygon(self, q):
    lines = self.get_lines()
    p1, p2 = lines[0]
    distance = get_distance_to_segment(q,p1,p2)
    for p1, p2 in lines:
      temp_distance = get_distance_to_segment(q,p1,p2)
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
    distance = get_distance_to_segment(q,ret_p1,ret_p2)
    for p1, p2 in lines:
      temp_distance = get_distance_to_segment(q,p1,p2)
      if distance > temp_distance:
        distance = temp_distance
        ret_p1 = p1
        ret_p2 = p2
    return ret_p1, ret_p2, distance

  def get_tangent_vector(self, point):
    min_vertex_dist = float("inf")
    min_vertex = None
    min_edge_dist = float("inf")
    min_edge = None
    # first find the closest vertex
    for vertex in self.points:
      dist_to_vertex = dist(point, vertex)
      if dist_to_vertex < min_vertex_dist:
        min_vertex_dist = dist_to_vertex
        min_vertex = vertex

    # next, find the closest edge
    for i, vertex1 in enumerate(self.points):
      if i < len(self.points) - 1:
        vertex2 = self.points[i + 1]
      else:
        vertex2 = self.points[0]
        if vertex1[0] == vertex2[0] and vertex1[1] == vertex2[1]:
          break

      dist_to_edge = get_distance_to_segment(point, vertex1, vertex2)
      if dist_to_edge < min_edge_dist:
        min_edge_dist = dist_to_edge
        min_edge = [vertex1, vertex2]

    # compare closest edge and closest vertex
    if min_vertex_dist <= min_edge_dist + 10e-5:
      # then closest point on polygon is min_vertex
      # compute unit vector from point to min_vertex
      x_component = (min_vertex[0] - point[0]) / dist(min_vertex, point)
      y_component = (min_vertex[1] - point[1]) / dist(min_vertex, point)
      # now rotate this vector by -pi/2 to get counterclockwise tangent
      return (y_component, -x_component)

    else:  # the closest point on the polygon is min_edge
      x_component = (min_edge[1][0] - min_edge[0][0]) / dist(min_edge[0], min_edge[1])
      y_component = (min_edge[1][1] - min_edge[0][1]) / dist(min_edge[0], min_edge[1])
      return (x_component, y_component)

  def set_shift(self, d_1, d_2):
    for index, value in enumerate(self.points):
      self.points[index] = (value[0] * d_1 + d_2, value[1] * d_1 + d_2)

  def point_inside(self, point):
    x, y = point
    n = len(self.points)
    inside = False

    p1x,p1y = self.points[0]
    for i in range(n+1):
      p2x,p2y = self.points[i % n]
      if y > min(p1y,p2y):
        if y <= max(p1y,p2y):
          if x <= max(p1x,p2x):
            if p1y != p2y:
              xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
            if p1x == p2x or x <= xinters:
              inside = not inside
      p1x,p1y = p2x,p2y
    return inside
