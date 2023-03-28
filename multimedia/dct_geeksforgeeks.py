import numpy as np

m, n = 8, 8


def dctTransform(matrix):
    dct = np.zeros((m, n))

    for i in range(m):
        for j in range(n):

            ci = 1 / (m ** 0.5) if i == 0 else (2 / m) ** 0.5
            cj = 1 / (n ** 0.5) if j == 0 else (2 / n) ** 0.5

            sum = 0
            for k in range(m):
                for l in range(n):

                    dct1 = matrix[k][l] * np.cos((2 * k + 1) * i * np.pi / (
                        2 * m)) * np.cos((2 * l + 1) * j * np.pi / (2 * n))
                    sum = sum + dct1

            dct[i][j] = ci * cj * sum

    for i in range(m):
        for j in range(n):
            print(round(dct[i][j], 5), end="\t")
        print()

if __name__ == '__main__':
    matrix = np.ones((m, n)) * 255.0
    dctTransform(matrix)