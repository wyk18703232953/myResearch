def main(n):
    if n <= 0:
        print(-1)
        return

    # Deterministic construction of s and c based on n
    s = [i % 7 + (i // 3) for i in range(n)]
    c = [i % 5 + 1 for i in range(n)]

    dp = [float('inf')] * n
    for i in range(1, n):
        mn = float('inf')
        for j in range(i):
            if s[i] > s[j]:
                val = c[i] + c[j]
                if val < mn:
                    mn = val
        dp[i] = mn

    res = float('inf')
    for i in range(1, n):
        for j in range(i):
            if s[i] > s[j]:
                val = c[i] + dp[j]
                if val < res:
                    res = val
    if res == float('inf'):
        res = -1
    print(res)


if __name__ == "__main__":
    main(10)