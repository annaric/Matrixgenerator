import random
import numpy as np
from Generator.Diagonalentries_Generator.Diagonal_Generator import DiagonalGenerator


# Side diagonal matrix generator
class Generator3:

    def __init__(self, size, density, pos_def, distribution, cond, diagonal_option):
        self.size = size
        self.density = density
        self.pos_def = pos_def
        self.distribution = distribution
        self.matrix = np.zeros((self.size, self.size))
        self.distance = random.randint(1, self.size - 1)
        self.positive = 1
        self.cond = cond
        self.diagonal_generator = DiagonalGenerator(self.size, self.pos_def, diagonal_option, cond)

    def generate(self):
        self.set_diagonal()
        for i in range(random.randint(0, 8)):
            self.distance = random.randint(1, self.size - 1)
            self.set_side_diagonal()
        self.matrix = self.diagonal_generator.set_diagonal_entries(self.matrix)
        return self.matrix

    def set_diagonal(self):
        for i in range(self.size - 1):
            self.matrix[i, i] = random.randint(1, 10000) / 10000

    def set_side_diagonal(self):
        for i in range(self.size - self.distance):
            self.matrix[i + self.distance, i] = self.set_random_number()
            self.matrix[i, i + self.distance] = self.set_random_number()

    def set_random_number(self):
        self.set_random_positive()
        number = random.randint(0, 10000)
        # if number != 0:
        number = self.positive * number / 10000
        return number

    def set_random_positive(self):
        rand = random.randint(0, 1)
        if rand == 0:
            self.positive = -1
        else:
            self.positive = 1
