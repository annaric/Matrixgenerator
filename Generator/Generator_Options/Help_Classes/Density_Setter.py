import random


class DensitySetter:

    def __init__(self, size, density):
        self.size = size
        self.density = density
        self.given_density = 0

    def set_density(self, matrix):
        number = round(self.density * self.size * self.size)
        for i in range(number):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            matrix[x, y] = 0
        return matrix
