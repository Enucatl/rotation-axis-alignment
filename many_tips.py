#!/usr/bin/env python
from __future__ import division, print_function
from progress_bar import progress_bar
from tip_finder import TipFinder
from array import array
import argparse
parser = argparse.ArgumentParser(description='''
        Plot x position of the tip (TipFinder) for all the files 
        given as input.''')
parser.add_argument('file_names', metavar='FILES',
        nargs='+', help='raw files to be analyzed')

file_names = parser.parse_args().file_names

x_positions = array("d", [])
y_positions = array("d", [])
image_ids = array("d", [])
n = len(file_names)

for i, file_name in enumerate(file_names):
    print(progress_bar(i/n), end='')
    t = TipFinder(file_name)
    x, y, m = t.get_wire_tip_coordinates()
    if m != 1: continue
    x_positions.append(x)
    y_positions.append(y)
    #print(x, y)
    "get image_id from file_name: tipically ccdimage_00006_00070_00.raw"
    image_id = int(file_name.split("_")[3])
    image_ids.append(image_id)

n = len(image_ids)
print(progress_bar(1), end='')
print()
import ROOT
from rootstyle import tdrstyle
tdrstyle()
graph_x = ROOT.TGraph(n, image_ids, x_positions)
graph_x.SetTitle("x position;file number;x #(){pixel}")
graph_y = ROOT.TGraph(n, image_ids, y_positions)
graph_y.SetTitle("y position;file number;y #(){pixel}")

canvas_name = "canvas"
canvas = ROOT.TCanvas(canvas_name, canvas_name)
canvas.Divide(2, 1)
canvas.cd(1)
graph_x.Draw("ap")
canvas.cd(2)
graph_y.Draw("ap")
root_file_name = "positions.root"
root_file = ROOT.TFile(root_file_name, "recreate")
root_file.cd()
graph_x.Write("graph_x")
graph_y.Write("graph_y")
root_file.Close()
raw_input()
