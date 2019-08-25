import numpy as np
from Generator.Diagonalentries_Generator.Diagonal_Generator import DiagonalGenerator
from Generator.Generator_Options.Generator_5 import Generator5
from Generator.Generator_Options.Help_Classes.Bandwith_reducer import BandwidthReducer
from Generator.Generator_Options.Help_Classes.Householder_transformation import HouseholderTransformation


# Pre-/postmultiply by orthogonal matrices
# Reduce Matrix with Householder transformation
class Generator1:
    def __init__(self, size, density, pos_def, distribution, cond, diagonal_option, symmetric):
        self.size = size
        self.density = density
        self.pos_def = pos_def
        self.distribution = distribution
        self.cond = cond
        self.diagonal_option = diagonal_option
        self.symmetric = symmetric
        self.diagonal_generator = DiagonalGenerator(self.size, self.pos_def, diagonal_option, cond)
        self.matrix = self.diagonal_generator.set_diagonal_entries(np.zeros((self.size, self.size)))
        self.orthogonal_matrix = None
        self.householder = HouseholderTransformation(self.size)
        self.bandwidth_reducer = BandwidthReducer(self.size)

    def generate(self) -> np.ndarray:
        self.premultiply()
        self.post_multiply()
        #self.bandwidth_transform()
        self.matrix = self.bandwidth_reducer.set_lower_bandwidth(self.matrix)
        self.matrix = self.bandwidth_reducer.set_upper_bandwidth(self.matrix)

        return self.matrix

    def premultiply(self):
        generator_5 = Generator5(self.size, self.density, self.pos_def,
                                 self.distribution, self.cond, self.diagonal_option, self.symmetric)
        self.orthogonal_matrix = generator_5.generate()
        self.matrix = np.matmul(self.orthogonal_matrix, self.matrix)

    def post_multiply(self):
        if self.symmetric:
            self.matrix = np.matmul(np.transpose(self.orthogonal_matrix), self.matrix)
        else:
            generator_5 = Generator5(self.size, self.density, self.pos_def,
                                     self.distribution, self.cond, self.diagonal_option, self.symmetric)
            orthogonal_matrix = generator_5.generate()
            self.matrix = np.matmul(self.matrix, orthogonal_matrix)

    def bandwidth_transform(self):
        bandwidth = self.size
        elimination_number = 5
        block_size = 1
        self.matrix = self.householder.transform(self.matrix, bandwidth, elimination_number, block_size)


