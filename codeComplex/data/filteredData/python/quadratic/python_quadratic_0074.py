def nCr(n, r):
    from math import factorial
    f, m = factorial, 1
    for i in range(n, n - r, -1):
        m *= i
    return int(m // f(r))


def main(n):
    # n: length of array a, and also number of queries
    # deterministic construction of a: permutation-like values in [1, n]
    a = [(i * 2 % n) + 1 for i in range(n)]

    ans = []
    tem = 0
    mem = [0] * (n + 1)

    # original first phase using array a
    for i in range(n):
        for j in range(a[i] - 1, 0, -1):
            if not mem[j]:
                tem += 1
        mem[a[i]] = 1

    # deterministic generation of queries
    # q = n queries; l, r in [1, n], ensure l <= r and span grows with i
    q = n
    for i in range(q):
        l = i % n + 1
        r = min(n, l + (i // 2))
        tem += nCr(r - l + 1, 2)
        ans.append('odd' if tem % 2 else 'even')

    # print('\n'.join(ans))
    pass
if __name__ == "__main__":
    main(10)