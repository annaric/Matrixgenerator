import numpy as np


class DiagonalGenerator4:
    def __init__(self, size, pos_def, scale, cond):
        self.size = size
        self.pos_def = pos_def
        self.scale = scale
        self.cond = cond

    def set_diagonal_entries(self, matrix):
        value = 1
        for i in range(self.size):
            matrix[i, i] = value
            value = value + 1 / self.cond
        return matrix
