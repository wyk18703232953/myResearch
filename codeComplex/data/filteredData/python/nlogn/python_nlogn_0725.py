def main(n):
    # Generate n "tile" strings as deterministic input.
    # We only need up to 3 items because original code uses first 3 tokens.
    # Map n to up to 3 tiles.
    kinds = ['m', 'p', 's']
    tiles = []
    # Deterministically generate up to 3 tiles based on n
    for i in range(3):
        if i >= n:
            break
        v = (n + i) % 9 + 1  # value 1..9
        k = kinds[(n + i) % 3]
        tiles.append(str(v) + k)

    t = tiles[:3]
    sset = set(t)
    res = 3
    if len(sset) == 1:
        res = min(res, 0)
    elif len(sset) == 2:
        res = min(res, 1)
    elif len(sset) == 3:
        res = min(res, 2)
    if res == 0:
        print(res)
        return

    t.sort()
    m = [int(a[0]) for a in t if a[1] == 'm']
    p = [int(a[0]) for a in t if a[1] == 'p']
    s = [int(a[0]) for a in t if a[1] == 's']

    def f(a):
        res_inner = 2
        aset = set(a)
        for i in aset:
            if ((i - 1 in aset and i + 1 in aset) or
                (i - 2 in aset and i - 1 in aset) or
                (i + 1 in aset and i + 2 in aset)):
                return 0
            elif (i - 1 in aset or i + 1 in aset or
                  i - 2 in aset or i + 2 in aset):
                res_inner = min(res_inner, 1)
        return res_inner

    res = min([res, f(m), f(p), f(s)])
    print(res)


if __name__ == "__main__":
    main(3)