from pygeo import meshread
from pygeo import meshshow
import sys

if len(sys.argv) > 1:
    V, F = meshread(sys.argv[1])
    meshshow(V, F)
