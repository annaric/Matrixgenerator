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

    def __init__(self, size, amount, density, pos_def, scale, distribution, cond, storage_location,
                 generation_option, diagonal_option):
        print("Your matrix will be generated, please wait...")
        self.size = size
        # value between 0 and 1
        self.density = density
        self.storage_location = storage_location
        self.amount = amount
        self.pos_def = pos_def
        # Option 1: (0,1) ; Option 2: (-1, 1)
        self.scale = scale
        # uniform or normal
        self.distribution = distribution
        # Option 1 to 6
        self.generation_option = generation_option
        self. cond = cond
        self.generator = None
        self.diagonal_option = diagonal_option
        #self.diagonal_generator = DiagonalGenerator(size, pos_def, scale, diagonal_option, cond)
        self.matrix = None

    def start_generation(self):
        self.choose_generator()
        self.start_generator()

    def choose_generator(self):
        if self.generation_option == 1:
            self.generator = Generator1(self.size, self.density, self.pos_def, self.distribution,
                                        self.cond, self.diagonal_option)
        elif self.generation_option == 2:
            self.generator = Generator2(self.size, self.density, self.pos_def, self.distribution,
                                        self.cond, self.diagonal_option)
        elif self.generation_option == 3:
            self.generator = Generator3(self.size, self.density, self.pos_def, self.distribution,
                                        self.cond, self.diagonal_option)
        elif self.generation_option == 4:
            self.generator = Generator4(self.size, self.density, self.pos_def, self.distribution,
                                        self.cond, self.diagonal_option)
        elif self.generation_option == 5:
            self.generator = Generator5(self.size, self.density, self.pos_def, self.distribution,
                                        self.cond, self.diagonal_option)
        elif self.generation_option == 6:
            self.generator = Generator6(self.size, self.density, self.pos_def, self.distribution,
                                        self.cond, self.diagonal_option)
        else:
            raise Exception("NotImplementedException")

    def start_generator(self):
        amount = self.amount
        i = 0
        while i < amount:
            self.matrix = self.generator.generate()
            #self.matrix = self.diagonal_generator.set_diagonal_entries(self.matrix)
            i = self.check_components(i)
        print("Finishing matrix generation")

    def save(self):
        # save in hdf5 file
        print(self.matrix)
        # scipy greyscale pattern image
        #image = Image.fromarray(self.matrix)
        #matplotlib.pyplot.imshow(self.matrix)

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
