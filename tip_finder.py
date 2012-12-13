#!/usr/bin/env python
from __future__ import division, print_function
import numpy
from skimage import io, feature
from readimages.skimage_reader import fromfile

class TipFinder(object):
    """
    Find location of the tip of the wire"""
    def __init__(self, file_name):
        super(TipFinder, self).__init__()
        self.image = fromfile(file_name)

    def get_wire_tip_coordinates(self):
        "this should actually find the tip with the harris algorithm"
        y, x = numpy.transpose(feature.harris(self.image,
            min_distance=100,
            threshold=0.3,
            gaussian_deviation=5))
        x, y = x[0], y[0]
        n = x.size
        if n != 1:
            print("WARNING:", len(x), "tips found!")
        return x, y, n

if __name__ == '__main__':
    import sys
    finder = TipFinder(sys.argv[1])
    print(finder.get_wire_tip_coordinates())
