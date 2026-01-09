def main(n):
    # Deterministically generate s and c based on n
    # s: strictly increasing to allow many valid pairs
    s = [i for i in range(1, n + 1)]
    # c: some deterministic cost pattern
    c = [i % 7 + 1 for i in range(n)]

    dp = [float('inf')] * n
    for i in range(1, n):
        mn = float('inf')
        for j in range(i):
            if s[i] > s[j]:
                cost = c[i] + c[j]
                if cost < mn:
                    mn = cost
        dp[i] = mn

    res = float('inf')
    for i in range(1, n):
        for j in range(i):
            if s[i] > s[j]:
                cost = c[i] + dp[j]
                if cost < res:
                    res = cost
    if res == float('inf'):
        res = -1
    # print(res)
    pass
if __name__ == "__main__":
    main(10)