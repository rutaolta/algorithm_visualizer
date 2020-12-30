from copy import deepcopy
import numpy as np

def ispair(nucl1, nucl2):
    pairs = {"A": "U", "U": "A", "G": "C", "C": "G"}
    if pairs[nucl1.upper()] == nucl2.upper():
        return 1
    return 0


class Nussinov:
    def __init__(self, seq):
        self.sequence = seq
        self.history = list()
        self.frame = 0
        self._run()

    def __getitem__(self, item):
        return self.history[item]


    def _run(self):
        n = len(self.sequence)
        matrix = [[0] * n for _ in range(n)]

        for d in range(2, n):
            for i in range(0, n - d):
                j = i + d
                arr = []
                arr.append(matrix[i + 1][j - 1] + ispair(self.sequence[i], self.sequence[j]))
                arr.append(matrix[i + 1][j])
                arr.append(matrix[i][j - 1])
                for k in range(i + 1, j - 1):
                    arr.append(matrix[i][k] + matrix[k + 1][j])
                matrix[i][j] = max(arr)
                self.history.append(matrix)
        return matrix #[0][len(seq) - 1] or 0