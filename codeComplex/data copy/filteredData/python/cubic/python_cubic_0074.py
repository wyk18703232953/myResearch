def main(n):
    from collections import deque

    mod = 1000000007
    INF = float('inf')

    # Deterministically map n to (rows, cols, number of starting points)
    # Ensure all are at least 1
    rows = max(1, n)
    cols = max(1, (n * 2) // 3 + 1)
    k = max(1, n // 3)

    # Generate k distinct starting positions within the grid deterministically
    # Using simple arithmetic; positions are 1-based as in the original code
    starts = []
    used = set()
    i = 0
    while len(starts) < k:
        r = (i * 2) % rows + 1
        c = (i * 3) % cols + 1
        if (r, c) not in used:
            used.add((r, c))
            starts.append((r, c))
        i += 1

    # Flatten starts to mimic original `l` list of length 2*k
    l = []
    for r, c in starts:
        l.append(r)
        l.append(c)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    n_rows, m_cols = rows, cols
    q = deque()
    v = [[0] * (m_cols + 1) for _ in range(n_rows + 1)]

    for i in range(0, 2 * k - 1, 2):
        a0, b0 = l[i], l[i + 1]
        q.append((a0, b0))
        v[a0][b0] = 1

    a = b = 1  # fallback initialization
    while q:
        a, b = q.popleft()
        for i in range(4):
            A, B = a + dx[i], b + dy[i]
            if 1 <= A <= n_rows and 1 <= B <= m_cols:
                if not v[A][B]:
                    q.append((A, B))
                    v[A][B] = 1

    # Return last visited cell instead of printing, for experiment use
    return a, b


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    result = main(10)
    # print(result[0], result[1])
    pass