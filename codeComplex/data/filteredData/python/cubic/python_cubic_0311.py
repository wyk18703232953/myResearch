import random

def main(n: int):
    # 根据规模 n 生成 R, G, B（可按需要调整策略）
    # 这里简单设置为三种颜色长度都为 n
    R = G = B = n

    # 生成测试数据：随机正整数列表
    # 可改为其他分布或固定数据
    rl = sorted([random.randint(1, 1000) for _ in range(R)], reverse=True)
    gl = sorted([random.randint(1, 1000) for _ in range(G)], reverse=True)
    bl = sorted([random.randint(1, 1000) for _ in range(B)], reverse=True)

    # 三维 DP 初始化
    dp = [[[-1] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]

    def cal(r, g, b):
        if dp[r][g][b] != -1:
            return dp[r][g][b]
        ans = 0
        if r < R and g < G:
            ans = max(ans, rl[r] * gl[g] + cal(r + 1, g + 1, b))
        if r < R and b < B:
            ans = max(ans, rl[r] * bl[b] + cal(r + 1, g, b + 1))
        if g < G and b < B:
            ans = max(ans, gl[g] * bl[b] + cal(r, g + 1, b + 1))
        dp[r][g][b] = ans
        return ans

    result = cal(0, 0, 0)
    print(result)


if __name__ == "__main__":
    # 示例：运行规模 n=5
    main(5)