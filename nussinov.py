# from copy import deepcopy
import numpy as np


def ispair(nucl1, nucl2):
    pairs = {"A": "U", "U": "A", "G": "C", "C": "G"}
    if pairs[nucl1] == nucl2:
        return 1
    return 0


class Nussinov:
    def __init__(self, seq):
        self.sequence = seq
        self.history = list()
        self.frame = 0
        self.min_loop_length = 1
        self._run()

    def __getitem__(self, item):
        return self.history[item]

    def get_last(self):
        return self.data[len(self.data.history) - 1]

    def get_first(self):
        return self.data[0]

    def initialize(self, N):
        DP = np.empty((N, N))
        DP[:] = np.NAN
        for k in range(0, self.min_loop_length):
            for i in range(N - k):
                j = i + k
                DP[i][j] = 0
        return DP

    def OPT(self, i, j):
        if i >= j - self.min_loop_length:
            return 0
        else:
            unpaired = self.OPT(i, j - 1)

            pairing = [1 + self.OPT(i, t - 1) + self.OPT(t + 1, j - 1) for t in range(i, j - self.min_loop_length) \
                       if ispair(self.sequence[t], self.sequence[j])]
            if not pairing:
                pairing = [0]
            paired = max(pairing)

            return max(unpaired, paired)

    def _run(self):
        N = len(self.sequence)
        DP = self.initialize(N)
        # structure = []

        for k in range(self.min_loop_length, N):
            for i in range(N - k):
                j = i + k
                DP[i][j] = self.OPT(i, j)

        for i in range(N):
            for j in range(0, i):
                DP[i][j] = DP[j][i]
                self.history.append(DP)
        return DP
        # n = len(self.sequence)
        # matrix = [[0] * n for _ in range(n)]
        #
        # for d in range(2, n):
        #     for i in range(0, n - d):
        #         j = i + d
        #         arr = []
        #         arr.append(matrix[i + 1][j - 1] + ispair(self.sequence[i], self.sequence[j]))
        #         arr.append(matrix[i + 1][j])
        #         arr.append(matrix[i][j - 1])
        #         for k in range(i + 1, j - 1):
        #             arr.append(matrix[i][k] + matrix[k + 1][j])
        #         matrix[i][j] = max(arr)
        #         self.history.append(matrix)
        # return matrix #[0][len(seq) - 1] or 0