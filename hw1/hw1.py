#!/usr/bin/env python2
import math
import sys


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


def get_distance_point_to_line(q, p1, p2):
    """
    :param q: the test point as a 2D tuple
    :param p1: the first point defining the line
    :param p2: the second point defining the line
    :return: the distance from the test point q to the line defined by p1 and p2
    """

    return True


def get_distance_point_to_segment(q, p1, p2):
    """
    :param q: the test point as a 2D tuple
    :param p1: the first endpoint of the line segment
    :param p2: the second endpoint of the line segment
    :return: the distance from the test point q to the line segment
            with endpoints p1 and p2
    """

    return True

"""
# example of usage
point1 = (1, 2)
point2 = (3, 7)
a, b, c = get_line_through_two_points(point1, point2)
print "the coefficients a, b, c of the line ax + by + c = 0 are: ", a, b, c
#check that ax + by + c = 0
print "This should be very close to zero:", a*point1[0] + b*point1[1] + c
print "This should also be very close to zero:", a*point2[0] + b*point2[1] + c

"""
