import random
import numpy as np
from Generator.Diagonalentries_Generator.Diagonal_Generator import DiagonalGenerator


# Side diagonal matrix generator
from Generator.Generator_Options.Help_Classes.Random_generator import RandomGenerator


class Generator3:

    def __init__(self, size, density, pos_def, distribution, cond, diagonal_option, symmetric):
        self.size = size
        self.density = density
        self.pos_def = pos_def
        self.distribution = distribution
        self.matrix = np.zeros((self.size, self.size))
        self.distance = random.randint(1, self.size - 1)
        self.positive = 1
        self.cond = cond
        self.symmetric = symmetric
        self.diagonal_generator = DiagonalGenerator(self.size, self.pos_def, diagonal_option, cond)
        self.random_generator = RandomGenerator()

    def generate(self) -> np.ndarray:
        self.matrix = self.diagonal_generator.set_diagonal_entries(self.matrix)
        for i in range(random.randint(1, 8)):
            self.distance = random.randint(1, self.size - 1)
            self.set_side_diagonal()
        return self.matrix

    def set_side_diagonal(self):
        for i in range(self.size - self.distance):
            array = self.random_generator.set_random(self.size - self.distance, self.distribution, False)
            array2 = self.random_generator.set_random(self.size - self.distance, self.distribution, False)
            self.matrix[i + self.distance, i] = array[i]
            if self.symmetric:
                self.matrix[i, i + self.distance] = array[i]
            else:
                self.matrix[i, i + self.distance] = array2[i]