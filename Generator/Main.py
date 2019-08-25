import random

from Generator.Generation_Controller import GenerationController

if __name__ == '__main__':
    size = 2
    # value between 0 and 1
    density = 0.8
    storage_location = "..."
    amount = 1
    pos_def = False
    # Option 1: (0,1) ; Option 2: (-1, 1) ; Option 3: normal
    distribution = 1
    #condition number
    cond = 10000
    # Option 1 to 4
    generation_option = 5
    diagonal_option = 0
    symmetric = False

    controller = GenerationController(size, amount, density, pos_def, distribution, cond,
                                  storage_location, generation_option, diagonal_option, symmetric)
    controller.start_generation()
