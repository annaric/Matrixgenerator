import random
import numpy as np
from Generator.Generator_Options.Help_Classes.Density_Setter import DensitySetter
from Generator.Generator_Options.Help_Classes.Bandwith_reducer import BandwidthReducer
from Generator.Diagonalentries_Generator.Diagonal_Generator import DiagonalGenerator


# Total random entries generator
# (optional) pre/postmultiply by diagonalmatrices
# (optional) Permute rows/colums
# (optional) set density
# (optional) Reducing upper and(/or) lower bandwith -> and: band matrix?

class Generator4:
    def __init__(self, size, density, pos_def, distribution, cond, diagonal_option):
        self.size = size
        self.density = density
        self.pos_def = pos_def
        self.distribution = distribution
        self.matrix = np.random.random((self.size, self.size))
        self.density_setter = DensitySetter(self.size, self.density)
        self.bandwidth_reducer = BandwidthReducer(self.size)
        cond = random.randint(1, 100)
        self.diagonal_generator = DiagonalGenerator(self.size, self.pos_def, diagonal_option, cond)

    def generate(self):
        # (optional) pre-/postmultiply by diagonalmatrices
        rand = random.randint(0, 2)
        if rand == 0:
            self.premultiply()
        elif rand == 1:
            self.post_multiply()
        # (optional) Permute rows/columns
        rand = random.randint(0, 2)
        if rand == 0:
            self.permute_columns()
        elif rand == 1:
            self.permute_rows()
        # (optional) set density
        rand = random.randint(0, 1)
        if rand == 0:
            self.matrix = self.density_setter.set_density(self.matrix)
        # (optional) Reducing upper and(/or) lower bandwidth -> and: band matrix?
        rand = random.randint(0, 2)
        if rand == 0:
            self.matrix = self.bandwidth_reducer.set_lower_bandwidth(self.matrix)
        elif rand == 1:
            self.matrix = self.bandwidth_reducer.set_upper_bandwidth(self.matrix)

        self.matrix = self.diagonal_generator.set_diagonal_entries(self.matrix)
        return self.matrix

    def premultiply(self):
        mult_matrix = np.zeros(self.size, self.size)
        self.diagonal_generator.set_diagonal_entries(mult_matrix)
        self.matrix = np.matmul(mult_matrix, self.matrix)

    def post_multiply(self):
        mult_matrix = np.zeros(self.size, self.size)
        self.diagonal_generator.set_diagonal_entries(mult_matrix)
        self.matrix = np.matmul(self.matrix, mult_matrix)

    def permute_rows(self):
        np.random.shuffle(self.matrix)

    def permute_columns(self):
        np.transpose(np.random.shuffle(np.transpose(self.matrix)))

    def generate_diagonal_matrix(self):
        cond = random.randint(0, 100)
        diagonal_generator = DiagonalGenerator(self.size, True, True, 0, cond)
        matrix = np
        matrix = diagonal_generator.set_diagonal_entries(matrix)
        return matrix
