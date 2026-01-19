def mcheck(a, pairs):
    m = len(a[0])
    allm = 2 ** m - 1

    subs = {i: {i} for i in range(allm + 1)}

    for i in range(allm + 1):
        for j in range(i):
            if i | j == i:
                subs[i].add(j)

    mx = [max(aa) for aa in a]

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


def core_algorithm(a):
    n = len(a)
    if n == 0:
        return 1, 1
    m = len(a[0])
    uniq = set()
    for row in a:
        uniq.update(row)
    uniq = sorted(uniq)
    if not uniq:
        return 1, 1
    pairs = {0: (0, 0)}
    check = mcheck(a, pairs)
    l = 0
    r = len(uniq) - 1
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
    l_val = uniq[l]
    if l_val not in pairs:
        check(l_val)
    a_idx = pairs[l_val][0]
    b_idx = pairs[l_val][1]
    if b_idx == -1:
        b_idx = a_idx
    return a_idx + 1, b_idx + 1


def generate_data(n):
    if n <= 0:
        n = 1
    n_rows = n
    m_cols = max(1, min(20, (n % 7) + 2))
    a = []
    for i in range(n_rows):
        row = []
        base = (i * 3) % 1000
        for j in range(m_cols):
            val = base + (j * 5 + i) % 17
            row.append(val)
        a.append(tuple(row))
    return a


def main(n):
    a = generate_data(n)
    i, j = core_algorithm(a)
    print("%d %d" % (i, j))


if __name__ == "__main__":
    main(10)