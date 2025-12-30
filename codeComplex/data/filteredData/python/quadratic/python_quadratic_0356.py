from collections import defaultdict, deque
from heapq import heappush, heappop
from math import inf
import random

def main(n):
    # 生成一个 n x n 的随机'*'和'.'网格，保证至少有一些'*'
    m = n
    A = [[0 for _ in range(m)] for __ in range(n)]
    left = [[0 for _ in range(m)] for __ in range(n)]
    right = [[0 for _ in range(m)] for __ in range(n)]
    up = [[0 for _ in range(m)] for __ in range(n)]
    down = [[0 for _ in range(m)] for __ in range(n)]

    # 随机生成网格；p 为出现 '*' 的概率
    p = 0.4
    for r in range(n):
        for c in range(m):
            if random.random() < p:
                A[r][c] = 1
                left[r][c] = right[r][c] = up[r][c] = down[r][c] = 1

    # 若全部是 '.'，强制随机放一个 '*'
    if all(A[r][c] == 0 for r in range(n) for c in range(m)):
        r = random.randrange(n)
        c = random.randrange(m)
        A[r][c] = 1
        left[r][c] = right[r][c] = up[r][c] = down[r][c] = 1

    # 预处理 left/right
    for r in range(n):
        for c in range(1, m):
            if A[r][c]:
                left[r][c] += left[r][c - 1]
        for c in range(m - 2, -1, -1):
            if A[r][c]:
                right[r][c] += right[r][c + 1]

    # 预处理 up/down
    for c in range(m):
        for r in range(1, n):
            if A[r][c]:
                up[r][c] += up[r - 1][c]
        for r in range(n - 2, -1, -1):
            if A[r][c]:
                down[r][c] += down[r + 1][c]

    res = []
    stars = 0

    ROWS = [[0 for _ in range(m)] for __ in range(n)]
    COLS = [[0 for _ in range(m)] for __ in range(n)]

    # 计算每个点能作为中心的最大十字臂长
    for r in range(n):
        for c in range(m):
            if A[r][c]:
                can = min(left[r][c], right[r][c], up[r][c], down[r][c])
                can -= 1
                if can > 0:
                    stars += 1
                    res.append((r + 1, c + 1, can))
                if r - can >= 0:
                    ROWS[r - can][c] += can
                if r + can + 1 < n:
                    ROWS[r + can + 1][c] -= can
                if c - can >= 0:
                    COLS[r][c - can] += can
                if c + can + 1 < m:
                    COLS[r][c + can + 1] -= can

    valid = [[False for _ in range(m)] for __ in range(n)]

    # 按列差分扫描
    for r in range(n):
        curr = 0
        for c in range(m):
            curr += COLS[r][c]
            if curr > 0:
                valid[r][c] = True

    # 按行差分扫描
    for c in range(m):
        curr = 0
        for r in range(n):
            curr += ROWS[r][c]
            if curr > 0:
                valid[r][c] = True

    # 验证每个 '*' 是否被某个十字覆盖
    for r in range(n):
        for c in range(m):
            if A[r][c] and not valid[r][c]:
                print(-1)
                return

    print(stars)
    for x, y, z in res:
        print(x, y, z)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)