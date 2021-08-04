from create_polyominoes import create, board_size
from preprocessing import create_covered
from creating_graph import create_graph
from x_algo import solve
from visual import visualize


# Вход алгоритма
input = [(3, 4), [((2, 2), 2)], [((3, 2), 1), ((2, 2), 3)]]

# Обработка входных данных
polyominoes = create(input)
placements = (create_covered(board_size(input), polyominoes))
graph, graph_invert = create_graph(placements, board_size(input))

# Поиск решения
solution = list(solve(graph, graph_invert))

if solution:
    print(True)
else:
    print(False)

# Визуализациия решений
visualize(solution, placements, input[0])



