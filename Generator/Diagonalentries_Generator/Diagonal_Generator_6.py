import random
import numpy as np


class DiagonalGenerator6:
    def __init__(self, size, pos_def, scale, cond):
        self.size = size
        self.pos_def = pos_def
        self.scale = scale
        self.cond = cond

    def set_diagonal_entries(self, matrix):
        for i in range(self.size):
            matrix[i, i] = random.randint(1, self.cond) / self.cond
        return matrix
