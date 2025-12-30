import random
import sys

inf = float('inf')
MOD = 10**9 + 7
from math import gcd, floor, ceil


def multiLineArrayPrint(arr):
    print('\n'.join([str(x) for x in arr]))


def naiveSolve():
    return


def solve_single_case(grid):
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0

    # collect (value, column) for all cells
    valCol = []
    for i in range(n):
        for j in range(m):
            valCol.append((grid[i][j], j))
    valCol.sort(reverse=True)

    # choose top n columns by value
    topCols = set()
    for val, col in valCol:
        topCols.add(col)
        if len(topCols) == n:
            break

    m2 = len(topCols)
    # construct reduced grid with only selected columns
    grid2 = [[-1 for _ in range(m2)] for __ in range(n)]
    topColsList = list(topCols)
    for j in range(m2):
        col = topColsList[j]
        for i in range(n):
            grid2[i][j] = grid[i][col]

    # brute force over all cyclic shifts for each of the m2 columns
    ans = -inf
    total_states = n ** m2
    for mask in range(total_states):
        temp_mask = mask
        grid3 = [[-1 for _ in range(m2)] for __ in range(n)]
        for col in range(m2):
            shift = temp_mask % n
            temp_mask //= n
            for row in range(n):
                grid3[row][col] = grid2[(shift + row) % n][col]
        tempAns = 0
        for row in range(n):
            maxx = -inf
            for col in range(m2):
                if grid3[row][col] > maxx:
                    maxx = grid3[row][col]
            tempAns += maxx
        if tempAns > ans:
            ans = tempAns

    return ans


def main(n):
    """
    生成规模为 n 的测试数据并执行原逻辑。
    测试设计：
      - t = 1
      - n 行 n 列网格
      - 元素为 [1, 100] 的随机整数
    """
    random.seed(0)

    t = 1
    allans = []

    for _ in range(t):
        rows = n
        cols = n
        grid = [[random.randint(1, 100) for _ in range(cols)] for __ in range(rows)]
        ans = solve_single_case(grid)
        allans.append(ans)

    multiLineArrayPrint(allans)


if __name__ == "__main__":
    # 示例：将 n 设为 3 进行测试
    main(3)