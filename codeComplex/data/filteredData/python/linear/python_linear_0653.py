def main(n):
    # n: length of array a
    if n <= 0:
        print(0)
        return

    # deterministic generation of val and array a
    val = (n % 7) + 1
    # ensure values are in a bounded range, but depend deterministically on i and n
    a = [0] + [((i * 3 + n) % (n // 2 + 2) + 1) for i in range(1, n + 1)]

    suma = [0 for _ in range(n + 1)]
    mx = 0
    target = 0
    for i in range(1, n + 1):
        suma[i] = suma[i - 1]
        if a[i] > mx:
            mx = a[i]
        if a[i] == val:
            target += 1
            suma[i] += 1

    ans = 0
    pre = [0 for _ in range(mx + 1)]
    dp = [0]
    for i in range(1, n + 1):
        pi = pre[a[i]]
        dp.append(max(1, 1 + dp[pi] - suma[i] + suma[pi]))
        if a[i] != val and dp[i] > ans:
            ans = dp[i]
        pre[a[i]] = i
    print(ans + target)


if __name__ == "__main__":
    main(10)