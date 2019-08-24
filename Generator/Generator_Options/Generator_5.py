import numpy as np
from Generator.Diagonalentries_Generator.Diagonal_Generator import DiagonalGenerator


# implements orthogonal matrix
class Generator5:

    def __init__(self, size, density, pos_def, distribution, cond, diagonal_option):
        self.size = size
        self.density = density
        self.pos_def = pos_def
        self.distribution = distribution
        self.diagonal_generator = DiagonalGenerator(self.size, self.pos_def, diagonal_option, cond)

    def generate(self):
        dim = self.size
        random_state = np.random
        h = np.eye(dim)
        d = np.ones((dim,))
        for n in range(1, dim):
            x = random_state.normal(size=(dim - n + 1,))
            d[n - 1] = np.sign(x[0])
            x[0] -= d[n - 1] * np.sqrt((x * x).sum())
            # Householder transformation
            hx = (np.eye(dim - n + 1) - 2. * np.outer(x, x) / (x * x).sum())
            mat = np.eye(dim)
            mat[n - 1:, n - 1:] = hx
            h = np.dot(h, mat)
            # Fix the last sign such that the determinant is 1
        d[-1] = (-1) ** (1 - (dim % 2)) * d.prod()
        # Equivalent to np.dot(np.diag(d), h) but faster, apparently
        h = (d * h.T).T
        return h

