import random

from Generator.Generator_Options.Generator_1 import Generator1
from Generator.Generator_Options.Generator_2 import Generator2
from Generator.Generator_Options.Generator_3 import Generator3
from Generator.Generator_Options.Generator_4 import Generator4
from Generator.Generator_Options.Generator_5 import Generator5
from Generator.Generator_Options.Generator_6 import Generator6
from Generator.Generator_Options.Help_Classes.Density_Setter import DensitySetter
from Generator.Diagonalentries_Generator.Diagonal_Generator import DiagonalGenerator

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import det


class GenerationController:

    def __init__(self, size, amount, density, pos_def, distribution, cond, storage_location,
                 generation_option, diagonal_option, symmetric):
        print("Your matrix will be generated, please wait...")
        self.size = size
        # value between 0 and 1
        self.density = density
        self.storage_location = storage_location
        self.amount = amount
        self.pos_def = pos_def
        # Option 1: (0,1) ; Option 2: (-1, 1); Option 3: normal
        self.distribution = distribution
        # Option 1 to 6
        self.generation_option = generation_option
        # boolean
        self.symmetric = symmetric
        self. cond = cond
        self.generator = None
        self.diagonal_option = diagonal_option
        self.matrix = None
        self.density_setter = DensitySetter(self.size, self.density)
        self.diagonal_generator = DiagonalGenerator(self.size, self.pos_def, self.diagonal_option, self.cond)

    def start_generation(self):
        amount = self.amount
        i = 0
        while i < amount:
            self.choose_generator()
            self.matrix = self.generator.generate()
            self.matrix = self.density_setter.set_density(self.matrix)
            self.matrix = self.density_setter.set_density(self.matrix)
            self.matrix = self.diagonal_generator.set_diagonal_entries(self.matrix)
            if self.check_components(i):
                self.save()
                i = i + 1
            else:
                print("not regular matrix was generated")
        print("Finishing matrix generation")

    def choose_generator(self):
        generator = self.generation_option
        if self.generation_option == 0:
            generator = random.randint(1, 6)

        if generator == 1:
            self.generator = Generator1(self.size, self.density, self.pos_def, self.distribution,
                                        self.cond, self.diagonal_option, self.symmetric)
        elif generator == 2:
            self.generator = Generator2(self.size, self.density, self.pos_def, self.distribution,
                                        self.cond, self.diagonal_option, self.symmetric)
        elif generator == 3:
            self.generator = Generator3(self.size, self.density, self.pos_def, self.distribution,
                                        self.cond, self.diagonal_option, self.symmetric)
        elif generator == 4:
            self.generator = Generator4(self.size, self.density, self.pos_def, self.distribution,
                                        self.cond, self.diagonal_option, self.symmetric)
        elif generator == 5:
            self.generator = Generator5(self.size, self.density, self.pos_def, self.distribution,
                                        self.cond, self.diagonal_option, self.symmetric)
        elif generator == 6:
            self.generator = Generator6(self.size, self.density, self.pos_def, self.distribution,
                                        self.cond, self.diagonal_option, self.symmetric)
        else:
            raise Exception("NotImplementedException")

    def save(self):
        # save in hdf5 file
        print(self.matrix)
        self.show_matrix()

    def save2(self):
        # save in hdf5 file
        pass

    def check_components(self, i):
        if self.pos_def:
            if self.check_pos_def():
                return self.check_regularity()
            else:
                print("not positive definite matrix was generated")
                return False
        else:
            return self.check_regularity()

    def check_regularity(self):
        np.seterr(all='ignore')
        if det(self.matrix) != 0:
            return True
        else:
            print("not regular matrix was generated")
            return False

    def check_pos_def(self):
        return np.all(np.linalg.eigvals(self.matrix) > 0)

    def show_matrix(self):
        matrix = self.matrix
        plt.spy(matrix)
        plt.show()
