import numpy as np


# Поиск всех возможных положений фигурок на доске
def create_covered(size, polyominos):
    placements = {}
    counter = 0
    M = size[0]
    N = size[1]
    for p_ind, p in enumerate(polyominos):
        mP, nP = p.shape
        for x in range(M):
            for y in range(N):
                if x + mP <= M:
                    if y + nP <= N:
                        cover = np.zeros((M,N))
                        cover[x:x+mP, y:y+nP] = p
                        placements[counter] = cover
                        counter += 1
    return placements


def create_types(input):
    types = {}
    M = input[0][0]
    N = input[0][1]
    counter = 0
    for polyomino in input[1]:
        shift = len(types)
        if polyomino[0][0] == polyomino[0][1]:
            types = {**types, **{x + shift: counter for x in range((M - polyomino[0][0] + 1) * (N - polyomino[0][1] + 1))}}
            counter += 1
        else:
            types = {**types, **{x + shift: counter for x in range((M - polyomino[0][0] + 1) * (N - polyomino[0][1] + 1))}}
            shift = len(types)
            types = {**types, **{x + shift: counter for x in range((M - polyomino[0][1] + 1) * (N - polyomino[0][0] + 1))}}
            counter += 1
    for polyomino in input[2]:
        shift = len(types)
        types = {**types, **{x + shift: counter for x in range(2 * (M - polyomino[0][0] + 1) * (N - polyomino[0][1] + 1))}}
        shift = len(types)
        types = {**types, **{x + shift: counter for x in range(2 * (M - polyomino[0][1] + 1) * (N - polyomino[0][0] + 1))}}
        counter += 1
    return types

