def main(n):
    # n: size of the input list ps
    # Deterministic generation of inputs:
    # Choose a and b as simple functions of n so they scale with n
    a = 2 * n + 3
    b = 3 * n + 5
    # Generate ps as a deterministic list of n integers
    # Make them diverse: some small, some larger via simple arithmetic
    ps = [(i * 2 + 1) % (4 * n + 7) for i in range(n)]

    mapping = set(ps)

    parents = {x: x for x in ps}
    parents['A'] = 'A'
    parents['B'] = 'B'
    ranks = {x: 0 for x in ps}
    ranks['A'] = 0
    ranks['B'] = 0

    def findSet(u):
        if parents[u] != u:
            parents[u] = findSet(parents[u])
        return parents[u]

    def unionSet(u, v):
        up = findSet(u)
        vp = findSet(v)
        if up == vp:
            return
        if ranks[up] > ranks[vp]:
            parents[vp] = up
        elif ranks[up] < ranks[vp]:
            parents[up] = vp

        else:
            parents[up] = vp
            ranks[vp] += 1

    for x in ps:
        if a - x in mapping:
            unionSet(x, a - x)

        else:
            unionSet(x, 'B')

        if b - x in mapping:
            unionSet(x, b - x)

        else:
            unionSet(x, 'A')

    if findSet('A') == findSet('B'):
        # print("NO")
        pass

    else:
        # print("YES")
        pass
        out = []
        for i in ps:
            if findSet(i) == findSet('A'):
                out.append('0')

            else:
                out.append('1')
        # print(' '.join(out))
        pass
if __name__ == "__main__":
    main(10)