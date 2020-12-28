def ispair(nucl1, nucl2):
    pairs = {"A": "U", "U": "A", "G": "C", "C": "G"}
    if pairs[nucl1] == nucl2:
        return 1
    return 0


def nussinov(seq):
    n = len(seq)
    matrix = [[0] * n for _ in range(n)]

    for d in range(2, n):
        for i in range(0, n - d):
            j = i + d
            arr = []
            arr.append(matrix[i + 1][j - 1] + ispair(seq[i], seq[j]))
            arr.append(matrix[i + 1][j])
            arr.append(matrix[i][j - 1])
            for k in range(i + 1, j - 1):
                arr.append(matrix[i][k] + matrix[k + 1][j])
            matrix[i][j] = max(arr)
    return matrix #[0][len(seq) - 1] or 0