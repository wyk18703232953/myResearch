from collections import deque
from random import randint

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solve(n, m, k, l):
    q = deque()
    v = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(0, 2 * k - 1, 2):
        x, y = l[i], l[i + 1]
        if 1 <= x <= n and 1 <= y <= m:
            q.append((x, y))
            v[x][y] = 1

    a = b = -1
    while q:
        a, b = q.popleft()
        for i in range(4):
            A, B = a + dx[i], b + dy[i]
            if 1 <= A <= n and 1 <= B <= m and not v[A][B]:
                q.append((A, B))
                v[A][B] = 1
    return a, b

def main(n):
    # 规模 n: 生成一个 n x n 的网格，k 个随机起点
    m = n
    # 至少 1 个起点，至多 n，避免过多
    k = max(1, min(n, 3))
    l = []
    used = set()
    while len(used) < k:
        x = randint(1, n)
        y = randint(1, m)
        if (x, y) not in used:
            used.add((x, y))
            l.extend([x, y])
    a, b = solve(n, m, k, l)
    print(a, b)

if __name__ == "__main__":
    # 示例: 规模为 5
    main(5)