from math import *
from cmath import *
from itertools import *
from decimal import *
from fractions import *
from types import CodeType, new_class

def solve_grid(a, n, m):
    minx, miny, maxx, maxy = n, m, 0, 0
    for x in range(n):
        for y in range(m):
            if a[x][y] == 'B':
                minx = min(minx, x + 1)
                miny = min(miny, y + 1)
                maxx = max(maxx, x + 1)
                maxy = max(maxy, y + 1)
    if maxx == 0 and maxy == 0:
        return 0, 0
    return (maxx + minx) // 2, (maxy + miny) // 2

def main(n):
    if n <= 0:
        return
    rows = n
    cols = n
    a = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if rows >= 3 and cols >= 3 and rows // 4 <= i <= (3 * rows) // 4 and cols // 4 <= j <= (3 * cols) // 4:
                row.append('B')

            else:
                row.append('W')
        a.append(''.join(row))
    cx, cy = solve_grid(a, rows, cols)
    # print(cx, cy)
    pass
if __name__ == "__main__":
    main(10)