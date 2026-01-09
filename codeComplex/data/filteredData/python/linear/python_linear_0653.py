def main(n):
    # Deterministic data generation
    # a will be a permutation-like sequence with values in [1, n]
    a = [0] + [i % n + 1 for i in range(1, n + 1)]
    # Choose val deterministically based on n
    val = (n // 2) % n + 1 if n > 0 else 1

    suma = [0 for _ in range(n + 1)]
    mx = 0
    target = 0
    for i in range(1, n + 1):
        suma[i] = suma[i - 1]
        mx = max(mx, a[i])
        if a[i] == val:
            target += 1
            suma[i] += 1

    ans = 0
    pre = [0 for _ in range(mx + 1)]
    dp = [0]
    for i in range(1, n + 1):
        dp.append(max(1, 1 + dp[pre[a[i]]] - suma[i] + suma[pre[a[i]]]))
        if a[i] != val:
            ans = max(ans, dp[i])
        pre[a[i]] = i
    # print(ans + target)
    pass
if __name__ == "__main__":
    main(10)