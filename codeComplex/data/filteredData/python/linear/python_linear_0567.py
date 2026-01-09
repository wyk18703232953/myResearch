def main(n):
    # Generate a deterministic parent array p of length n-1
    # p[i] in [1, i+1] to ensure a valid rooted tree with root 0
    if n <= 0:
        return
    p = [(i // 2) + 1 for i in range(n - 1)]

    tr = {}
    for i in range(n - 1):
        parent = p[i] - 1
        if parent not in tr:
            tr[parent] = []
        tr[parent].append(i + 1)

    lc = [-1 for _ in range(n)]

    def get_lc(i):
        if lc[i] == -1:
            if i in tr:
                lc[i] = 0
                for j in tr[i]:
                    lc[i] += get_lc(j)

            else:
                lc[i] = 1
        return lc[i]

    for i in range(n - 1, -1, -1):
        get_lc(i)

    # print(*sorted(lc))
    pass
if __name__ == "__main__":
    # Example call for time complexity experiments
    main(10)