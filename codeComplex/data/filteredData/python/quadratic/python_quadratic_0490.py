def main(n):
    def update(l, r, i, res, n):
        j = 0
        while j < i:
            if res[j] is None:
                r[j] -= 1
                if r[j] < 0:
                    return False
            j += 1
        j += 1
        while j < n:
            if res[j] is None:
                l[j] -= 1
                if l[j] < 0:
                    return False
            j += 1
        return True

    # deterministic generation of l and r based on n
    # l[i] counts how many unassigned positions must be on the left of i
    # r[i] counts how many unassigned positions must be on the right of i
    l = [i % (n // 3 + 1) for i in range(n)]
    r = [(n - 1 - i) % (n // 3 + 1) for i in range(n)]

    ilist = {1}
    res = [None] * n
    cur = n

    while ilist and (sum(l) != 0 or sum(r) != 0):
        ilist = set()
        for i in range(n):
            if l[i] == r[i] == 0 and res[i] is None:
                res[i] = cur
                ilist.add(i)
        for i in ilist:
            check = update(l, r, i, res, n)
            if not check:
                return False
        cur -= 1
    if not ilist:
        return False
    for i in range(n):
        if res[i] is None:
            res[i] = cur
    return res


if __name__ == "__main__":
    n = 10
    res = main(n)
    if not res:
        print("NO")
    else:
        print("YES")
        for x in res:
            print(x, end=" ")