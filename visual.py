import numpy as np


def visualize(solution, placements, size):
    for x in solution:
        matrix = np.zeros(size)
        for i in x:
            matrix += placements[i] * (i + 1)
        print(matrix)
