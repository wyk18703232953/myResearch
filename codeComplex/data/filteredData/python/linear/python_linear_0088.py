def main(n):
    maxN = 10**6 + 5
    dp = [0] * maxN
    b = [0] * maxN

    # 生成确定性输入：N 组数据
    # 将 n 映射为 N，且 N 不超过 maxN
    N = max(1, min(n, maxN))

    # 确定性构造 beacon 数据
    # 使用不同的位置和值模式，覆盖各种分支情况
    for i in range(N):
        # 位置在 [0, maxN-1] 内均匀铺开
        pos = (i * 37) % maxN
        # 值在 [0, 1000] 范围的确定性构造
        val = (i * 97) % 1001
        b[pos] = val

    if b[0] > 0:
        dp[0] = 1

    for i in range(1, maxN):
        if b[i] == 0:
            dp[i] = dp[i - 1]

        else:
            if b[i] >= i:
                dp[i] = 1

            else:
                dp[i] = dp[i - b[i] - 1] + 1

    result = N - max(dp)
    return result


if __name__ == "__main__":
    # 示例调用，使用一个适中的规模参数
    # print(main(100000))
    pass