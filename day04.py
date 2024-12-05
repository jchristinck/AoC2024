import re
import numpy as np


def get_diagonals(grid, anti=True):
    dim = len(grid)
    assert dim == len(grid[0])
    return_grid = [[] for _ in range(2 * len(grid) - 1)]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if anti:
                return_grid[row + col].append(grid[col][row])
            else:
                return_grid[col - row + (dim - 1)].append(grid[row][col])
    return [''.join(x) for x in return_grid]


inp = open("input/day04.txt", "r").read().splitlines()
normal = sum([len(re.findall("XMAS", x)) for x in inp])
backw = sum([len(re.findall("XMAS", x)) for x in [y[::-1] for y in inp]])
up = sum([len(re.findall("XMAS", x)) for x in [''.join(y) for y in zip(*inp)]])
down = sum([len(re.findall("XMAS", x)) for x in [''.join(y[::-1]) for y in zip(*inp)]])
matrix = np.array([list(x) for x in inp])
inp_diags = get_diagonals(matrix, True)
diags = sum([len(re.findall("XMAS", x)) for x in inp_diags])
bdiags = sum([len(re.findall("XMAS", x)) for x in [y[::-1] for y in inp_diags]])
inp_adiags = get_diagonals(matrix, False)
adiags = sum([len(re.findall("XMAS", x)) for x in inp_adiags])
badiags = sum([len(re.findall("XMAS", x)) for x in [y[::-1] for y in inp_adiags]])
print(normal + backw + up + down + diags + bdiags + adiags + badiags)  # 2549
