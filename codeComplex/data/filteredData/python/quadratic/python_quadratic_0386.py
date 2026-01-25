from math import *
from cmath import *
from itertools import *
from decimal import *
from fractions import *
from sys import *
from types import CodeType, new_class

def main(n):
    # Interpret n as both number of rows and columns of the grid
    if n <= 0:
        return

    # Deterministically generate an n x n grid with 'B' forming a centered square
    size = n
    a = []

    # Choose a deterministic block size based on n
    block_size = max(1, n // 3)
    if block_size % 2 == 0:
        block_size -= 1
    if block_size <= 0:
        block_size = 1
    if block_size > n:
        block_size = n

    # Determine the bounds of the 'B' block
    min_block_row = (n - block_size) // 2
    max_block_row = min_block_row + block_size - 1
    min_block_col = (n - block_size) // 2
    max_block_col = min_block_col + block_size - 1

    for x in range(size):
        row_chars = []
        for y in range(size):
            if min_block_row <= x <= max_block_row and min_block_col <= y <= max_block_col:
                row_chars.append('B')
            else:
                row_chars.append('.')
        a.append(''.join(row_chars))

    # Original algorithm logic (translated to use generated data)
    n_rows, m_cols = size, size
    minx, miny, maxx, maxy = n_rows, m_cols, 0, 0
    for x in range(n_rows):
        for y in range(m_cols):
            if a[x][y] == 'B':
                minx = min(minx, x + 1)
                miny = min(miny, y + 1)
                maxx = max(maxx, x + 1)
                maxy = max(maxy, y + 1)

    # If there is no 'B' at all, do nothing
    if maxx == 0 and maxy == 0:
        return

    print((maxx + minx) // 2, (maxy + miny) // 2)

if __name__ == "__main__":
    main(7)