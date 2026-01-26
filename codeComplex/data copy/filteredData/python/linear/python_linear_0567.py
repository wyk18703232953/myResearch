def main(n):
    # n: number of nodes in the tree
    if n <= 0:
        return

    # deterministically generate parent array p of length n-1
    # root is node 0; for i in [1..n-1], parent of i is (i-1)//2
    p = [(i - 1) // 2 + 1 for i in range(1, n)]

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
                total = 0
                for j in tr[i]:
                    total += get_lc(j)
                lc[i] = total

            else:
                lc[i] = 1
        return lc[i]

    for i in range(n - 1, -1, -1):
        get_lc(i)

    # print(*sorted(lc))
    pass
if __name__ == "__main__":
    main(10)