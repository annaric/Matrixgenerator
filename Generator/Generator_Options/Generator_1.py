import numpy as np
from Generator.Diagonalentries_Generator.Diagonal_Generator import DiagonalGenerator
from Generator.Generator_Options.Generator_5 import Generator5


# Pre-/postmultiply by orthogonal matrices
# Reduce Matrix with Householder transformation
class Generator1:
    def __init__(self, size, density, pos_def, distribution, cond, diagonal_option):
        self.size = size
        self.density = density
        self.pos_def = pos_def
        self.distribution = distribution
        self.cond = cond
        self.diagonal_option = diagonal_option
        self.diagonal_generator = DiagonalGenerator(self.size, self.pos_def, diagonal_option, cond)
        self.matrix = self.diagonal_generator.set_diagonal_entries(np.zeros((self.size, self.size)))

    def generate(self) -> np.ndarray:
        self.premultiply()
        self.post_multiply()
        self.householder()
        return self.matrix

    def premultiply(self):
        generator_5 = Generator5(self.size, self.density, self.pos_def,
                                 self.distribution, self.cond, self.diagonal_option)
        orthogonal_matrix = generator_5.generate()
        self.matrix = np.matmul(orthogonal_matrix, self.matrix)

    def post_multiply(self):
        generator_5 = Generator5(self.size, self.density, self.pos_def,
                                 self.distribution, self.cond, self.diagonal_option)
        orthogonal_matrix = generator_5.generate()
        self.matrix = np.matmul(self.matrix, orthogonal_matrix)

    def householder(self):
        pass
