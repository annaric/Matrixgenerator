import random


class BandwidthReducer:

    def __init__(self, size):
        self.size = size
        self.matrix = None

    def set_upper_bandwidth(self, matrix):
        self.matrix = matrix
        distance = random.randint(1, self.size - 1)
        for i in range(self.size - distance):
            self.set_upper_null_diagonal(distance + i)
        return self.matrix

    def set_lower_bandwidth(self, matrix):
        self.matrix = matrix
        distance = random.randint(1, self.size - 1)
        for i in range(self.size - distance):
            self.set_lower_null_diagonal(distance + i)
        return matrix

    def set_lower_null_diagonal(self, line):
        for i in range(self.size - line):
            self.matrix[i + line, i] = 0

    def set_upper_null_diagonal(self, line):
        for i in range(self.size - line):
            self.matrix[i, i + line] = 0
