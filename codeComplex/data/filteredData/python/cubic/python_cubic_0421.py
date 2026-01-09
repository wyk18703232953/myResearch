import math

def process(s):
    b = []
    for j in s:
        b.append(j)
    return b

def main(n):
    if n < 1:
        n = 1
    # Map n to grid size and k
    rows = n
    cols = n
    # Ensure k is even and scalable with n
    k = 2 * (n % 5 + 1)

    m = cols

    d1 = [[float("inf") for _ in range(m + 1)] for _ in range(rows + 1)]
    d2 = [[float("inf") for _ in range(m + 1)] for _ in range(rows + 1)]

    # Deterministic generation for horizontal edges (d1): rows x (cols-1)
    for i in range(rows):
        for j in range(m - 1):
            d1[i][j] = (i + 1) * (j + 2)

    # Deterministic generation for vertical edges (d2): (rows-1) x cols
    for i in range(rows - 1):
        for j in range(m):
            d2[i][j] = (i + 2) * (j + 1)

    n_local = rows
    m_local = cols

    if k % 2 != 0:
        ans = [[-1 for _ in range(m_local)] for _ in range(n_local)]

    else:
        ans = [[float('inf') for _ in range(m_local + 1)] for _ in range(n_local + 1)]
        for i in range(n_local):
            for j in range(m_local):
                ans[i][j] = min(
                    2 * d1[i][j],
                    2 * d1[i][j - 1] if j - 1 >= 0 else float('inf'),
                    2 * d2[i - 1][j] if i - 1 >= 0 else float('inf'),
                    2 * d2[i][j]
                )

        curr = 2
        while curr != k:
            new = [[float('inf') for _ in range(m_local + 1)] for _ in range(n_local + 1)]
            for i in range(n_local):
                for j in range(m_local):
                    left = ans[i][j - 1] + 2 * d1[i][j - 1] if j - 1 >= 0 else float('inf')
                    right = ans[i][j + 1] + 2 * d1[i][j] if j + 1 < m_local else float('inf')
                    up = ans[i - 1][j] + 2 * d2[i - 1][j] if i - 1 >= 0 else float('inf')
                    down = ans[i + 1][j] + 2 * d2[i][j] if i + 1 < n_local else float('inf')
                    new[i][j] = min(left, right, up, down)

            for i in range(n_local):
                for j in range(m_local):
                    ans[i][j] = new[i][j]

            curr += 2

    for i in range(n_local):
        # print(*ans[i][:m_local])
        pass
if __name__ == "__main__":
    main(5)