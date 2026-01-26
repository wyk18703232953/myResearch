import os
from collections import deque

def bfs_last_zero(n, m, starts):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    v = [[1] * (m + 2) for _ in range(n + 2)]
    # set borders to 0 (blocked/visited)
    for i in range(m + 2):
        v[0][i] = 0
        v[-1][i] = 0
    for i in range(n + 2):
        v[i][0] = 0
        v[i][-1] = 0
    # enqueue start points
    for x, y in starts:
        if 1 <= x <= n and 1 <= y <= m:
            q.append((x, y))
            v[x][y] = 0
    # if no valid starts, nothing to traverse
    if not q:
        return 0, 0
    # BFS
    while True:
        x, y = q.popleft()
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if v[xx][yy]:
                q.append((xx, yy))
                v[xx][yy] = 0
        if not q:
            return x, y

def main(n):
    # map n to grid size and number of starting points
    # ensure at least 1x1 grid
    rows = max(1, n)
    cols = max(1, n)
    # number of starting points k grows slowly with n
    k = max(1, (n + 1) // 2)

    # deterministically generate starting coordinates inside the grid
    starts = []
    for i in range(k):
        # simple deterministic pattern based on i
        x = (i % rows) + 1
        y = ((i * 2) % cols) + 1
        starts.append((x, y))

    x, y = bfs_last_zero(rows, cols, starts)
    # emulate original behavior of writing to a file by printing instead
    # print(f"{x} {y}")
    pass
if __name__ == "__main__":
    # example deterministic call
    main(10)