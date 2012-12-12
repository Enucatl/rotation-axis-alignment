#!/usr/bin/env python
from __future__ import division, print_function
import numpy
from skimage import io, transform
from readimage import skimage_reader
from readimage.skimage_reader import fromfile

class TipFinder(object):
    """
    Find location of the tip of the wire"""
    def __init__(self, file_name):
        super(MinimumFinder, self).__init__()
        self.image = fromfile(file_name)

    def get_wire_tip_coordinates():
        "this should actually find the tip with the harris algorithm"
        y, x = numpy.transpose(feature.harris(image, min_distance=100,
            threshold=0.3, gaussian_deviation=5))
        if len(x) != 1:
            print("WARNING:", len(x), "tips found!")
        x, y = x[0], y[0]
        return x, y

if __name__ == '__main__':
    import sys
    image = TipFinder(sys.argv[1])
    print(image.get_wire_tip_coordinates())
