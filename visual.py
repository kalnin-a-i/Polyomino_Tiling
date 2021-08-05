import numpy as np


def visualize(solution, placements, size):
    matrix = np.zeros(size)
    for i in solution[0]:
        matrix += placements[i] * (i + 1)
    print(matrix)
