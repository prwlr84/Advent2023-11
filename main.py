from input import input_string
from itertools import combinations


def get_points(grid_data):
    points = []
    counter = 0
    for i in range(len(grid_data)):
        for j, elem in enumerate(grid_data[i]):
            if elem == '#':
                points.append([i, j])
                counter += 1

    return points


def expand_grid(base_grid):
    new_grid = []
    for sublist in base_grid:
        new_grid.append(sublist)
        if all(elem == '.' for elem in sublist):
            new_grid.append(sublist.copy())

    transpose_lst = list(map(list, zip(*new_grid)))
    for i in range(len(transpose_lst) - 1, 0, -1):
        if all(elem == '.' for elem in transpose_lst[i]):
            for sublist in new_grid:
                sublist.insert(i + 1, '.')

    return new_grid


grid = expand_grid([list(line) for line in input_string.split('\n')])


def get_dist_sum():
    coordinates = get_points(grid)
    combinations_list = list(combinations(coordinates, 2))

    distances = [abs(c[1][0] - c[0][0]) + abs(c[1][1] - c[0][1]) for c in combinations_list]
    print(sum(distances), len(coordinates))


if __name__ == '__main__':
    get_dist_sum()
