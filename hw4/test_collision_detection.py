#!/usr/bin/env python2
"""
ME/ECE 179P, Homework #4
This script tests a polygon collision detector with four scenarios, one
where some vertices of one polygon are inside the other, one where two
polygons collide without this being the case, one where two polygons
do not collide, and one where the two polygons are the same.
"""
import timeit
from polygon import Polygon
import pylab as pp
from collision_detection import check_collision_between_polygons


def main():
    """
    Testing polygon collision detector
    """
    #test polygons
    polygon1 = Polygon([(0, 0), (4, 1), (4, 2), (0, 1)])
    polygon2a = Polygon([(-2, -1), (-1, -1), (0, 5), (-1, 5)])
    polygon2b = Polygon([(-0.5, 0.5), (0.5, 0.5), (1.5, 6.5), (0.5, 6.5)])
    polygon2c = Polygon([(0.5, -0.5), (1.5, -0.5), (2.5, 5.5), (1.5, 5.5)])

    # test 1 - no collision
    collision = check_collision_between_polygons(polygon1, polygon2a)
    if collision:
        print "***Error!  Collision detected when no collision exists***"
    else:
        print "No collision check passed"

    # test 2 - vertex collision
    collision = check_collision_between_polygons(polygon1, polygon2b)
    if not collision:
        print "***Error!  Vertex collision not detected***", "\n"
    else:
        print "Vertex collision check passed"

    # test 3 - segment collision
    collision = check_collision_between_polygons(polygon1, polygon2c)
    if not collision:
        print "***Error!  Segment collision not detected***"
    else:
        print "Segment collision check passed"

    # test 4 -- coincident polygons collision
    collision = check_collision_between_polygons(polygon1, polygon1)
    if not collision:
        print "***Error!  Coincident collision not detected***"
    else:
        print "Coincident collision check passed"

    ## Next, time many collision detection runs
    print "\n", "<<< Timing 1000 collision checks >>>", "\n"

    tic = timeit.default_timer()
    for i in range(1000):
        collision = check_collision_between_polygons(polygon1, polygon2a)
    toc = timeit.default_timer()
    print "No collision time:", toc - tic, "secs"

    tic = timeit.default_timer()
    for i in range(1000):
        collision = check_collision_between_polygons(polygon1, polygon2b)
    toc = timeit.default_timer()
    print "Vertex collision time:", toc - tic, "secs"

    tic = timeit.default_timer()
    for i in range(1000):
        collision = check_collision_between_polygons(polygon1, polygon2b)
    toc = timeit.default_timer()
    print "Segment collision time:", toc - tic, "secs"

if __name__ == '__main__':

    main()  # run test
