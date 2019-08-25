import numpy as np
from numpy.random.mtrand import RandomState


class RandomGenerator:

    def __init__(self):
        self.size = 1
        self.array = None
        self.value = None

    def set_random(self, size, distribution, one_value):
        self.size = size
        if distribution == 0:
            self.uniform(one_value)
        elif distribution == 1:
            self.uniform_negative(one_value)
        elif distribution == 2:
            self.normal_distribution(one_value)
        else:
            raise Exception("NotImplementedException")

        if not one_value:
            return self.array
        else:
            return self.value

    def uniform(self, one_value):
        if not one_value:
            self.array = np.random.uniform(0, 1, self.size)
        else:
            self.value = np.random.uniform(0, 1, 1)

    def uniform_negative(self, one_value):
        if not one_value:
            self.array = np.random.uniform(-1, 1, self.size)
        else:
            self.value = np.random.uniform(-1, 1, 1)

    def normal_distribution(self, one_value):
        dim = self.size
        self.array = RandomState.normal(loc=0.0, scale=1.0, size=dim)
