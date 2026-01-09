import sys

def main(n):
    # Deterministic parameter generation based on n
    # Ensure n is at least 2 to form a non-trivial tree
    if n < 2:
        n = 2
    # d grows like log n but at least 1 and at most n-1
    d = max(1, min(n - 1, n.bit_length()))
    # k at least 2, at most n
    k = max(2, min(n, 3 + (n % 5)))

    # Original logic starts here
    if d > n - 1:
        sys.stdout.write("NO\n")
        return

    par = [-1 for _ in range(n)]
    prevlevel = [0]
    bad = [False for _ in range(n)]
    clevel = []
    cdep = 1
    callow = k
    cnode = 1
    firstchild = 1

    for _ in range(1, n):
        if len(clevel) == callow:
            prevlevel = clevel
            clevel = []
            cdep += 1
            callow *= (k - 1)
            firstchild *= (k - 1)

        cdiv = k
        if cdep > 1:
            cdiv -= 1
        if cdiv == 0:
            sys.stdout.write("NO\n")
            return

        par[cnode] = prevlevel[len(clevel) // cdiv]
        clevel.append(cnode)

        cnode += 1

    mdep = d // 2

    if cdep > mdep + 1:
        sys.stdout.write("NO\n")
        return

    if cdep == mdep + 1 and (d % 2 == 0):
        sys.stdout.write("NO\n")
        return

    if cdep == mdep + 1 and len(clevel) > firstchild:
        sys.stdout.write("NO\n")
        return

    attach1 = -1
    attach2 = -1

    d1 = cdep
    d2 = cdep

    attach1 = clevel[0]
    if len(clevel) > firstchild:
        attach2 = clevel[-1]

    else:
        attach2 = prevlevel[-1]
        d2 -= 1

    te = attach1
    while te != -1:
        bad[te] = True
        te = par[te]
    te = attach2
    while te != -1:
        bad[te] = True
        te = par[te]

    cptr = n - 1
    while d1 + d2 < d:
        if bad[cptr]:
            cptr -= 1
            continue

        if d2 < d1:
            par[cptr] = attach2
            attach2 = cptr
            d2 += 1

        else:
            par[cptr] = attach1
            attach1 = cptr
            d1 += 1

        cptr -= 1

    sys.stdout.write("YES\n")
    for i in range(1, n):
        sys.stdout.write(str(i + 1) + " " + str(par[i] + 1) + "\n")


if __name__ == "__main__":
    main(10)