from nussinov import ispair


class Traceback:
    def __init__(self, seq, DP):
        self.sequence = seq
        self.min_loop_length = 1
        self.structure = []
        self.DP = DP

    def fill_structure(self, i, j):
        if j <= i:
            return
        elif self.DP[i][j] == self.DP[i][j - 1]:
            self.fill_structure(i, j - 1)
        else:
            for k in [b for b in range(i, j - self.min_loop_length) if ispair(self.sequence[b], self.sequence[j])]:
                if k - 1 < 0:
                    if self.DP[i][j] == self.DP[k + 1][j - 1] + 1:
                        self.structure.append((k, j))
                        self.fill_structure(k + 1, j - 1)
                        break
                elif self.DP[i][j] == self.DP[i][k - 1] + self.DP[k + 1][j - 1] + 1:
                    self.structure.append((k, j))
                    self.fill_structure(i, k - 1)
                    self.fill_structure(k + 1, j - 1)
                    break

    def write_structure(self):
        dot_bracket = ["." for _ in range(len(self.sequence))]
        for s in self.structure:
            dot_bracket[min(s)] = "("
            dot_bracket[max(s)] = ")"
        return "".join(dot_bracket)

    def run(self):
        self.fill_structure(0, len(self.sequence) - 1)
        # self.structure = self.write_structure()
        return self.write_structure()#self.structure
