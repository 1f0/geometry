from __future__ import print_function
from paraview.simple import *
import sys

if(len(sys.argv) < 2):
    print('# Visualize vector field')
    print('Usage: ', sys.argv[0], 'input.vtk')
    sys.exit(1)

LegacyVTKReader(sys.argv[1])
Render()
Interact()
