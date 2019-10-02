import numpy as np
import sys
from typing import List


def meshread(filename: str) -> List[np.ndarray]:
    if filename.endswith('.obj'):
        V = []
        F = []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    words = line.split()[1:]
                    V.append([float(w) for w in words])
                elif line.startswith('f '):
                    words = line.split()[1:]
                    wordHeads = [w.split('/')[0] for w in words]
                    # obj vertex index from 1
                    F.append([int(w) - 1 for w in wordHeads])
        print('v: %d, f: %d' % (len(V), len(F)), file=sys.stderr)
        return [np.array(V), np.array(F)]
    else:
        raise NotImplementedError
