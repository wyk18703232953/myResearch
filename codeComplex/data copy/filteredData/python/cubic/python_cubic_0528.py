from collections import Counter


def mx(f):
    res = []
    for k in sorted(f.keys(), reverse=True):
        for _ in range(f[k]):
            res.append(k)
    return res


def solve(n, a, b):
    res = None
    for k in range(n + 1):
        aa = Counter(a)
        cur = []
        for i in range(k):
            if aa[b[i]] == 0:
                return res
            cur.append(b[i])
            aa[b[i]] -= 1
        if k < n:
            for e in range(b[k] - 1, -1, -1):
                if aa[e] > 0:
                    cur.append(e)
                    aa[e] -= 1
                    cur.extend(mx(aa))
                    break
            if len(cur) < n:
                continue
        res = cur
    return res


def main(n):
    # Generate deterministic inputs based on n
    # a_str corresponds to the multiset of digits (first line in original)
    # b_str corresponds to the digit list (second line in original)
    if n <= 0:
        # print("")
        pass
        return

    # a_str: a sequence of digits with length 2*n, constructed deterministically
    # digits cycle through 0..9
    a_str = ''.join(str(i % 10) for i in range(2 * n))

    # b_str: a sequence of digits with length n, constructed deterministically
    # make it depend on n but still simple: (i * 3) % 10
    b_str = ''.join(str((i * 3 + n) % 10) for i in range(n))

    a = Counter(map(int, a_str))
    b = list(map(int, b_str))

    if sum(a.values()) < len(b):
        res = mx(a)

    else:
        res = solve(len(b), a, b)

    # print(''.join(map(str, res)))
    pass
if __name__ == "__main__":
    main(10)