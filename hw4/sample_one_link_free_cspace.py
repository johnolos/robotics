#!/usr/bin/env python2
"""
ME/ECE 179P, Homework #4
This module gives a sketch of the one-link robot collision test
for exercise 4.7
"""
import math
from geometry import get_distance_to_segment

def main():
    """
    Computes the free configuration space for a one link manipulator.
    """
    # The link is modeled as a rectangle with semi-circles attached to the
    # ends, meaning it is specified by a length and a radius.
    link1_length = 1.0
    link1_radius = 0.1

    # The link is attached to a base at (0,0).
    arm_base = (0, 0)

    # To simplify the checks for collisions, the only obstacle in
    # the workspace is a circle specified by a center and a radius.
    circle_center = (0.5, 0.5)
    circle_radius = 0.2

    # making a number of sampels between -pi and pi
    num_samples = 100
    step_size = 2 * math.pi / num_samples
    obstacle_configs = list()

    for i in range(num_samples):
        angle = -math.pi + (i * step_size)
        # The segment describing the link is defined by two points, armBase
        # and end_point.
        end_point = (arm_base[0] + link1_length * math.cos(angle), \
            arm_base[1] + link1_length * math.sin(angle))

        # To check that the link is not hitting the circle at this
        # angle, it suffices to check that the distance
        # between the center of the circular obstacle and the segement
        # defining the link is greater than the sum of the radii.
        if get_distance_to_segment(circle_center, arm_base, end_point) < \
           link1_radius + circle_radius:
            obstacle_configs.append(angle)

    # print the configurations that correspond to a collision with the obstacle
    print obstacle_configs

if __name__ == '__main__':

    main()  # determine the free configuration space
