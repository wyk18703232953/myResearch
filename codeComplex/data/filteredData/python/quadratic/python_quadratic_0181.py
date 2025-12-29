import random

def main(n: int):
    # 生成测试数据
    # values: 长度为 n 的随机整数数组
    values = [random.randint(0, 10**9) for _ in range(n)]

    # 生成查询数量（这里设为 n，按需可调整）
    queries = n

    # 预生成 queries 个合法的区间 [l, r]，1 <= l <= r <= n
    query_ranges = []
    for _ in range(queries):
        l = random.randint(1, n)
        r = random.randint(l, n)
        query_ranges.append((l, r))

    # 初始化 DP 数组
    dp = [[0] * 5009 for _ in range(5009)]

    # 第 0 行：原始值
    for i in range(n):
        dp[0][i] = values[i]

    # 构造基于异或的三角形
    for i in range(1, n):  # 0 已经填好
        for j in range(n - i + 1):
            top = dp[i - 1][j]
            right = dp[i - 1][j + 1]
            dp[i][j] = top ^ right

    # 对每条斜线取最大值
    for i in range(1, n):
        for j in range(n - i + 1):
            top = dp[i - 1][j]
            right = dp[i - 1][j + 1]
            dp[i][j] = max(right, max(dp[i][j], top))

    # 处理查询并输出
    for left, right in query_ranges:
        last_row = (right - 1) - (left - 1)
        last_column = (left - 1)
        print(dp[last_row][last_column])


if __name__ == "__main__":
    # 示例：调用 main(5)，可按需修改规模
    main(5)