import random

from Generator.Diagonalentries_Generator.Diagonal_Generator_1 import DiagonalGenerator1
from Generator.Diagonalentries_Generator.Diagonal_Generator_2 import DiagonalGenerator2
from Generator.Diagonalentries_Generator.Diagonal_Generator_3 import DiagonalGenerator3
from Generator.Diagonalentries_Generator.Diagonal_Generator_4 import DiagonalGenerator4
from Generator.Diagonalentries_Generator.Diagonal_Generator_5 import DiagonalGenerator5
from Generator.Diagonalentries_Generator.Diagonal_Generator_6 import DiagonalGenerator6


class DiagonalGenerator:
    def __init__(self, size, pos_def, scale, diagonal_option, cond):
        self.size = size
        self.pos_def = pos_def
        self.scale = scale
        self.diagonal_option = diagonal_option
        self.cond = cond
        self.diagonal_generator = None

    def set_diagonal_entries(self, matrix):
        if self.diagonal_option == 0:
            self.diagonal_option = random.randint(1, 6)

        if self.diagonal_option == 1:
            self.diagonal_generator = DiagonalGenerator1(self.size, self.pos_def, self.scale, self.cond)
        elif self.diagonal_option == 2:
            self.diagonal_generator = DiagonalGenerator2(self.size, self.pos_def, self.scale, self.cond)
        elif self.diagonal_option == 3:
            self.diagonal_generator = DiagonalGenerator3(self.size, self.pos_def, self.scale, self.cond)
        elif self.diagonal_option == 4:
            self.diagonal_generator = DiagonalGenerator4(self.size, self.pos_def, self.scale, self.cond)
        elif self.diagonal_option == 5:
            self.diagonal_generator = DiagonalGenerator5(self.size, self.pos_def, self.scale, self.cond)
        elif self.diagonal_option == 6:
            self.diagonal_generator = DiagonalGenerator6(self.size, self.pos_def, self.scale, self.cond)
        else:
            raise Exception("NotImplementedException")

        matrix = self.diagonal_generator.set_diagonal_entries(matrix)
        return matrix
