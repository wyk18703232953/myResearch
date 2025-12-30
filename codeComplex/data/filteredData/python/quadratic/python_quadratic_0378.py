# A. Find Square (modified to use main(n) and generated test data)
import random

def main(n: int):
    # generate a random m (number of columns), at least 1
    m = max(1, n)

    # prepare an empty grid of '.'
    grid = [['.' for _ in range(m)] for _ in range(n)]

    # generate a random square size s (side length)
    s = random.randint(1, min(n, m))

    # choose random top-left position so that the square fits
    top_row = random.randint(0, n - s)
    left_col = random.randint(0, m - s)

    # fill the square with 'B'
    for i in range(top_row, top_row + s):
        for j in range(left_col, left_col + s):
            grid[i][j] = 'B'

    # run the original logic on the generated grid
    for i in range(n):
        s_row = ''.join(grid[i])
        left = s_row.find('B')
        if left != -1:
            right = s_row.rfind('B')
            c = (right - left) // 2 + 1
            print(i + c, left + c)
            break

if __name__ == "__main__":
    # example call; adjust n as needed
    main(5)