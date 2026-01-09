import bisect
import math
import itertools

alpha = 'abcdefghijklmnopqrstuvwxyz'
inf = 1e17

def calc1(grid):
    l = len(grid)
    cnt = 0
    for i in range(l):
        for j in range(l):
            if (i + j) % 2 and grid[i][j]:
                cnt += 1
            if (i + j) % 2 == 0 and grid[i][j] == 0:
                cnt += 1
    return cnt

def calc2(grid):
    l = len(grid)
    cnt = 0
    for i in range(l):
        for j in range(l):
            if (i + j) % 2 and grid[i][j] == 0:
                cnt += 1
            if (i + j) % 2 == 0 and grid[i][j]:
                cnt += 1
    return cnt

def solve(n, grids):
    one = []
    zero = []
    for grid in grids:
        one.append(calc1(grid))
        zero.append(calc2(grid))
    take = [3, 5, 6, 9, 10, 12]
    answer = inf
    for mask in range(16):
        cnt = 0
        if mask not in take:
            continue
        if mask in take:
            if mask & 1:
                cnt += one[3]

            else:
                cnt += zero[3]
            if mask & 2:
                cnt += one[2]

            else:
                cnt += zero[2]
            if mask & 4:
                cnt += one[1]

            else:
                cnt += zero[1]
            if mask & 8:
                cnt += one[0]

            else:
                cnt += zero[0]
        answer = min(answer, cnt)
    return answer

def generate_grids(n):
    grids = []
    for g in range(4):
        grid = []
        for i in range(n):
            row = []
            for j in range(n):
                val = ((g + 1) * (i + 1) * (j + 1)) % 2
                row.append(val)
            grid.append(row)
        grids.append(grid)
    return grids

def main(n):
    grids = generate_grids(n)
    result = solve(n, grids)
    # print(result)
    pass
if __name__ == "__main__":
    main(5)