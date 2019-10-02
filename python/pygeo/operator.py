import numpy as np
from scipy.sparse import csc_matrix as matrix


class Laplacian:
    def __init__(self, V: np.ndarray, F: np.ndarray):
        self.V = V
        self.F = F
        n = self.V.shape[0]
        self.boundary_cnt = np.zeros(n)

    def weight_for_pair(self, i: int, j: int):
        self.boundary_cnt[i] += 1
        self.boundary_cnt[j] -= 1

    def assign_weight(self, i: int, j: int):

    def build_weight(self):
        n = V.shape[0]
        m = V.shape[1]
        self.weight = matrix((n, n))
        self.weight_sum = matrix((n, n))
        for f in self.F:
            for i in range(m):
                self.assign_weight(f[i], f[(i+1) % 3])

    def build(self):


def weight(V: np.ndarray, F: np.ndarray) -> mat:


def weight():


def laplacian(V: np.ndarray, F: np.ndarray) -> mat:
    n = V.shape[0]
    weight_sum = mat((n, n))

    for f in F:
        for i in f:
