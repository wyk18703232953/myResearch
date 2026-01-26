def main(n):
    # Generate deterministic input array b of length n
    # Values are in range [0, 2023] to match index range used in original code
    if n <= 0:
        # print(0)
        pass
        return
    b = [(i * 37 + 11) % 2024 for i in range(n)]

    # 2D array e with 2024 rows and n+1 columns, initialized to -1
    e = [[-1] * (n + 1) for _ in range(2024)]

    # List of lists d with n rows
    d = [[] for _ in range(n)]

    for i, v in enumerate(b):
        if 0 <= v < 2024:
            e[v][i] = i
        d[i].append(i)

    for v in range(1, 2023):
        row_v = e[v]
        row_vp1 = e[v + 1]
        for i in range(n):
            j = row_v[i]
            h = row_v[j + 1] if j != -1 and j + 1 <= n else -1
            if j != -1 and h != -1:
                row_vp1[i] = h
                d[i].append(h)

    a = [i for i in range(1, n + 1)]
    for s in range(n):
        for idx in d[s]:
            if s > 0:
                candidate = a[s - 1] + 1

            else:
                candidate = 1
            if candidate < a[idx]:
                a[idx] = candidate

    # print(a[n - 1])
    pass
if __name__ == "__main__":
    main(1000)