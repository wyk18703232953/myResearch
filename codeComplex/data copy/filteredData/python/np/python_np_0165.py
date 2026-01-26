def main(n):
    # Interpret n as number of elements
    if n <= 0:
        print(0)
        return

    # Deterministic generation of n, l, r, x, and lis
    # n: number of elements
    # x: required minimum difference between max and min in subset
    # l, r: sum range for subsets
    x = max(1, n // 3)
    total_sum = n * (n + 1) // 2
    l = total_sum // 4 + 1
    r = total_sum // 2 + 1

    lis = [i for i in range(1, n + 1)]

    # Core logic from original solve()
    lis = sorted(lis)
    dp = [0]
    dp_low = [0]
    dp_high = [0]
    for i in range(len(lis)):
        current_len = len(dp)
        for j in range(current_len):
            if dp_low[j] == 0:
                dp_low.append(lis[i])
            else:
                dp_low.append(dp_low[j])
            dp_high.append(lis[i])
            dp.append(dp[j] + lis[i])
    count = 0
    for i in range(len(dp)):
        if dp[i] >= l and dp[i] <= r and dp_high[i] - dp_low[i] >= x:
            count += 1
    print(count)


if __name__ == "__main__":
    main(10)