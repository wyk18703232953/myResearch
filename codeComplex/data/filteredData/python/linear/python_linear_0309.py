from collections import defaultdict
import bisect

def main(n):
    # Interpret n as both array size and modulus
    if n <= 0:
        return

    m = max(1, n)

    # Deterministically generate array a of length n
    # Example pattern: a[i] = (i * 2 + i // 3) % (2 * m) + i
    a = [((i * 2 + i // 3) % (2 * m)) + i for i in range(n)]

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
    for i in rem:
        for j in i:
            out[j[1]] = j[0]

    diff_sum = sum(out) - sum(a)
    out_str = ' '.join(map(str, out))

    # print(diff_sum)
    pass
    # print(out_str)
    pass
if __name__ == "__main__":
    main(10)