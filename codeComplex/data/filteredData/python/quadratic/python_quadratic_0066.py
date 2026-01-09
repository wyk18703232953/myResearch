def main(n):
    # n controls the size of the initial array and the number of queries
    # Array d of length n, deterministic construction
    d = [(i * 3 + 7) % (2 * n + 1) for i in range(n)]

    odd = 0
    for i in range(n):
        for j in range(i, n):
            if d[i] > d[j]:
                odd ^= 1

    m = n  # number of queries scales with n
    ans = []
    for i in range(m):
        # deterministic construction of l, r within [0, n-1], with l <= r
        l = i % n
        r = (n - 1 - i) % n
        if l > r:
            l, r = r, l
        k = r - l + 1
        if (k * (k - 1) // 2) % 2:
            odd ^= 1
        ans.append("odd" if odd else "even")

    # print('\n'.join(ans))
    pass
if __name__ == "__main__":
    main(10)