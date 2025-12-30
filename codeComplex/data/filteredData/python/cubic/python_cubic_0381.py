def main(n: int):
    # 生成测试数据：根据规模 n 构造 N 和 MOD
    # 例如：N = n，MOD 取一个常用的大质数
    N = n
    MOD = 10**9 + 7

    dp = []
    comps = [0] * (N + 1)

    # 预计算组合数 nCr，行数与原代码一致 420
    ncr = [[1]]
    for i in range(420):
        tmp = [1]
        for j in range(i):
            tmp.append((ncr[i][j] + ncr[i][j + 1]) % MOD)
        tmp.append(1)
        ncr.append(tmp)

    for i in range(N):
        curr = list(comps)
        curr[1] = pow(2, i, MOD)
        for j in range(i - 1):
            m = pow(2, i - j - 2, MOD)
            for k in range(N):
                num = j - k + 2
                if num < 0:
                    continue
                mr = (m * ncr[i - j - 1 + num][num]) % MOD
                curr[k + 1] += mr * dp[j][k]
                curr[k + 1] %= MOD
        dp.append(curr)

    ans = sum(dp[-1]) % MOD
    print(ans)


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的默认测试规模
    main(5)