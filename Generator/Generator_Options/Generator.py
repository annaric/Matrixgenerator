import numpy as np


class Generator:
    def __init__(self, size, density, pos_def, distribution):
        self.size = size
        self.density = density
        self.pos_def = pos_def
        self.distribution = distribution
        self.matrix = np.zeros(self.size, self.size)

    def generate(self):
        pass
