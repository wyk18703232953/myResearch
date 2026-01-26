def main(n):
    if n <= 0:
        # print(-1)
        pass
        return

    # 构造确定性输入数据 a, b，长度均为 n
    a = [i % 7 for i in range(n)]
    b = [i % 5 + 1 for i in range(n)]

    dp = [0] * n
    for i in range(n):
        v = float('inf')
        for j in range(i + 1, n):
            if a[j] > a[i]:
                v = min(v, b[i] + b[j])
        dp[i] = v

    for i in range(n):
        v = float('inf')
        for j in range(i + 1, n):
            if a[j] > a[i]:
                v = min(v, b[i] + dp[j])
        dp[i] = v

    ans = min(dp)
    # print(ans if ans != float('inf') else -1)
    pass
if __name__ == "__main__":
    main(10)