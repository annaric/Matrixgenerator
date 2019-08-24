import numpy as np
from Generator.Diagonalentries_Generator.Diagonal_Generator import DiagonalGenerator
from Generator.Generator_Options.Generator_5 import Generator5


# Pre-/postmultiply by orthogonal matrices
# Reduce Matrix with Householder transformation
class Generator1:
    def __init__(self, size, density, pos_def, scale, distribution, cond, diagonal_option):
        self.size = size
        self.density = density
        self.pos_def = pos_def
        self.scale = scale
        self.distribution = distribution
        self.cond = cond
        self.diagonal_option = diagonal_option
        self.diagonal_generator = DiagonalGenerator(self.size, self.pos_def, self.scale, diagonal_option, cond)
        self.matrix = self.diagonal_generator.set_diagonal_entries(self.matrix)

    def generate(self):
        self.premultiply()
        self.post_multiply()
        self.householder()

    def premultiply(self):
        generator_5 = Generator5(self.size, self.density, self.pos_def, self.scale,
                               self.distribution, self.cond, self.diagonal_option)
        orthogonal_matrix = generator_5.generate()
        self.matrix = np.matmul(orthogonal_matrix, self.matrix)

    def post_multiply(self):
        generator_5 = Generator5(self.size, self.density, self.pos_def, self.scale,
                                 self.distribution, self.cond, self.diagonal_option)
        orthogonal_matrix = generator_5.generate()
        self.matrix = np.matmul(self.matrix, orthogonal_matrix)

    def householder(self):
        pass
