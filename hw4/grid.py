#!/usr/bin/env python2
import pylab as pp
import math
import random

def halton_sequence_algorithm(length, base):
    s = []
    for i in range(1, length):
        i_temp = i
        x = 0.0
        f = 1.0 / base
        while(i_temp > 0):
            q = int(i_temp / base)
            r = i_temp % base
            x = x + f*r
            i_temp = q
            f = f/base
        s.append(x)
    return s


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Grid:
    def __init__(self, size, n):
        self.points = []
        self.size = size
        self.n = n
        self.k = int(math.sqrt(self.n))
        self.step = self.size / self.k
        self.offset = self.size / (2 * self.k)

    def plot_grid(self):
        pp.xticks([self.step * i for i in range(self.k + 1)])
        pp.yticks([self.step * i for i in range(self.k + 1)])
        pp.grid()

    def plot_points(self):
        for point in self.points:
            pp.plot(point.x, point.y, "or")

    def plot(self):
        pp.ylim(0.0 - 0.1,1.0 + 0.1)
        pp.xlim(0.0 - 0.1,1.0 + 0.1)
        self.plot_grid()
        self.plot_points()
        pp.show()

    def clear(self):
        self.points = []

    def uniform_random_grid(self):
        """ Will create a random generated point in each cell. """
        for x in range(0,self.k):
            for y in range(0,self.k):
                rand_x = random.uniform(0.0,self.step)
                rand_y = random.uniform(0.0,self.step)
                point = Point(x * self.step + rand_x, \
                y * self.step + + rand_y)
                self.points.append(point)
        """
        Had a difficult time understanding what a uniformly-genereated random
        grid looks like. This is a random grid implementation scrapped due to
        thinking it was not the proper solution to the problem. I kept it to let
        you know that the exercise caused confusion among me and others.
        i = 0
        while(i < self.n):
            x = random.uniform(0.0,self.size)
            y = random.uniform(0.0,self.size)
            point = Point(x, y)
            self.points.append(point)
            i+=1
        """

    def uniform_center_grid(self):
        for x in range(0,self.k):
            for y in range(0,self.k):
                point = Point(x * self.step + self.offset, \
                y * self.step + self.offset)
                self.points.append(point)

    def halton_generated_grid(self, base_1, base_2):
        x_list = halton_sequence_algorithm(self.n, base_1)
        y_list = halton_sequence_algorithm(self.n, base_2)
        for x, y in zip(x_list, y_list):
            point = Point(x,y)
            self.points.append(point)


def main():
    n = 100
    grid = Grid(1.0,n)

    grid.uniform_center_grid()
    grid.plot()
    grid.clear()

    grid.uniform_random_grid()
    grid.plot()
    grid.clear()

    base_1 = 2
    base_2 = 3
    grid.halton_generated_grid(base_1, base_2)
    grid.plot()

if __name__ == '__main__':
    main()  # run test
