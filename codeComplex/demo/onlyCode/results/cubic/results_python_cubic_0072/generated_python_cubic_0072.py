def main(n):
    from collections import deque
    m = n
    k = max(1, n // 2)
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    a = []
    for i in range(1, k + 1):
        a.append((i % n) + 1)
        a.append((i % m) + 1)
    v = [[1] * (m + 2) for _ in range(n + 2)]
    for i in range(m + 2):
        v[0][i] = 0
        v[-1][i] = 0
    for i in range(n + 2):
        v[i][0] = 0
        v[i][-1] = 0
    for i in range(0, 2 * k, 2):
        x0, y0 = a[i], a[i + 1]
        if 1 <= x0 <= n and 1 <= y0 <= m and v[x0][y0]:
            q.append((x0, y0))
            v[x0][y0] = 0
    if not q:
        q.append((1, 1))
        v[1][1] = 0
    while True:
        x, y = q.popleft()
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if v[xx][yy]:
                q.append((xx, yy))
                v[xx][yy] = 0
        if not q:
            return x, y

if __name__ == "__main__":
    print(main(5))