# https://codeforces.com/problemset/problem/35/C

from sys import stdin, exit
from typing import List, Tuple, Dict
from itertools import product


def distance(tree: Tuple[int, int], outbreak: Tuple[int, int]):
    return abs(tree[0] - outbreak[0]) + abs(tree[1] - outbreak[1])


def shorthest_path(tree: Tuple[int, int], outbreaks: List[Tuple[int, int]], min_dst: int):
    shorthest_path = float('inf')
    for outbreak in outbreaks:
        if shorthest_path < min_dst:
            break
        shorthest_path = min(shorthest_path, distance(tree, outbreak))
    return shorthest_path


input_f = open('input.txt', 'r')
output_f = open('output.txt', 'w')

N, M = [int(v) for v in input_f.readline().rstrip().split()]
input_f.readline()  # ignore
outbreaks_line = [int(v) for v in input_f.readline().rstrip().split()]
outbreaks = []
input_f.close()


for i in range(0, len(outbreaks_line) - 1, 2):
    outbreaks.append((outbreaks_line[i], outbreaks_line[i+1]))

last_tree = (1, 1)
best_dst = 0
for x, y in product(range(1, N + 1), range(1, M + 1)):
    path_len = shorthest_path((x, y), outbreaks, best_dst)
    if path_len > best_dst:
        last_tree = (x, y)
        best_dst = path_len

output_f.write(' '.join(map(str, last_tree)))
# print(' '.join(map(str, last_tree)))

output_f.close()
