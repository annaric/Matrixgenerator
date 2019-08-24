import numpy as np
import random
from Generator.Diagonalentries_Generator.Diagonal_Generator import DiagonalGenerator


# implements orthogonal matrix
class Generator6:

    def __init__(self, size, density, pos_def, distribution, cond, diagonal_option):
        self.size = size
        self.density = density
        self.pos_def = pos_def
        self.distribution = distribution
        self.diagonal_option = diagonal_option
        self.diagonal_generator = DiagonalGenerator(self.size, self.pos_def, self.diagonal_option, cond)
        self.matrix = np.zeros((self.size, self.size))

    def generate(self):
        self.matrix = self.diagonal_generator.set_diagonal_entries(self.matrix)
        for i in range(random.randint(1, 10)):
            help_matrix = np.random.random((self.size, self.size))
            self.matrix = np.matmul(help_matrix, self.matrix)
            help_matrix = np.linalg.inv(help_matrix)
            self.matrix = np.matmul(self.matrix, help_matrix)
        return self.matrix

