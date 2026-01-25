def main(n):
    # 生成确定性的二进制字符串 a, b，满足 len(a) <= len(b)
    # 将 n 映射为长度，保证有意义的规模：len(a) = n, len(b) = 2n (n>=1)
    if n <= 0:
        return 0

    # 生成长度为 n 的二进制字符串 a
    # 第 i 位为 (i % 2)，保证有 0 有 1
    a = ''.join(str(i % 2) for i in range(n))

    # 生成长度为 2n 的二进制字符串 b
    # 使用简单算术构造一个周期为 3 的模式
    m = 2 * n
    b = ''.join(str((i % 3) // 2) for i in range(m))

    # 保留原程序的算法逻辑
    dp = [[0 for _ in range(2)] for _ in range(m + 1)]
    dp[1][0] = int(b[0]) ^ 1
    dp[1][1] = int(b[0])
    for i in range(2, m + 1):
        dp[i][0] = dp[i - 1][0] + (int(b[i - 1]) ^ 1)
        dp[i][1] = dp[i - 1][1] + int(b[i - 1])
    ans = 0
    for i in range(n):
        count0 = dp[m - n + i + 1][0] - dp[i][0]
        count1 = dp[m - n + i + 1][1] - dp[i][1]
        ans += count0 * int(a[i]) + count1 * (int(a[i]) ^ 1)
    print(ans)
    return ans


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 观察时间复杂度表现
    main(10)