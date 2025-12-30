import random

def main(n):
    # 1. 根据规模 n 生成测试数据：长度 m 的二进制串 s
    # 这里选取 m = max(1, n // 2)，可按需修改生成规则
    m = max(1, n // 2)
    s = [random.randint(0, 1) == 1 for _ in range(m)]

    # 2. 原逻辑开始
    z = [[0, 0]]
    for c in s:
        ind = z[-1][c]
        z[-1][c] = len(z)
        z.append(z[ind][:])
    assert len(z) == m + 1
    z[m][0] = z[m][1] = m  # make it sticky

    # how many things match directly
    dp = [0 for _ in range(m + 1)]
    dp[0] = 1
    for _ in range(n):
        ndp = [0 for _ in range(m + 1)]
        for i in range(m + 1):
            ndp[z[i][0]] += dp[i]
            ndp[z[i][1]] += dp[i]
        dp = ndp
    res = dp[m]

    for k in range(1, m):
        s0 = 0
        for c in s[-k:]:
            s0 = z[s0][c]
        dp = [0 for _ in range(m + 1)]
        dp[s0] = 1
        for _ in range(n - k):
            ndp = [0 for _ in range(m + 1)]
            for i in range(m + 1):
                ndp[z[i][0]] += dp[i]
                ndp[z[i][1]] += dp[i]
            dp = ndp
        for s1 in range(m):  # skip m
            v = dp[s1]
            for c in s[-k:]:
                if s1 == m:
                    v = 0
                s1 = z[s1][c]
            if s1 == m:
                res += v

    print(res)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)