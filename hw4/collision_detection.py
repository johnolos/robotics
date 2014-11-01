#!/usr/bin/env python2
from polygon import Polygon
"""
Exercise E4.8 Collision Dectection between Polygons

Author: John Storvold
Date: 13th of October, 2014
"""

def check_collision_between_polygons(polygon_1, polygon_2):
    """
    :param polygon_1: Polygon 1
    :param polygon_2: Polygon 2
    Check if there is a collision between the polygons by doing a check on
    the polygons vertices and by doing a check on the polygon's line segments.
    """

    # Check vertices inside eachother.
    if check_vertices_inside_polygon(polygon_1, polygon_2):
        return True

    # Check line segments are overlapping
    for p1, p2 in polygon_1.get_lines(): # Segments from polygon 1
        for p3, p4 in polygon_2.get_lines(): # Segments from polygon 2
            if check_intersecting_segments(p1,p2,p3,p4):
                return True
    return False

def check_vertices_inside_polygon(polygon_1, polygon_2):
    """
    :param polygon_1: Polygon 1
    :param polygon_2: Polygon 2
    Checks if either polygon's vertices are inside one another.
    """
    if polygon_1.inside_polygon(polygon_2):
        return True
    if polygon_2.inside_polygon(polygon_1):
        return True
    return False

def check_intersecting_segments(p1,p2,p3,p4):
    """
    :param p1: A point in 2D space.
    :param p2: A point in 2D space.
    :param p3: A point in 2D space.
    :param p4: A point in 2D space.
    Checks if two line segments are intersecting eachother.
    Line segment 1 is formed from point p1 and point p2.
    Line segement 2 is formed from point p3 and point p4.
    """
    s1 = (p2[0] - p1[0], p2[1] - p1[1])
    s2 = (p4[0] - p3[0], p4[1] - p3[1])

    # Ensure that it calculates corretly
    k = float(-s2[0] * s1[1] + s1[0] * s2[1])

    # If K is zero, the line segments are parallell to each other.
    if k == 0:
        return False
    s = (-s1[1] * (p1[0] - p3[0]) + s1[0] *(p1[1] - p3[1])) / k
    t = (s2[0] * (p1[1] - p3[1]) - s2[1] *(p1[0] - p3[0])) / k

    if 0 <= s <= 1 and 0 <= t <= 1:
        return True
    return False
