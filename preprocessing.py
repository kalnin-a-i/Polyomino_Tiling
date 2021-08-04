import numpy as np


# Поиск всех возможных положений фигурок на доске
def create_covered(size, polyominos):
    placements = {}
    counter = 0
    covered = []
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










