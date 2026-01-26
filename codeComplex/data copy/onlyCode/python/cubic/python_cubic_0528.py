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


a = Counter(map(int, input()))
b = list(map(int, input()))
if sum(a.values()) < len(b):
    res = mx(a)
else:
    res = solve(len(b), a, b)
print(''.join(map(str, res)))