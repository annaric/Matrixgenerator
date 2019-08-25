import random

import matplotlib as matplotlib
import scipy as scip
from Generator.Generator_Options.Generator_1 import Generator1
from Generator.Generator_Options.Generator_2 import Generator2
from Generator.Generator_Options.Generator_3 import Generator3
from Generator.Generator_Options.Generator_4 import Generator4
from Generator.Generator_Options.Generator_5 import Generator5
from Generator.Generator_Options.Generator_6 import Generator6
from Generator.Diagonalentries_Generator.Diagonal_Generator import DiagonalGenerator
import numpy as np
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
        #boolean
        self.symmetric = symmetric
        self. cond = cond
        self.generator = None
        self.diagonal_option = diagonal_option
        # self.diagonal_generator = DiagonalGenerator(size, pos_def, scale, diagonal_option, cond)
        self.matrix = None

    def start_generation(self):
        amount = self.amount
        i = 0
        while i < amount:
            self.choose_generator()
            self.matrix = self.generator.generate()
            i = self.check_components(i)
        print("Finishing matrix generation")

    def choose_generator(self):
        generator = self.generation_option
        if self.generation_option == 0:
            generator = random.randint(1, 6)
        print(generator)

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

    def start_generator(self):
           pass # self.matrix = self.diagonal_generator.set_diagonal_entries(self.matrix)

    def save(self):
        # save in hdf5 file
        print(self.matrix)
        # scipy greyscale pattern image
        # image = Image.fromarray(self.matrix)
        # matplotlib.pyplot.imshow(self.matrix)

    def save2(self):
        # save in hdf5 file
        pass

    def check_components(self, i):
        if self.pos_def:
            if self.check_pos_def():
                i = self.check_regularity(i)
        else:
            i = self.check_regularity(i)
        return i

    def check_regularity(self, i):
        np.seterr(all='ignore')
        if det(self.matrix) != 0:
            self.save()
            i = i + 1
        else:
            print("not regular matrix was generated")
        return i

    def check_pos_def(self):
        value = True
        #value = np.all(np.linalg.eigvals(self.matrix) > 0)
        return value
