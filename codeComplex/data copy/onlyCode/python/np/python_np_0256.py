from sys import stdin
from itertools import permutations

rints = lambda: [int(x) for x in stdin.readline().split()]
x1, y1, x2, y2, x3, y3 = rints()

for x in [[x1, y1], [y1, x1]]:
    for y in [[x2, y2], [y2, x2]]:
        for z in [[x3, y3], [y3, x3]]:
            if x[1] == y[1] == z[1] and x[0] + y[0] + z[0] == x[1]:
                print(x[1])
                print('\n'.join(
                    ['A' * x[1] for _ in range(x[0])] + ['B' * x[1] for _ in range(y[0])] + ['C' * z[1] for _ in
                                                                                             range(z[0])]))
                exit()

for per in permutations([[[x1, y1], [y1, x1], 'A'], [[x2, y2], [y2, x2], 'B'], [[x3, y3], [y3, x3], 'C']], 3):
    for x in per[0][:-1]:
        for y in per[1][:-1]:
            for z in per[2][:-1]:
                if x[1] == (y[1] + z[1]) and y[0] == z[0] and x[1] == x[0] + y[0]:
                    print(x[1])
                    print('\n'.join(
                        [per[0][-1] * x[1] for _ in range(x[0])] + [per[1][-1] * y[1] + per[2][-1] * z[1] for _ in
                                                                    range(y[0])]))
                    exit()

print(-1)
