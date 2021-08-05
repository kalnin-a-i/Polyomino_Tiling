import numpy as np


def create(input):
    polyominoes = []

    # Обработка прямоугольных полиомино
    # первый размер строки второй столбцы
    for polyomino in input[1]:
        if polyomino[0][0] != polyomino[0][1]:
            polyominoes.append(np.ones(polyomino[0]))
            polyominoes.append(np.ones(polyomino[0][::-1]))
        else:
            polyominoes.append(np.ones(polyomino[0]))

    # Обработка L-полиамино
    for polyomino in input[2]:
        # 1 ориентация
        pl = np.zeros((polyomino[0]))
        pl[:, :1] = np.ones(polyomino[0][0]).reshape((pl.shape[0], 1))
        pl[-1::] = np.ones(polyomino[0][1])
        polyominoes.append(np.array(pl))

        # 2 ориентация
        pl = np.zeros((polyomino[0]))
        pl[::, -1::] = np.ones(polyomino[0][0]).reshape((pl.shape[0], 1))
        pl[0] = np.ones(polyomino[0][1])
        polyominoes.append(np.array(pl))

        # 3 ориентация
        pl = np.zeros((polyomino[0][::-1]))
        pl[:, :1] = np.ones(polyomino[0][1]).reshape((pl.shape[0], 1))
        pl[0] = np.ones(polyomino[0][0])
        polyominoes.append(np.array(pl))

        # 4 ориентация
        pl = np.zeros((polyomino[0][::-1]))
        pl[:, -1:] = np.ones(polyomino[0][1]).reshape((pl.shape[0], 1))
        pl[-1] = np.ones(polyomino[0][0])
        polyominoes.append(np.array(pl))

    return polyominoes


def board_size(input):
    return input[0]


def total_number(input):
    total = 0
    for x in input[1]:
        total += x[1]
    for x in input[2]:
        total += x[1]
    return total


def area(input):
    area = 0
    for polyomino in input[1]:
        area += polyomino[0][0] * polyomino[0][1] * polyomino[1]
    for polyomino in input[2]:
        area += (polyomino[0][0] + polyomino[0][1] - 1) * polyomino[1]
    return area


def max_linear_size(input):
    maxi = 0
    for polyomino in input[1] + input[2]:
        if maxi < max(polyomino[0]):
            maxi = max(polyomino[0])
    return maxi


def create_numbers(input):
    numbers = {}
    counter = 0
    for polyomino in input[1] + input[2]:
        numbers[counter] = polyomino[1]
        counter += 1
    return numbers
