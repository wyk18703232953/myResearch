from collections import defaultdict
import bisect

def main(n):
    # Generate deterministic test data:
    # Let m be a divisor-related size; ensure m >= 1 and m <= n (if n > 0).
    if n <= 0:
        return
    m = max(1, n // 3)
    if m > n:
        m = n

    # Original code expects:
    # n, m
    # a: list of length n
    # We generate a[i] in a deterministic pattern with varied residues.
    a = [(i * 2 + i // 3) % (3 * m + 7) for i in range(n)]

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
            for j in range(ind, -1, -1):
                while len(rem[j]) > req:
                    pop, _ = rem[j].pop()
                    rem[i].append([pop + (i - j) % m, _])
                    if len(rem[i]) == req:
                        ok = True
                        break
                if ok:
                    break
                ind -= 1
            else:
                ind = m - 1
                for j in range(ind, -1, -1):
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
    print(sum(out) - sum(a))
    print(' '.join(map(str, out)))


if __name__ == "__main__":
    main(1000)