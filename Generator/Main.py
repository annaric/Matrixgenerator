import random

from Generator.Generation_Controller import GenerationController

if __name__ == '__main__':
    size = 3
    # value between 0 and 1
    density = 0.8
    storage_location = "..."
    amount = 1
    pos_def = True
    # Option 1: (0,1) ; Option 2: (-1, 1)
    scale = 1
    # uniform or normal
    distribution = "uniform"
    #condition number
    cond = 10000
    # Option 1 to 4
    generation_option = 2 #random.randint(1, 4)
    diagonal_option = 1 #random.randint(1, 6)

    controller = GenerationController(size, amount, density, pos_def, scale, distribution, cond,
                                  storage_location, generation_option, diagonal_option)
    controller.start_generation()
