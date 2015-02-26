#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
All the constants used in pycmt3d
'''

import scipy

# Mathmatical constants
PI = scipy.pi

# Scale of cmt parameters
# (latitude, longtitude, depth and moment centroid time and half duration)
SCALE_DELTA = 0.0025
SCALE_LOCATION = 0.001      # degree
SCALE_DEPTH = 1.0        # km
SCALE_MOMENT = 1.0e+22   # dyns*cm
SCALE_CTIME = 1.0        # seconds
SCALE_HDUR = 1.0         # seconds

# Maximum number of parameters
NPARMAX = 11

# Maximum npts for records
NDATAMAX = 30000

# Maximum number of records (NRECMAX < NWINMAX)
NRECMAX = 1200

# Maximum number of windows
NWINMAX = 1800

# Number of pars for moment only
NM = 6

# number of pars for moment+location only
NML = 9

# Small numbers
EPS2 = 1.0d-2
EPS5 = 1.0d-5

# Number of regions for azimuthal weighting
NREGIONS = 10

# Reference distance for Pnl, Rayleigh and Love wave weighting
REF_DIST = 100.0

# Earth's radius for depth scaling
R_EARTH=6371  # km