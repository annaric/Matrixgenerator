import numpy as np


class DiagonalGenerator2:
    def __init__(self, size, pos_def, cond):
        self.size = size
        self.pos_def = pos_def
        self.cond = cond

    def set_diagonal_entries(self, matrix):
        for i in range(self.size):
            matrix[i, i] = 1
        matrix[self.size - 1, self.size - 1] = 1 / self.cond
        return matrix
