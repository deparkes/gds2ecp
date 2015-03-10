# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:11:08 2015

@author: Duncan

Convert GDS Boundary type format into a shapely LinearRing

GDS Boundaries are of the format XY: x1,y1, ..., xn, yn
they must be explicitly closed

Shapely LinearRing objects are an ordered sequence of (x,y) tuples 
e.g. ring = LinearRing([(0, 0), (1, 1), (1, 0)])

In this script I'll assume you've already extracted the list of x,y values from
the gds file.

To convert from gds to LinearRing we'll need to go from a single list to a 
list of tuples.

The answers to this question allow us to pick out the coordinate pairs from
the gds boundary list:
http://stackoverflow.com/questions/4628290/pairs-from-single-list

"""

from itertools import izip
from matplotlib import pyplot as plt
from shapely.geometry import LinearRing


def pairwise(t):
    it = iter(t)
    return izip(it,it)

# for "pairs" of any length
def chunkwise(t, size=2):
    it = iter(t)
    return izip(*[it]*size)

# Use a test
gds_test = (0, 0, 30000, 0, 15000, 15000, 5000, 15000, 0, 0)

ring = list(pairwise(gds_test))

print ring

# Not really necessary, but we can also plot this

patch2b = PolygonPatch(u, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
ax.add_patch(patch2b)
