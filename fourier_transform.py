#!/usr/bin/env python
from __future__ import division, print_function
import math
import numpy
from rootstyle import tdrstyle
import argparse
parser = argparse.ArgumentParser(description='''
        Find x alignment with fourier transform.''')
parser.add_argument('file_name', metavar='file',
        nargs='?', help='root files with graph_x made by many_tips.py')

file_name = parser.parse_args().file_name

import ROOT
root_file = ROOT.TFile(file_name)
graph_x_name = "graph_x"
graph_x = root_file.Get(graph_x_name)

n = graph_x.GetN()
a = numpy.empty(n)

y_points = graph_x.GetY()
for i in range(n):
    a[i] = y_points[i]

a = a[:100]
transformed = numpy.fft.fft(a)
for item in transformed:
    print(item)

tdrstyle()
graph_x.Draw("ap")
function = ROOT.TF1("cosine", "[0] + [1] * sin([2] * (x + [3]))", 0, 195)
function.SetParameters(525, 375, math.pi / 180, -122)
function.SetNpx(10000)
graph_x.Fit("cosine")

raw_input()
