import random

def main(n: int):
    # 1. 根据规模 n 生成 R, G, B
    #    控制总规模在 O(n) 级别：R + G + B ≈ n
    #    并避免出现 0 长度的颜色数组
    if n < 3:
        n = 3
    # 随机拆分 n 为三份
    R = random.randint(1, n - 2)
    G = random.randint(1, n - R - 1)
    B = n - R - G

    # 2. 生成测试数据：red, green, blue 为随机整数数组
    #    可根据需要调整数值范围
    red = sorted(
        [random.randint(1, 1000) for _ in range(R)],
        reverse=True
    )
    green = sorted(
        [random.randint(1, 1000) for _ in range(G)],
        reverse=True
    )
    blue = sorted(
        [random.randint(1, 1000) for _ in range(B)],
        reverse=True
    )

    # 3. 初始化 dp 数组
    dp = [[[-1] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]

    # 4. 递归函数，捕获外部变量
    def rec(r, g, b):
        if dp[r][g][b] != -1:
            return dp[r][g][b]
        ans = 0
        if r < R and g < G:
            ans = max(ans, red[r] * green[g] + rec(r + 1, g + 1, b))
        if r < R and b < B:
            ans = max(ans, red[r] * blue[b] + rec(r + 1, g, b + 1))
        if b < B and g < G:
            ans = max(ans, blue[b] * green[g] + rec(r, g + 1, b + 1))
        dp[r][g][b] = ans
        return ans

    # 5. 执行并输出结果
    result = rec(0, 0, 0)
    print(result)


if __name__ == "__main__":
    # 示例：n = 10，可根据需要修改
    main(10)