import random
import numpy as np


class DiagonalGenerator1:
    def __init__(self, size, pos_def, cond):
        self.size = size
        self.pos_def = pos_def
        self.cond = cond

    def set_diagonal_entries(self, matrix):
        value = 1 / self.cond
        for i in range(self.size):
            matrix[i, i] = value
        matrix[0, 0] = 1
        return matrix

