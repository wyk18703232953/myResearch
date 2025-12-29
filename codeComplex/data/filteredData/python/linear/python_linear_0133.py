def main(n):
    # 生成规模为 n 的测试数据：一个长度为 n 的二进制串和参数 k
    # 这里示例：s0 为前 n 位的二进制展开的 1..n 的奇偶性（只是构造一个有点变化的串）
    # 你可以根据需要自行修改生成方式
    bits = []
    for i in range(1, n + 1):
        bits.append('1' if i % 2 == 0 else '0')
    s0 = ''.join(bits)
    # k 取一个与 n 相关的值，这里简单设置为 n // 2，最少为 1
    k = max(1, n // 2)

    s1 = s0[::-1]
    lens1 = len(s1)
    maxnum = 1005
    mod = 1000000007
    dp = [[0] * maxnum for _ in range(maxnum)]
    f = [0] * maxnum
    c = [[0] * maxnum for _ in range(maxnum)]

    def cntone(num):
        tmps = bin(num)[2:]
        cnt = 0
        for i in range(len(tmps)):
            if tmps[i] == '1':
                cnt += 1
        return cnt

    for i in range(1, maxnum):
        if i == 1:
            f[i] = 0
        else:
            f[i] = f[cntone(i)] + 1

    for i in range(maxnum):
        if i == 0:
            c[i][0] = 1
            continue
        for j in range(i + 1):
            if j == 0:
                c[i][j] = 1
            else:
                c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % mod

    for i in range(lens1):
        if i == 0:
            dp[i][0] = 1
            if s1[i] == '1':
                dp[i][1] = 1
            else:
                dp[i][1] = 0
            continue
        else:
            for j in range(0, i + 2):
                if j == 0:
                    dp[i][j] = 1
                    continue
                if s1[i] == '1':
                    dp[i][j] = (dp[i - 1][j - 1] + c[i][j]) % mod
                else:
                    dp[i][j] = dp[i - 1][j] % mod

    ans = 0

    for i in range(1, lens1 + 1):
        if f[i] == k - 1:
            ans = (ans + dp[lens1 - 1][i]) % mod

    if k == 0:
        ans = 1
    elif k == 1:
        ans -= 1
    else:
        ans = ans

    print(ans)


# 示例调用
if __name__ == "__main__":
    # 这里可修改 n 测试不同规模
    main(10)