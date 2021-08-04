# Создание двудольного графа хранимого в виде двух словарей
def create_graph(placements, size):
    M = size[0]
    N = size[1]
    graph = {}
    graph_invert = {}

    for i in range(M):
        for j in range(N):
            for position in placements.keys():
                if placements[position][i][j] == 1:
                    if (i, j) not in graph:
                        graph[(i, j)] = set()
                    if position not in graph_invert:
                        graph_invert[position] = []
                    graph[(i, j)].add(position)
                    graph_invert[position].append((i, j))
    return graph, graph_invert
