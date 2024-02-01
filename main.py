from input import input_string
from itertools import combinations


def get_coordinates(grid_data):
    points = []
    counter = 0
    for i in range(len(grid_data)):
        for j, elem in enumerate(grid_data[i]):
            if elem == '#':
                points.append([i, j])
                counter += 1

    return points


def expand_grid(base_grid):
    x = []
    y = []
    new_grid = []
    for i, sublist in enumerate(base_grid):
        new_grid.append(sublist)
        if all(elem == '.' for elem in sublist):
            new_grid.append(sublist.copy())
            y.append(i)

    transpose_lst = list(map(list, zip(*new_grid)))
    for j in range(len(transpose_lst) - 1, 0, -1):
        if all(elem == '.' for elem in transpose_lst[j]):
            x.append(j)
            for sublist in new_grid:
                sublist.insert(j + 1, '.')

    return new_grid, [y, x[::-1]]


grid, expanding_positions = expand_grid([list(line) for line in input_string.split('\n')])


def adjust_coordinates(coordinates):
    x = coordinates[0]
    y = coordinates[1]

    for t in list(enumerate(expanding_positions[0])):
        if x <= t[1]:
            x = t[0] * 9 + x
            break
        elif x > expanding_positions[0][-1]:
            x = len(expanding_positions[0]) * 9 + x
            break
        else:
            continue

    for t in list(enumerate(expanding_positions[1])):
        if y <= t[1]:
            y = t[0] * 9 + y
            break
        elif y > expanding_positions[1][-1]:
            y = len(expanding_positions[1]) * 9 + y
            break
        else:
            continue

    # for t in list(enumerate(expanding_positions[0])):
    #     if x <= t[1]:
    #         x = t[0] * 9 + x
    #         break
    #     elif x > expanding_positions[0][-1]:
    #         x = len(expanding_positions[0]) * 9 + x
    #         break
    #     else:
    #         continue
    #
    # for t in list(enumerate(expanding_positions[1])):
    #     if y <= t[1]:
    #         y = t[0] * 9 + y
    #         break
    #     elif y > expanding_positions[1][-1]:
    #         y = len(expanding_positions[1]) * 9 + y
    #         break
    #     else:
    #         continue

    return x, y


# def count_expansions(coordinates):



def calc_dist(coordinates, adjusted=False):
    c = coordinates
    if adjusted:
        c = list(map(adjust_coordinates, coordinates))
        return abs(c[1][0] - c[0][0]) + abs(c[1][1] - c[0][1])
    else:
        return abs(c[1][0] - c[0][0]) + abs(c[1][1] - c[0][1])


def get_dist_sum():
    coordinates = get_coordinates(grid)
    combinations_list = list(combinations(coordinates, 2))

    distances = [calc_dist(c) for c in combinations_list]
    distances2 = [calc_dist(c, True) for c in combinations_list]
    print(sum(distances), sum(distances2), expanding_positions)


if __name__ == '__main__':
    get_dist_sum()
