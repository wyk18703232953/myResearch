def main(n):
    # Map n to grid dimensions and k
    # For example: m = n, k = 2 * n (even to trigger DP branch)
    if n <= 0:
        return
    m = n
    k = 2 * n

    # Deterministic generation of a (n x (m-1)) and b ((n-1) x m)
    # Original code expects:
    # a: n rows, m-1 horizontal edge costs per row (rightward edges)
    # b: n-1 rows, m   vertical edge costs per row (downward edges)
    # We can generate them using simple arithmetic based on indices.
    a = []
    for i in range(n):
        row = []
        for j in range(m - 1):
            row.append((i + 1) * (j + 2))
        a.append(row)

    b = []
    for i in range(n - 1):
        row = []
        for j in range(m):
            row.append((i + 2) * (j + 1))
        b.append(row)

    if k % 2:
        ans = [-1] * m
        for _ in range(n):
            # print(*ans)
            pass
        return

    k //= 2
    pre = [[0] * m for _ in range(n)]
    cur = [[10 ** 9] * m for _ in range(n)]
    for _ in range(k):
        cur = [[10 ** 9] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i:
                    cur[i][j] = min(cur[i][j], pre[i - 1][j] + b[i - 1][j])
                if i < n - 1:
                    cur[i][j] = min(cur[i][j], pre[i + 1][j] + b[i][j])
                if j:
                    cur[i][j] = min(cur[i][j], pre[i][j - 1] + a[i][j - 1])
                if j < m - 1:
                    cur[i][j] = min(cur[i][j], pre[i][j + 1] + a[i][j])
        pre = cur
    for i in range(n):
        cur[i] = [cur[i][j] * 2 for j in range(m)]
        # print(*cur[i])
        pass
if __name__ == "__main__":
    main(5)