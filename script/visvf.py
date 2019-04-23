from __future__ import print_function
from paraview.simple import *
import sys

if(len(sys.argv) < 2):
    print('# Visualize vector field')
    print('Usage: ', sys.argv[0], 'input.vtk')
    sys.exit(1)


reader = LegacyVTKReader(FileNames=sys.argv[1])
Show(reader)

glyph = Glyph(Input=reader)
Show(glyph)

SetViewProperties(ViewSize=[512, 512])

Render()
Interact()
