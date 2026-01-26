from collections import defaultdict
import bisect

def main(n):
    # ensure n >= 1
    if n <= 0:
        return

    # define m and a based on n, deterministically
    # let m be a divisor-ish of n to keep structure similar
    m = max(1, n // 3)
    # avoid m > n in extreme small cases
    if m > n:
        m = n

    # construct array a deterministically
    # pattern: a[i] = i*(i+1)//2 + (i % m)
    a = [i * (i + 1) // 2 + (i % m) for i in range(n)]

    rem = [[] for _ in range(m)]
    req = n // m
    ans = 0
    for i in range(n):
        rem[a[i] % m].append([a[i], i])
    ind = m - 1
    for i in range(m):
        size = len(rem[i])
        if size > req:
            ind = i
        if size < req:
            ok = False
            for j in range(ind, ind - m, -1):
                while len(rem[j]) > req:
                    pop, _ = rem[j].pop()
                    rem[i].append([pop + (i - j) % m, _])
                    if len(rem[i]) == req:
                        ok = True
                        break
                if ok:
                    break
                ind -= 1

    out = [0] * n
    for bucket in rem:
        for val, idx in bucket:
            out[idx] = val
    # print(sum(out) - sum(a))
    pass
    # print(' '.join(map(str, out)))
    pass
if __name__ == "__main__":
    main(20)