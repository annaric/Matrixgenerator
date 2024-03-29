import random

import numpy as np
from Generator.Generator_Options.Help_Classes.Density_Setter import DensitySetter
from Generator.Generator_Options.Help_Classes.Bandwith_reducer import BandwidthReducer
from Generator.Diagonalentries_Generator.Diagonal_Generator import DiagonalGenerator
from Generator.Generator_Options.Help_Classes.Random_generator import RandomGenerator


# (optional?) Fill upper/lower Triangle
# (optional) Pre/Postmultiply with S and S -1
# (optional) Reducing upper OR lower bandwidth
# (optional) set density

class Generator2:
    def __init__(self, size, density, pos_def, distribution, cond, diagonal_option, symmetric):
        self.size = size
        self.density = density
        self.pos_def = pos_def
        self.distribution = distribution
        self.density_setter = DensitySetter(self.size, self.density)
        self.bandwidth_reducer = BandwidthReducer(self.size)
        self.cond = cond
        self.symmetric = symmetric
        self.diagonal_generator = DiagonalGenerator(self.size, True, diagonal_option, 20)
        self.matrix = np.zeros((self.size, self.size))
        self.s_matrix = np.random.random((self.size, self.size)) #np.zeros((self.size, self.size))
        self.generate_s()
        self.random_generator = RandomGenerator()

    def generate(self) -> np.ndarray:
        self.matrix = self.diagonal_generator.set_diagonal_entries(self.matrix)
        # Fill upper/lower Triangle
        rand = random.randint(0, 2)
        if rand == 0:
            self.fill_lower_triangle()
        elif rand == 1:
            self.fill_upper_triangle()

        # Pre-/postmultiply with S and S -1
        rand = random.randint(0, 1)
        if rand == 0:
            self.premultiply()
            self.post_multiply()

        # Reducing upper OR lower bandwidth
        rand = random.randint(0, 2)
        if rand == 0:
            self.matrix = self.bandwidth_reducer.set_lower_bandwidth(self.matrix)
        elif rand == 1:
            self.matrix = self.bandwidth_reducer.set_upper_bandwidth(self.matrix)

        # set density
        rand = 0 #random.randint(0, 1)
        if rand == 0:
            self.matrix = self.density_setter.set_density(self.matrix)
        return self.matrix

    def fill_upper_triangle(self):
        distance = 1
        for i in range(self.size - 1):
            array = self.random_generator.set_random(self.size - distance, self.distribution, False)
            for j in range(self.size - distance):
                self.matrix[j, j + distance] = array[j]
                # random.randint(0, 1000)/1000
            distance = distance + 1

    def fill_lower_triangle(self):
        distance = 1
        for i in range(self.size - 1):
            array = self.random_generator.set_random(self.size - distance, self.distribution, False)
            for j in range(self.size - distance):
                self.matrix[j + distance, j] = array[j]
                # random.randint(0, 1000) / 1000
            distance = distance + 1

    def premultiply(self):
        self.generate_s()
        self.diagonal_generator.set_diagonal_entries(self.s_matrix)
        self.matrix = np.matmul(self.s_matrix, self.matrix)

    def post_multiply(self):
        s_inv_matrix = np.linalg.inv(self.s_matrix)
        self.diagonal_generator.set_diagonal_entries(s_inv_matrix)
        self.matrix = np.matmul(self.matrix, s_inv_matrix)

    def generate_s(self):
        matrix = np.random.random((self.size, self.size))
        self.diagonal_generator = DiagonalGenerator(self.size, True, random.randint(1, 6), 20)
        self.s_matrix = self.diagonal_generator.set_diagonal_entries(matrix)
