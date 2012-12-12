#!/usr/bin/env python
from __future__ import division, print_function

class MinimumFinder(object):
    """
    Find location of the minimum of the Y projection of the 2d histogram"""
    def __init__(self, histogram, y_bin):
        "histogram should be a TH2D"
        super(MinimumFinder, self).__init__()
        self.histogram = histogram.ProjectionY("projectionY", y_bin, y_bin)

    def get_minimum_bin(x_min, x_max):
        self.histogram.SetRange(x_min, x_max)
        return self.histogram.GetMinimumBin()
