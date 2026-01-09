from collections import defaultdict
import bisect

def main(n):
    # n: length of array a; also used to define m for scalability
    if n <= 0:
        return

    # Define m as a deterministic function of n, ensuring m >= 1
    m = max(1, n // 3 + 1)

    # Deterministic construction of array a of length n
    # Example pattern: quadratic-linear combination to create diverse residues
    a = [(i * i + 3 * i + 7) for i in range(n)]

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
    main(10)