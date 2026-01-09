def main(n):
    # Scale definition:
    #   m: modulus
    #   n: length of the array
    # For determinism and scalability, set m as a function of n
    # Ensure m >= 1 and not too large relative to n
    if n <= 0:
        return

    # Example deterministic choice: m roughly sqrt(n), at least 1
    m = max(1, int(n**0.5))

    # Generate a deterministic array arr of length n
    # Use simple arithmetic patterns
    arr = [(i * 3 + 7) % (5 * m + 10) for i in range(n)]

    dp = [[] for _ in range(m)]
    for i in range(n):
        dp[arr[i] % m].append(i)

    res = 0
    k = n // m
    ans = arr.copy()
    s = []
    for _ in range(2):
        for i in range(m):
            if len(dp[i]) < k:
                while len(s) != 0 and len(dp[i]) < k:
                    x = s.pop()
                    y = arr[x] % m
                    if i > y:
                        ans[x] = ans[x] + (i - y)
                        res = res + (i - y)

                    else:
                        ans[x] = ans[x] + (m - 1 - y) + (i + 1)
                        res = res + (m - 1 - y) + (i + 1)
                    dp[i].append("xxx")
            if len(dp[i]) > k:
                while len(dp[i]) > k:
                    s.append(dp[i].pop())

    # print(res)
    pass
    # print(*ans)
    pass
if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(10_000)