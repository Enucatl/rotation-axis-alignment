#!/usr/bin/env python
from __future__ import division, print_function

def progress_bar(percentage):
    return '\r[{0:100s}] {1:.1%}'.format('#'*int((percentage * 100)), percentage)
