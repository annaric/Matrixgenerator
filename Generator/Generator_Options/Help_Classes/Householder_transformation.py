import numpy as np


class HouseholderTransformation:

    def __init__(self, size):
        self.size = size

    def transform(self, matrix, bandwidth, elimination_number, block_size):
        b = bandwidth - elimination_number
        j = 1
        matrix_b = None
        while j < self.size - b - 1:
            j_1 = j
            j_2 = j_1 + block_size
            i_1 = j + b
            i_2 = min(j + b + block_size - 1, self.size)
            while i_1 < self.size:
                #QR
                matrix_b = matrix[i_1:i_2, j_1:j_2].copy()
                q, r = np.linalg.qr(matrix_b)
                q = np.unwrap(q)
                r = np.unwrap(r)
                matrix_b = self.edit_r(r)
                matrix[i_1:i_2 + 1, j_1:j_2] = matrix_b
                # Pre
                matrix_b = matrix[i_1:i_2, j_2 + 1: i_1 - 1].copy()
                matrix_b = np.matmul(np.transpose(q), matrix_b)
                matrix[i_1:i_2, j_2 + 1: i_1 - 1] = matrix_b
                # Sym
                matrix_b = matrix[i_1:i_2, i_1:i_2].copy()
                matrix_b = np.matmul(np.transpose(q), matrix_b, q)
                matrix[i_1:i_2, i_1:i_2] = matrix_b
                # post
                matrix_b = matrix[i_2 + 1:min(i_2 + bandwidth, self.size), i_1:i_2].copy()
                matrix_b = np.matmul(matrix_b, q)
                matrix[i_2 + 1:min(i_2 + bandwidth, self.size), i_1:i_2] = matrix_b

                j_1 = i_1
                j_2 = j_1 + block_size - 1
                i_1 = i_1 + bandwidth
                i_2 = min(i_2 + bandwidth, self.size)
            j = j + block_size
        return matrix_b

    def edit_r(self, matrix_r):
        size = np.size(matrix_r)
        help_matrix = np.eye(size + 1)
        help_matrix2 = help_matrix[0: size + 1, 0: size]
        matrix_r = np.matmul(help_matrix2, matrix_r)
        return matrix_r

