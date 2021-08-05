from create_polyominoes import create, board_size, total_number, area, max_linear_size, create_numbers
from preprocessing import create_covered, create_types
from creating_graph import create_graph
from x_algo import solve
from visual import visualize


def main(input):
    # Проверим, что суммарная площадь полиомино не превосходит площадь поля и максимальный линейный размер полиомино не больше самой длинной стороны поля
    if area(input) > input[0][0] * input[0][1]:
        return False
    if max_linear_size(input) > max(input[0]):
        return False

    # Если с площадью и максимальным линейным размером все хорошо то запускаем алгоритм
    # Обработка входных данных
    polyominoes = create(input)
    placements = (create_covered(board_size(input), polyominoes))
    graph, graph_invert = create_graph(placements, board_size(input))
    #print(placements)

    # Поиск решения
    types = create_types(input)
    #print(types)
    numbers = create_numbers(input)
    #print(numbers)

    # Отладочные принты
    #print(graph)
    #print(graph_invert)


    solution = list(solve(graph, graph_invert, total_number(input), types, numbers))

    # Визуализациия решений
    #visualize(solution, placements, input[0])

    if solution:
        return(True)
    else:
        return(False)


# Тесты
inputs_true = [[(2, 3), [], [((2, 2), 1)]],
               [(2, 3), [((2, 2), 1), ((2, 1), 1)], []],
               [(2, 3), [], [((2, 2), 2)]],
               [(2, 3), [((2, 2), 1)], []],
               [(3, 5), [((2, 2), 1)], [((2, 2), 2), ((2, 3), 1)]],
               [(5, 5), [], [((3, 3), 1), ((2, 3), 5)]]]

for i in range(len(inputs_true)):
    if main(inputs_true[i]):
        print('OK')
    else:
        print(f'FAIL {i+1}')

inputs_false = [[(2, 3), [((2, 2), 2)], []],
                [(2, 3), [((2, 2), 1)], [((2, 2), 1)]],
                [(2, 3), [], [((4, 2), 1)]],
                [(2, 3), [], [((4, 2), 1)]],
                [(4, 3), [((4, 2), 1)], [((3, 2), 1)]]]

for i in range(len(inputs_false)):
    if not main(inputs_false[i]):
        print('OK')
    else:
        print(f'FAIL {i+1}')
