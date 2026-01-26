from collections import defaultdict, deque
from heapq import heappush, heappop
from math import inf

ri = lambda : map(int, input().split())

def solve():
    n,m = ri()
    A = [[0 for _ in range(m)] for __ in range(n)]
    left = [[0 for _ in range(m)] for __ in range(n)]
    right = [[0 for _ in range(m)] for __ in range(n)]
    up = [[0 for _ in range(m)] for __ in range(n)]
    down = [[0 for _ in range(m)] for __ in range(n)]
    for r in range(n):
        lst = input()
        for c in range(m):
            if lst[c] == '*':
                A[r][c] = left[r][c] = right[r][c] = up[r][c] = down[r][c] = 1

    for r in range(n):
        for c in range(1, m):
            if A[r][c]:
                left[r][c] += left[r][c-1]
        for c in range(m-2, -1, -1):
            if A[r][c]:
                right[r][c] += right[r][c+1]

    for c in range(m):
        for r in range(1, n):
            if A[r][c]:
                up[r][c] += up[r-1][c]

        for r in range(n-2, -1, -1):
            if A[r][c]:
                down[r][c] += down[r+1][c]
    res = []
    stars = 0

    ROWS = [[0 for _ in range(m)] for __ in range(n)]
    COLS = [[0 for _ in range(m)] for __ in range(n)]

    for r in range(n):
        for c in range(m):
            if A[r][c]:
                can = min(left[r][c], right[r][c], up[r][c], down[r][c])
                can -= 1
                if can > 0:
                    stars += 1
                    res.append((r+1, c+1, can))
                ROWS[r-can][c] += can
                if r+can+1 < n:
                    ROWS[r+can+1][c] -= can
                COLS[r][c-can] += can
                if c+can+1 < m:
                    COLS[r][c+can+1] -= can

    valid = [[False for _ in range(m)] for __ in range(n)]
    for r in range(n):
        curr = 0
        for c in range(m):
            curr += COLS[r][c]
            if curr > 0:
                valid[r][c] = True


    for c in range(m):
        curr = 0
        for r in range(n):
            curr += ROWS[r][c]
            if curr > 0:
                valid[r][c] = True

    for r in range(n):
        for c in range(m):
            if A[r][c] and not valid[r][c]:
                print(-1)
                return
    print(stars)
    for x,y,z in res:
        print(x,y,z)
t = 1
#t = int(input())
while t:
    t -= 1
    solve()

