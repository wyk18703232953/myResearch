def prof(f):
    return f


def report(f):
    return f


def mcheck(a, pairs):
    m = len(a[0])
    allm = 2 ** m - 1

    subs = {i: {i} for i in range(allm + 1)}

    for i in range(allm + 1):
        for j in range(i):
            if i | j == i:
                subs[i].add(j)

    mx = [max(aa) for aa in a]

    @prof
    def check(v):
        masks = {0: -1}
        done = [False] * (allm + 1)
        for i, aa in enumerate(a):
            if mx[i] < v:
                continue
            c = sum(1 << b for b in range(len(aa)) if aa[b] >= v)
            if not done[c]:
                for cc in subs[c]:
                    if allm - cc in masks:
                        other = masks[allm - c]
                        pairs[v] = (i, other)
                        return True
                    masks[cc] = i
                    done[cc] = True
        return False

    return check


@prof
def go(n, m, a):
    uniq = set()
    for aa in a:
        uniq.update(aa)

    uniq = sorted(uniq)
    pairs = {0: (0, 0)}
    check = mcheck(a, pairs)
    l = 0
    r = len(uniq) - 1
    if r < 0:
        print("1 1")
        return
    while l != r:
        if l + 1 == r:
            if check(uniq[r]):
                l = r
            else:
                r = l
            continue
        c = (l + r) // 2
        if check(uniq[c]):
            l = c
        else:
            r = c

    lval = uniq[l]
    if lval not in pairs:
        check(lval)
    a_idx = pairs[lval][0]
    b_idx = pairs[lval][1]
    if b_idx == -1:
        b_idx = a_idx

    print("%d %d" % (a_idx + 1, b_idx + 1))


def main(n):
    if n < 1:
        n = 1
    m = max(1, (n % 5) + 1)
    a = []
    for i in range(n):
        row = [(i + 1) * (j + 2) % (n + m + 3) for j in range(m)]
        a.append(tuple(row))
    go(n, m, a)


if __name__ == "__main__":
    main(10)