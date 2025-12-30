mod = 10**9 + 7

def main(n: int):
    # 生成测试数据：长度为 n 的指令序列 v[1..n]
    # 这里简单采用规则：奇数位为 'f'，偶数位为 's'
    # 你可以按需要改成随机或其他分布
    v = [None] * (n + 1)
    for i in range(1, n + 1):
        v[i] = 'f' if i % 2 == 1 else 's'

    # DP 数组：dp[i][l] 与原程序含义一致
    dp = [[0] * (n + 2) for _ in range(n + 1)]

    # 初始化：最后一行全部为 1
    for l in range(n + 2):
        dp[n][l] = 1

    # 自底向上的 DP 计算
    for i in range(n - 1, 0, -1):
        curr_sum = 0
        for l in range(n):
            curr_sum += dp[i + 1][l]
            curr_sum %= mod
            if v[i] == 'f':
                dp[i][l] = dp[i + 1][l + 1]
            else:
                dp[i][l] = curr_sum

    # 返回原程序最终输出
    return dp[1][0]


if __name__ == "__main__":
    # 示例：调用 main(5) 或其他规模
    print(main(5))