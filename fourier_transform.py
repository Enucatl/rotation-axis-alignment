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
tdrstyle()
graph_canvas_name = "graph_canvas"
graph_canvas = ROOT.TCanvas(
        graph_canvas_name,
        graph_canvas_name)
graph_x.Draw("ap")

histogram = ROOT.TH1D("height_difference",
        "height difference; file_id; height difference #(){pixel}",
        180, 0, 180)
for i in range(int(math.floor(n/2))):
    difference = graph_x.Eval(i) - graph_x.Eval(i + 180)
    histogram.SetBinContent(i + 1, difference)

histogram_canvas_name = "histogram_canvas"
histogram_canvas = ROOT.TCanvas(
        histogram_canvas_name,
        histogram_canvas_name)
histogram.Draw()

graph_y_name = "graph_y"
graph_y = root_file.Get(graph_y_name)
raw_input()
