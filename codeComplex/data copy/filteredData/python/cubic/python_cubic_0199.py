def main(n):
    # deterministic generation of arr with values in [1, 2023]
    if n <= 0:
        return 0
    arr = [(i % 2023) + 1 for i in range(n)]

    max_v = 2024
    tracker = [[-1] * (n + 1) for _ in range(max_v)]

    d = [[] for _ in range(n)]
    for j, v in enumerate(arr):
        tracker[v][j] = j
        d[j].append(j)

    for v in range(1, max_v - 1):
        row_v = tracker[v]
        row_next = tracker[v + 1]
        for i in range(n):
            j = row_v[i]
            h = row_v[j + 1] if j != -1 and j + 1 < n + 1 else -1
            if j != -1 and h != -1:
                row_next[i] = h
                d[i].append(h)

    a = [i for i in range(1, n + 1)]
    for s in range(n):
        for pos in d[s]:
            if s > 0:
                cand = a[s - 1] + 1

            else:
                cand = 1
            if cand < a[pos]:
                a[pos] = cand
    return a[n - 1]


if __name__ == "__main__":
    # print(main(10))
    pass