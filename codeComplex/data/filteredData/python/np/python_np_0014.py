def main(n):
    # generate a deterministic n x n matrix of floats
    b = [[((i + 1) * (j + 1)) / (n + 1) for j in range(n)] for i in range(n)]

    ma = 1 << n
    dp = [0.0 for _ in range(ma)]
    dp[0] = 1.0

    for mask in range(1, ma):
        l = n - bin(mask).count("1") + 1
        res = l * (l - 1) // 2
        if res == 0:
            continue
        for i in range(n):
            if mask & (1 << i):
                prev_mask = mask ^ (1 << i)
                base = dp[prev_mask] / res
                for j in range(n):
                    if not (mask & (1 << j)):
                        dp[mask] += base * b[j][i]

    ans = []
    full_mask = ma - 1
    for i in range(n):
        ans.append(dp[full_mask - (1 << i)])
    print(*ans)


if __name__ == "__main__":
    main(4)