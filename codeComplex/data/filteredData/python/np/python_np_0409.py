import sys

def bs(a, mid, ans, n, m):
    can = [0 for _ in range(1 << m)]
    for i in range(n):
        t = 0
        for j in range(m):
            t = (t << 1) | (a[i][j] >= mid)
        can[t] = i + 1
    for i in range(1 << m):
        if not can[i]:
            continue
        for j in range(1 << m):
            if not can[j]:
                continue
            if i | j == (1 << m) - 1:
                ans[0] = can[i]
                ans[1] = can[j]
                return 1
    return 0

def main(n):
    # n controls both number of rows and columns for scalability
    if n <= 0:
        return
    m = max(1, n // 2)
    rows = n

    # Deterministic matrix generation
    # a[i][j] = (i + 1) * (j + 2) + (i // 2) + (j % 3)
    a = [
        [
            (i + 1) * (j + 2) + (i // 2) + (j % 3)
            for j in range(m)
        ]
        for i in range(rows)
    ]

    l = 0
    r = 10**11
    ans = [1, 1]
    while l <= r:
        mid = (l + r) // 2
        if bs(a, mid, ans, rows, m):
            l = mid + 1
        else:
            r = mid - 1
    print(ans[0], ans[1])

if __name__ == "__main__":
    main(10)